import requests
import re
from texttable import Texttable

def depart(origroup):
    k = 0
    m = 0
    newgroup1 = []
    newgroup2 = []
    newgroup3 = []
    newgroup4 = []
    newgroup5 = []
    newgroup6 = []
    newgroup7 = []
    newgroup8 = []
    newgroup9 = []
    newgroup10 = []
    newgroup11= []
    newgroup12= []
    for match in origroup:
        if k == 5 and m == 0:
            newgroup1.append(str(match.group(1)))
            newgroup2.append(str(match.group(2)))
            newgroup3.append(str(match.group(3)))
            newgroup4.append(str(match.group(4)))
            newgroup5.append(str(match.group(5)))
            newgroup6.append(str(match.group(6)))
            newgroup7.append(str(match.group(7)))
            newgroup8.append(str(match.group(8)))
            newgroup9.append(str(match.group(9)))
            newgroup10.append(str(match.group(10)))
            newgroup11.append(str(match.group(11)))
            newgroup12.append(str(match.group(12)))
            k = 0
            m = 1
        if k == 6 and m == 1:
            newgroup1.append(str(match.group(1)))
            newgroup2.append(str(match.group(2)))
            newgroup3.append(str(match.group(3)))
            newgroup4.append(str(match.group(4)))
            newgroup5.append(str(match.group(5)))
            newgroup6.append(str(match.group(6)))
            newgroup7.append(str(match.group(7)))
            newgroup8.append(str(match.group(8)))
            newgroup9.append(str(match.group(9)))
            newgroup10.append(str(match.group(10)))
            newgroup11.append(str(match.group(11)))
            newgroup12.append(str(match.group(12)))
            k = 0
        k += 1
    return newgroup1,newgroup2,newgroup3,newgroup4,newgroup5,newgroup6,newgroup7,newgroup8,newgroup9,newgroup10,newgroup11,newgroup12


print("Start Connect")
page = requests.get("http://www.gdmo.cn/weather-gdmo/citylive/city-live!cityLiveData.action")
print("Data get,start analyse")

p = []
rf = []
t = []
ddate = []
obt = []
ctn = []
wv = []
rh =[]
maxt = []
mint = []
rain24 = []
wd = []

r='{"p":(\d*\S\d),"description":null,"rf":(\d*\S\d),"t":(\d*\S\d),"ddatetime":"(\d*-\d*-\d*\s\d*\S\d*)","obtId":"(\d{5})","cityName":"(\S\S)","lon":\d*\S\d*,"lat":\d*\S\d*,"maxMinTd":0.0,"wv":(\d*\S\d),"rh":(\d*\S\d),"maxt":(\d*\S\d),"mint":(\d*\S\d),"description2":null,"pm25":null,"rain24h":(\d*\S\d),"wd":(\d*\S\d),"imgCode":null}'

data = re.finditer(r, page.text)
print("Analysing Finish")


p, rf, t, ddate, obt, ctn, wv, rh, maxt, mint, rain24, wd = depart(data)

show=[['' for i in range(12)] for i in range(len(p)+1)]
for i in range(0,12):
    a = ["Time", "obtID", "Name", "Temp", "RH", "Pres", "WD", "WV", "rf", "rain24h", "DmaxT", "DminT"]
    show[0][i] = a[i]
for i in range(0,len(p)):
    show[i+1][0] = ddate[i]
    show[i + 1][1] = obt[i]
    show[i + 1][2] = ctn[i]
    show[i + 1][3] = t[i]
    show[i + 1][4] = rh[i]
    show[i + 1][5] = p[i]
    show[i + 1][6] = wd[i]
    show[i + 1][7] = wv[i]
    show[i + 1][8] = rf[i]
    show[i + 1][9] = rain24[i]
    show[i + 1][10] = maxt[i]
    show[i + 1][11] = mint[i]


table = Texttable()
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t','t','t','t','t','t','t','t','t','t','t','t'])
table.set_cols_width([17,5,4,5,5,6,5,5,5,7,5,5])
table.set_cols_align(['c','c','c','c','c','c','c','c','c','c','c','c'])
table.add_rows(show)
print(table.draw())
print()
print("Max Temperature in "+ctn[t.index(max(t))]+":"+str(max(t))+"dC")
print("Min Temperature in "+ctn[t.index(min(t))]+":"+str(min(t))+"dC")
print("Max Wind Speed in "+ctn[wv.index(max(wv))]+":"+str(max(wv))+"m/s")