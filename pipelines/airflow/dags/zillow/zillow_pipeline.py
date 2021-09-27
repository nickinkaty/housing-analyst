# CHECK REALESTATE API DATA IS AVAILABLE
import json

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import timedelta, datetime

default_args = {
    "owner": "airflow",
    'depends_on_past': False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("zillow_pipeline",
         start_date=datetime(2021, 9, 12),
         schedule_interval="@monthly",
         default_args=default_args,
         catchup=False
         ) as dag:

    fetch_all_region_id_and_insert = BashOperator(
        task_id='fetch_all_region_id_and_insert',
        bash_command='python ${AIRFLOW_ZILLOW_DAGS_PY_SCRIPTS_FOLDER}/fetch_zillow_url_parameters_and_insert.py',
    )

    fetch_real_estates_and_insert = BashOperator(
        task_id='fetch_real_estates_and_insert',
        bash_command='python ${AIRFLOW_ZILLOW_DAGS_PY_SCRIPTS_FOLDER}/fetch_real_estates_and_insert.py',
    )

fetch_all_region_id_and_insert >> fetch_real_estates_and_insert