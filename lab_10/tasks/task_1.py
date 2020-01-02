import requests
from urllib.parse import urljoin
from json import JSONDecodeError

def get_cities_woeid(query: str, timeout: float = 5.):
    url = 'https://www.metaweather.com/api/'
    cities_url=urljoin(url,'location/search')
    req=requests.get(cities_url,params=dict(query=query),timeout=timeout)
    list={}
    if req.status_code>=400:
        raise req.exceptions.HTTPError
    try:
        cities=req.json()
    except JSONDecodeError:
        raise RuntimeError
    
    for city in cities:
        list[city['title']]=city['woeid']
    return list


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
