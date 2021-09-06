# CHECK REALESTATE API DATA IS AVAILABLE
import json

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import timedelta, datetime

proxies = {
    "http": "http://248975009710735361-st-us_texas:ASYVCP04GX7FMWF@resi.linkproxy.lighting:8000/",
    "https": "https://248975009710735361-st-us_texas:ASYVCP04GX7FMWF@resi.linkproxy.lighting:8000/",
}

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("zillow_pipeline",
         start_date=datetime(2021, 8, 14),
         schedule_interval="@monthly",
         default_args=default_args,
         catchup=False
         ) as dag:

    fetch_all_region_id = BashOperator(
        task_id='fetch_all_region_id',
        bash_command='python ${AIRFLOW_ZILLOW_DAGS_PY_SCRIPTS_FOLDER}/fetch_zillow_url_parameters_and_insert.py',
    )

    is_real_estates_available = HttpSensor(
        task_id="is_real_estates_available",
        http_conn_id="zillow_api",
        endpoint='search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":2},"usersSearchTerm":"77493","mapBounds":{"west":-95.907893,"east":-95.773356,"south":29.785206,"north":29.950635},"regionSelection":[{"regionId":91981,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
        response_check=lambda response: True if response.status_code == 200 else False,
        poke_interval=5,
        timeout=20
    )

fetch_all_region_id >> is_real_estates_available
