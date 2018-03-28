import requests
import re

input("Press Enter to start check realtime temperature in Guangdong.")

print("Start Connect")
page = requests.get("http://www.gdmo.cn/weather-gdmo/citylive/city-live!cityLiveData.action")
print("Data get,start analyse")

templist = []
citylist = []
temp = re.finditer('"t":(\d\d\S\d),"ddatetime":"', page.text)
cityname = re.finditer('"cityName":"(\S\S)","lon"', page.text)
print("Analysing Finish")
k=0
m=0
for match in cityname:
    if k==5 and m==0:
        citylist.append(str(match.group(1)))
    if k==10 and m==0:
        citylist.append(str(match.group(1)))
        k=0
        m=1
    if k==6 and m==1:
        citylist.append(str(match.group(1)))
        k=0
    k+=1
k=0
m=0
for match in temp:
    if k==5 and m==0:
        templist.append(str(match.group(1)))
    if k==10 and m==0:
        templist.append(str(match.group(1)))
        k=0
        m=1
    if k==6 and m==1:
        templist.append(str(match.group(1)))
        k=0
    k+=1

for i in range(0,85):
    print(citylist[i]+":"+str(templist[i]))

input()
