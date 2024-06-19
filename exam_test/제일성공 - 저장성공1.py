import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/ipo.nhn"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

ipo_data = []


for tr in soup.select("table.type_7 > tbody > tr"):

    td_list = tr.select("td")

    name = td_list[0].select_one(".item_name")
    if name:
        name = td_list[0].select_one(".item_name").get_text(strip=True)
    else : 
        name = "미정"
    
    price = td_list[0].select_one(".area_price .num")
    if price : 
        price = td_list[0].select_one(".area_price .num").get_text(strip=True)
    else :
        price = "미정"

    category = td_list[0].select_one(".area_type")
    if category : 
        category = td_list[0].select_one(".area_type").get_text(strip=True)
    else : 
        category = "미정"

    underwriter = td_list[0].select_one(".area_sup")
    if underwriter :
        underwriter = td_list[0].select_one(".area_sup").get_text(strip=True)
    else : 
        underwriter = "미정"

    competition_rate_element = td_list[0].select_one(".area_competition .num")
    if competition_rate_element:
        competition_rate = competition_rate_element.get_text(strip=True)
    else:
        copetition_rate = "미정"

    subscription_period = td_list[0].select_one(".area_private .num")
    if subscription_period :
        subscription_period = td_list[0].select_one(".area_private .num").get_text(strip=True)
    else:
        subscription_period = "미정"

    listing_date = td_list[0].select_one(".area_list .num")
    if listing_date :
        listing_date = td_list[0].select_one(".area_list .num").get_text(strip=True)
    else :
        listing_date = "미정"

    ipo_entry = {
        "Name": name,
        "Price": price,
        "Category": category,
        "Underwriter": underwriter,
        "Competition Rate": competition_rate,
        "Subscription Period": subscription_period,
        "Listing Date": listing_date,
    }
    ipo_data.append(ipo_entry)

    with open("ipo_data.csv", "w", newline="") as csvfile:
        fieldnames = ["Name", "Price", "Category", "Underwriter", "Competition Rate", "Subscription Period", "Listing Date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ipo_data)
    
    print("Results saved to ipo_data.csv")

    print(name, price, category, underwriter, competition_rate, subscription_period, listing_date)