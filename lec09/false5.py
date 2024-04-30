import sys
if "./" not in sys.path: 
  sys.path.append("./")

from lec09 import hw_submission

import os

import requests

def download(filename,URL):
  
  URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
  filename = "jeonju_all.csv"

  if not os.path.exists(filename): 
    with open(filename, "w") as f:
      res = requests.get(URL) 
      f.write(res.text)

def read_col(filename, col_idx):

  results = []
  with open(filename) as f:
    lines = f.readlines()
    for line in lines[1:]:
      tokens = line.split(",")
      results.append(float(tokens[col_idx]))

  return results


      

def main():
  
  URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
  filename = "jeonju_all.csv"

  download(filename,URL)


  if not os.path.exists(filename):  
        with open(filename, "w") as f:
           res = requests.get(URL) 
           f.write(res.text)
    
  cal = read_col("lec09/ta_20240429021144.csv", 0)
  region = read_col("lec09/ta_20240429021144.csv", 1)
  tavg = read_col("lec09/ta_20240429021144.csv", 2)
  tmin = read_col("lec09/ta_20240429021144.csv", 3)
  tmax = read_col("lec09/ta_20240429021144.csv", 4)


  # 최대 강수량 날짜 찾기
  rain_max = -float('inf')
  rain_max_date = None
  for date, tmin, tavg, tmax in results:
    if tmax > rain_max:
      rain_max = tmax
      rain_max_date = date

  # 최대 일교차 날짜 찾기
  tdiff_max = -float('inf')
  tdiff_max_date = None
  for date, tmin, tavg, tmax in results:
    tdiff = tmax - tmin
    if tdiff > tdiff_max:
      tdiff_max = tdiff
  tdiff_max_date = date

  # 결과 출력
  print(f"최대 강수량: {rain_max}℃ ({rain_max_date})")
  print(f"최대 일교차: {tdiff_max}℃ ({tdiff_max_date})")

  # 제출 (본인 이름, 최대 강수량, 최대 강수량 날짜, 최대 일교차, 최대 일교차 날짜)
  hw_submission.submit("홍길동", rain_max, rain_max_date, tdiff_max, tdiff_max_date)

if __name__ == "__main__":
  main()
