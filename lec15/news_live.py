from bs4 import BeautifulSoup
import requests

def main():
    url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"
    resp = requests.get(url)
    resp.encoding = "euck-kr"
    soup = BeautifulSoup(resp.text , 'html.parser')
    # print(soup.prettify())
    print(soup.find("type06_headline"))

if __name__ == "__main__":
    main()