import requests

URL = "https://coopjbnu.kr/menu/week_menu.php" 

data = { "code": "mobile1" }

with open("./cafeteria_menu_week.html", "w", encoding="UTF-8") as f: # .은 해당폴더, ..은 상위폴더 / W = write / encoding="UTF-8" - 한글깨짐방지
    res = requests.get(URL) # requests의 get 기능 사용
    res.encoding = "UTF-8" 
    f.write(res.text)
