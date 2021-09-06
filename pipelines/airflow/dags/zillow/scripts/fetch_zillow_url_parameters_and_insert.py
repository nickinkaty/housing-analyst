import json, requests, re, os


def fetch_zillow_url_parameters_and_insert(zipcodes: list):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'www.zillow.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    }

    proxies = {
        "http": os.environ["PROXY_HTTP"],
        "https": os.environ["PROXY_HTTPS"]
    }

    print(proxies)

    # airflow tasks test zillow_pipeline fetch_all_region_id 2021-08-14

    zillow_url_parameters = []
    for zipcode in zipcodes:
        region_id_url = 'https://www.zillow.com/homes/{zipcode}_rb/'.format(zipcode=zipcode)

        # GET REGION ID HTML
        region_id_html_page = requests.get(region_id_url, headers=headers, proxies=proxies).text

        # FIND REGION ID IN HTML BETWEEN "cd146":" & ","cd66"
        region_id = re.search('"cd146":"(.*)","cd66"', region_id_html_page)

        # IF NOT FOUND THROW ERROR
        if region_id:
            region_id = region_id.group(1)
        else:
            raise Exception("ERROR: REGION ID IS NOT FOUND")

        zillow_url_parameters.append({"zipcode": int(zipcode), "region_id": int(region_id)})

    print("{API_BASE_URL}zillowUrlParameters".format(API_BASE_URL=os.environ["API_BASE_URL"]), json.dumps(zillow_url_parameters))

    # try:
    headers = {'content-type': 'application/json'}
    zillowUrlParametersAPI = "{API_BASE_URL}zillowUrlParameters".format(API_BASE_URL=os.environ["API_BASE_URL"])
    print(zillowUrlParametersAPI)
    # print(zillowUrlParametersAPI)
    requests.post("http://172.18.0.6:5000/api/v1/zillowUrlParameters", data=json.dumps(zillow_url_parameters), headers=headers)
    # except requests.exceptions.ConnectionError:
    #     requests.status_code = "Connection refused"

    return zillow_url_parameters


zipcodes = ["77001", "77493"]

fetch_zillow_url_parameters_and_insert(zipcodes)
