import filecmp
import pathlib
from typing import Union
import datetime
from dateutil.parser import parse

import pandas as pd


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    if not isinstance(path,pathlib.Path):
        path=pathlib.Path(path)
    data_list=[]
    for file in path.iterdir():
        data=pd.read_csv(file)
        check_day=pd.to_datetime(data['created']).dt.date==pd.to_datetime(data['applicable_date']).dt.date
        data_list.append(data[check_day])
    data_list=pd.concat(data_list)
    save=pd.DataFrame(data_list, columns=['created','min_temp','the_temp','max_temp','air_pressure','humidity','visibility','wind_direction_compass','wind_direction','wind_speed'])
    save.rename({'the_temp':'temp'},inplace=True,axis='columns')
    save['created']=save['created'].apply(lambda x: x[:16])
    save.sort_values('created',inplace=True)
    save.to_csv(f'{path}.csv',index=False)

if __name__ == '__main__':
    concat_data(r'weather_data\523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        r'weather_data\523920_2017_03.csv'
    )
