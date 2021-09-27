import sys
import requests

sys.path.append('/opt/airflow')
from zillow.scripts_functions.request_parameters import header, proxies


def request_proxy_tries(request_type: str, url: str, tries=20):
    for i in range(tries):
        try:
            if request_type == "GET":
                request = requests.get(url, headers=header, proxies=proxies)

            if "captcha" in request.text:
                raise Exception("Captcha Found!")

        except Exception as e:
            # print(e)
            if i <= tries:  # i is zero indexed
                continue
            else:
                raise SystemExit(e)
        except requests.exceptions.ProxyError as e:
            # print("Tries: ", i)
            if i <= tries:  # i is zero indexed
                continue
            else:
                raise SystemExit(e)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        break

    return request
