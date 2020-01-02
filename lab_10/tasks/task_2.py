import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
from json import JSONDecodeError
import calendar
import csv
from tqdm.auto import tqdm


API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    
    days=calendar.monthrange(year,month)[1]
    
    if path is None:
        path=pathlib.Path.cwd()
    else:
        path=pathlib.Path(path)
    path /= f'{woeid}_{year}_{month:02d}'
    path.mkdir(parents=True, exist_ok=True)
    new_files=[]
    for day in tqdm(range(1,days+1)):
        file_name=f'{year}_{month:02d}_{day:02d}.csv'
        data=get_data(woeid,year,month,day,timeout)
        if data:
            with open(path / file_name,'w') as _file:
                writer=csv.DictWriter(_file,delimiter=',',fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            new_files.append(file_name)
    return str(path), new_files

def get_data(woeid,year,month,day,timeout):
    cities_url=urljoin(API_URL,f'location/{woeid}/{year}/{month}/{day}')
    data=None
    req=requests.get(cities_url,timeout=timeout)
    if req.status_code>=400:
        raise req.exceptions.HTTPError
    try:
        data=req.json()
    except JSONDecodeError:
        raise RuntimeError
    return data

if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)

    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = r'weather_data\523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()

    assert expected_path == dir_path 

    expected_path = r'weather_data\523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()

    assert expected_path == dir_path
