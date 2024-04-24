import os
import requests

URL = "https://api.taegon.kr/stations/146/?sy=2022&ey=2022&format=csv" 

filename = "lec08/weather_146_2022.csv"

if not os.path.exits(filename):  # 파일이 없으면 다운받는 코드(반복해서 긁어오는 것 방지 - 디도스 예방)
    with open(filename, "w") as f:
        res = requests.get(URL) 
        f.write(res.text)

# 파일을 내 폴더에 다운 받는 코드

#if os.path.exits(filename):  # 파일이 있으면 다운받는 코드