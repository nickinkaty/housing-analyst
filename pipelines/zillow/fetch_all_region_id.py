import requests, re

# ZILLOW CONFIGURATIONS
from zillow_urls import ZILLOW_REGION_ID_URL


def fetch_all_region_id(zipcodes: list):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'www.zillow.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }

    region_ids_zipcodes = []
    for zipcode in zipcodes:
        region_id_url = ZILLOW_REGION_ID_URL.format(zipcode=zipcode);
        # GET REGION ID HTML
        region_id_html_page = requests.get(region_id_url, headers=headers).text

        # FIND REGION ID IN HTML BETWEEN "cd146":" & ","cd66"
        region_id = re.search('"cd146":"(.*)","cd66"', region_id_html_page).group(1)
        region_ids_zipcodes.append([zipcode, region_id])

    return region_ids_zipcodes


zipcodes = ["77493"]

fetch_all_region_id(zipcodes)
