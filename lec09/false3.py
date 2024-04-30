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

def main():

    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&tnGroupSns =&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190 4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename = "ta_20240429021144.csv"

    download(filename,URL)


    # tmax,tmax_dates = ???
    # tdiff_max,tdiff_max_dates = ???

    #예시
    tmax,tmax_dates = 38 , "2021-08-12"
    tdiff_max,tdiff_max_dates = 28.5 , "1989-01-09"

    hw_submission.submit("홍길동",tmax,tmax_dates,tdiff_max,tdiff_max_dates)

    pass

def submit(name: str, rain_max: float, rain_max_date: str, gap_max: float, gap_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbybB2LSi0F85FkC4KmI0XgjMqvhn7-6eJjZQi0oucbgbEvwDmNVRoyMMnd5UyezpqJp/exec"
    PARAMS = {
        '제출자': name,
        '최대강수량': rain_max,
        '최대강수량날짜': rain_max_date,
        '최대일교차': gap_max,
        '최대일교차날짜': gap_max_date,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    submit("홍길동", 340.1, "2011-08-04", 25.2, "1978-01-04")
