import requests

# INSERT REAL ESTATE JSON TO DB REST API
def insert_real_estate_data(real_estates_json):
    r = requests.post('http://localhost:5000/api/v1/realestates', json=real_estates_json)
    print(r.text)