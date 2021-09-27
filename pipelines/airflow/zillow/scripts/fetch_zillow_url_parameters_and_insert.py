import sys
sys.path.append('/opt/airflow')

import json, requests, re, os
from zillow.tests_data.test_houston_zipcodes_list import houston_zipcodes
from zillow.scripts_functions.request_parameters import header, proxies
from zillow.scripts_functions.request_proxy import request_proxy_tries


def fetch_zillow_url_parameter(zipcode :str) -> str:
    url = 'https://www.zillow.com/homes/{zipcode}_rb/'.format(zipcode=zipcode)
    url_html_page = request_proxy_tries("GET", url).text
    zillow_url_parameters = re.search('<!--{"queryState":(.*),"isMapVisible":true,"filterState":{"',
                                      url_html_page).group(1)
    zillow_url_parameters = json.loads(zillow_url_parameters + "}")
    print(zipcode)
    return {
            "zipcode": zillow_url_parameters["usersSearchTerm"],
            "mapBounds": zillow_url_parameters["mapBounds"],
            "regionSelection": zillow_url_parameters["regionSelection"]
            }

# airflow tasks test zillow_pipeline fetch_all_region_id_and_insert 2021-09-12
def fetch_zillow_url_parameters_and_insert(zipcodes: list):
    zillow_url_parameters = []
    for zipcode in zipcodes:
        # region_id = fetch_region_id(zipcode)

        zillow_url_parameter = fetch_zillow_url_parameter(zipcode)
        zipcode = zillow_url_parameter["zipcode"]
        region_id = zillow_url_parameter["regionSelection"][0]["regionId"]
        region_type = zillow_url_parameter["regionSelection"][0]["regionType"]
        west = zillow_url_parameter["mapBounds"]["west"]
        east = zillow_url_parameter["mapBounds"]["east"]
        north = zillow_url_parameter["mapBounds"]["north"]
        south = zillow_url_parameter["mapBounds"]["south"]

        zillow_url_parameters.append({
            "region_id": int(region_id),
            "region_type": region_type,
            "zipcode": int(zipcode),
            "west": west,
            "east": east,
            "north": north,
            "south": south
        })

    try:
        # INSERT ALL URL PARAMETERS TO DB
        zillow_url_parameters_api = "{API_BASE_URL}zillowUrlParameters".format(API_BASE_URL=os.environ["API_BASE_URL"])
        requests.post(zillow_url_parameters_api, data=json.dumps(zillow_url_parameters), headers={'content-type': 'application/json'})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    fetch_zillow_url_parameters_and_insert(houston_zipcodes)
