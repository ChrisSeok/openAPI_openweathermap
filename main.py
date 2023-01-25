import requests
from bs4 import BeautifulSoup as bs
import json
import datetime
import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4) #makes print easier to see 

serviceKey = '6658714550666c6f33324255415266'
dtype = 'json'
url = 'http://openapi.seoul.go.kr:8088/sample/json/GeoInfoWinterAvrgTemp/1/5/'
res=requests.get(url)
items = res.json()
# print(pp.pprint(items))
nesdata = items['GeoInfoWinterAvrgTemp']['row']
df = pd.DataFrame(nesdata)
df.to_csv('data.csv', index=False)






