import csv
import requests
import os

import sys
if "./" not in sys.path: 
    sys.path.append("./")

from lec09 import hw_submission

def download(filename,URL):
   
   URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=" 
   
   filename = "lec09/jeonju_all.csv"

   if not os.path.exists(filename):  
      with open(filename, "w") as f:
        res = requests.get(URL) 
        f.write(res.text)

# 1번
f = open('lec09/jeonju_weather.csv')
datas = csv.reader(f)
header = next(datas)

max_temp = -999
max_date = ''

for data in datas:
    if data[4] == '':
        data[4] = -999
    data[4] = float(data[4])

    if max_temp < data[4]:
        max_date = data[0]
        max_temp = data[4]


f = open('lec09/jeonju_weather.csv')
lists=csv.reader(f)
header=next(lists)

max_temps = -999
min_temps = ''
day_temps = -999
max_dates = ''
day_dates = ''
for list in lists :
    if list[2] == '':
      list[2] = 0
    if list[3] == '':
      list[3] = 0
    if list[4] == '':
      list[4] = -999

    list[2] = float(list[2])
    list[3] = float(list[3])
    list[4] = float(list[4])

    if(list[4] - list[3]) > day_temps:
      day_temps = (list[4] - list[3])
      max_temps = list[4]
      min_temps = list[3]
      day_dates = list[0]

def main():
   URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
   filename = "jeonju_all.csv"
   download(filename,URL)

   hw_submission.submit("박성민",max_temp,max_dates,day_temps,day_dates)

if __name__ == "__main__":
    main()

   



