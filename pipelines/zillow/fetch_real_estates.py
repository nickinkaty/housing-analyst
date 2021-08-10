import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'www.zillow.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
}


# https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":2},"usersSearchTerm":"77388","mapBounds":{"west":-95.525514,"east":-95.429085,"south":30.024531,"north":30.085588},"regionSelection":[{"regionId":91898,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2
# {"usersSearchTerm":"77388","mapBounds":{"west":-95.67814331103516,"east":-95.27645568896484,"south":30.015682532307267,"north":30.094430223351907},"regionSelection":[{"regionId":91898,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true,"mapZoom":12}

# https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":2},"usersSearchTerm":"77493","mapBounds":{"west":-95.907893,"east":-95.773356,"south":29.785206,"north":29.950635},"regionSelection":[{"regionId":91981,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2
# {"pagination":{"currentPage":2},"usersSearchTerm":"77493","mapBounds":{"west":-95.907893,"east":-95.773356,"south":29.785206,"north":29.950635},"regionSelection":[{"regionId":91981,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}

# r = requests.get('https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":2},"usersSearchTerm":"77493","mapBounds":{"west":-95.907893,"east":-95.773356,"south":29.785206,"north":29.950635},"regionSelection":[{"regionId":91981,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2', headers=headers)
# print(r.text)

# def clean_json(json: str):


def fetch_real_estates(region_id: str):
    r = requests.get('https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":2},"usersSearchTerm":"77493","mapBounds":{"west":-95.907893,"east":-95.773356,"south":29.785206,"north":29.950635},"regionSelection":[{"regionId":91981,"regionType":7}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2', headers=headers).json()
    real_estate_results = r["cat1"]["searchResults"]["listResults"]


fetch_real_estates("1")