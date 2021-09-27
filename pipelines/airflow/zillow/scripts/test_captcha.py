import json
import re
import sys
import requests

from twocaptcha import TwoCaptcha

solver = TwoCaptcha('18ca610038ebf491e8064ce25cb8d650')

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'www.zillow.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
}

request_session = requests.Session()
captcha_html = request_session.get("https://www.zillow.com/captcha/", headers=header).text
site_key = re.search('class="g-recaptcha" data-sitekey="(.*)"></div><br/><input id="dest"', captcha_html).group(1)


try:
    result = solver.recaptcha(
        sitekey=site_key,
        url='https://www.zillow.com/captcha',
        invisible=1)

except Exception as e:
    sys.exit(e)

# else:
#     sys.exit('solved: ' + str(result))

print(result["code"])

try:
    content = request_session.post(
        'https://www.zillow.com/captcha',
        data={
            'g-recaptcha-response': result["code"],
            'dest': "ognl:originalDestination",
            'norecaptcha': "false",
        },
        headers=header
    )
except ConnectionError as e: # Handle fundamental connectivity issues
    # Handle your error state
    print(e)

# Will throw ValueError if we can't parse Google's response
print(content.text)

# if not 'success' in content or not content['success']:
    # The reCaptcha hasn't passed...