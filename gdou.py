import requests
from bs4 import BeautifulSoup
import re


print("Start Connect")
page = requests.get("http://www.gdmo.cn/weather-gdmo/citylive/city-live!cityLiveData.action")
print("Data get,start analyse")

t = re.search('"t":(\d\d\S\d),"ddatetime":"', page.text)
print("Analysing Finish")
print(t.group(1))

