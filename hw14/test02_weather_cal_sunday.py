import csv
import requests
import os

import sys
if "./" not in sys.path: 
    sys.path.append("./")

from lec09 import hw_submission


def download(filename,URL):
   
   URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=" 
   
   filename = "hw14/jeonju_all.csv"

   if not os.path.exists(filename):  
      with open(filename, "w") as f:
        res = requests.get(URL) 
        f.write(res.text)


def temp_dictionary(filename):

  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    highest_temp = -999  
    highest_temp_date = ''
    largest_temp_diff = -999
    largest_temp_diff_date = ''

    for data in reader:
      
      if data[2] == '':
        data[2] = 0
      if data[3] == '':
        data[3] = 0
      if data[4] == '':
        data[4] = -999
      
      data[2] = float(data[2])  
      data[3] = float(data[3])  
      data[4] = float(data[4])  

      #최고기온과 날짜
      if data[4] > highest_temp:
        highest_temp = data[4]
        highest_temp_date = data[0]

      temp_diff = data[4] - data[2]
      
      #최대기온차이와 날짜
      if temp_diff > largest_temp_diff:
        largest_temp_diff = temp_diff
        largest_temp_diff_date = data[0]

  return {
      'highest_temp': highest_temp,
      'highest_temp_date': highest_temp_date,
      'largest_temp_diff': largest_temp_diff,
      'largest_temp_diff_date': largest_temp_diff_date
  }


def main():
   URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
   filename = "jeonju_all.csv"
   download(filename,URL)

   weather_data = temp_dictionary('hw14/jeonju_weather.csv')

   hw_submission.submit("박성민",weather_data['highest_temp'],weather_data['highest_temp_date'],weather_data['largest_temp_diff'],weather_data['largest_temp_diff_date'])

if __name__ == "__main__":
    main()


