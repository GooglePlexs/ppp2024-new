from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.jbnu.ac.kr/kor/?menuID=139"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text , 'html.parser')
    
    # print("resp.text")
    # print(soup.prettify())
    # print(soup.find("type06_headline"))
    # print(soup.table.find_all("td","left"))

    for idx, news_item in enumerate(soup.table.find_all("td","left")):
        print(f'{idx+1} - {news_item.a["title"]}')


if __name__ == "__main__":
    main()