import requests
from requests.auth import HTTPBasicAuth


def fetch_zipcodes_by_city_state(city: str, state: str) -> str:
    zipcodes = requests.get(
        "https://service.zipapi.us/zipcode/zips?X-API-KEY=e289a762b6414fad29801ee5817e5755&city={city}&state={state}".format(city=city, state=state),
        auth=HTTPBasicAuth("nickmoreno100@gmail.com", "Buddy12354!")).json()

    return zipcodes["data"]

# print(fetch_zipcodes_by_city_state("Houston", "TX"))