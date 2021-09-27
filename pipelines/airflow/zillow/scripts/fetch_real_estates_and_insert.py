import os
import sys
import requests

sys.path.append('/opt/airflow')

from zillow.scripts_functions.request_proxy import request_proxy_tries
from zillow.scripts_functions.request_parameters import header, proxies
from zillow.scripts_functions.clean_data import clean_real_estate_data


# airflow tasks test zillow_pipeline fetch_real_estates_and_insert 2021-09-12
def fetch_real_estates_insert(region_id: str) -> None:
    zillow_url_parameters_api = "{API_BASE_URL}zillowUrlParameters".format(API_BASE_URL=os.environ["API_BASE_URL"])
    r_zillow_url_parameters = requests.get(zillow_url_parameters_api).json()
    zillow_url_parameters = r_zillow_url_parameters["data"];
    # print(zillow_url_parameters)

    zillow_real_estates_results = []
    for zillow_url_parameter in zillow_url_parameters:
        zipcode = zillow_url_parameter["zipcode"]
        region_id = zillow_url_parameter["region_id"]
        region_type = zillow_url_parameter["region_type"]
        west = zillow_url_parameter["west"]
        east = zillow_url_parameter["east"]
        south = zillow_url_parameter["south"]
        north = zillow_url_parameter["north"]
        zillow_real_estate_url = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={{"pagination":{{"currentPage":{page}}},"usersSearchTerm":"{zipcode}","mapBounds":{{"west":{west},"east":{east},"south":{south},"north":{north}}},"regionSelection":[{{"regionId":{region_id},"regionType":{region_type}}}],"isMapVisible":false,"filterState":{{"sortSelection":{{"value":"globalrelevanceex"}},"isAllHomes":{{"value":true}}}},"isListVisible":true}}&wants={{"cat1":["listResults"],"cat2":["total"]}}&requestId=2'
        zillow_real_estate_url_formatted = zillow_real_estate_url.format(page=1, zipcode=zipcode, region_id=region_id,
                                                                         region_type=region_type, west=west, east=east,
                                                                         south=south, north=north)

        # FETCH THE TOTAL PAGES
        zillow_real_estates = request_proxy_tries("GET", zillow_real_estate_url_formatted).json()
        total_pages = zillow_real_estates["cat1"]["searchList"]["totalPages"]

        page = 1
        while page < total_pages + 1:
            zillow_real_estate_url_formatted = zillow_real_estate_url.format(page=page, zipcode=zipcode,
                                                                             region_id=region_id,
                                                                             region_type=region_type, west=west,
                                                                             east=east, south=south, north=north)

            zillow_real_estates = request_proxy_tries("GET", zillow_real_estate_url_formatted).json()

            zillow_real_estates_result = zillow_real_estates["cat1"]["searchResults"]["listResults"]
            for zillow_real_estates_json in zillow_real_estates_result:
                zillow_real_estates_results.append(zillow_real_estates_json)

            page += 1

    clean_real_estate_results = clean_real_estate_data(zillow_real_estates_results)

    divide_number = 500
    real_estate_api_calls = [clean_real_estate_results[i:i + divide_number] for i in
                             range(0, len(clean_real_estate_results), divide_number)]

    # INSERT REAL ESTATE RESULT INTO POSTGRES
    for real_estate_api_call in real_estate_api_calls:
        real_estate_url_api_url = "{API_BASE_URL}realestates".format(API_BASE_URL=os.environ["API_BASE_URL"])
        r_real_estate = requests.post(real_estate_url_api_url, json=real_estate_api_call)
        # print(r_real_estate.content)


if __name__ == "__main__":
    fetch_real_estates_insert("1")
