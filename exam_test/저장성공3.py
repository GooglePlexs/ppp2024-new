import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/ipo.nhn"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create a CSV file with headers
with open("ipo_file.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Company Name", "Price", "Category", "Underwriter",
                     "Competition Rate", "Subscription Period", "Listing Date"])

    # Extract and write data to CSV
    for tr in soup.select("table.type_7 > tbody > tr"):
        td_list = tr.select("td")

        name = td_list[0].select_one(".item_name")
        name = name.get_text(strip=True) if name else "미정"

        price = td_list[0].select_one(".area_price .num")
        price = price.get_text(strip=True) if price else "미정"

        category = td_list[0].select_one(".area_type")
        category = category.get_text(strip=True) if category else "미정"

        underwriter = td_list[0].select_one(".area_sup")
        underwriter = underwriter.get_text(strip=True) if underwriter else "미정"

        competition_rate_element = td_list[0].select_one(".area_competition .num")
        competition_rate = competition_rate_element.get_text(strip=True) if competition_rate_element else "미정"

        subscription_period = td_list[0].select_one(".area_private .num")
        subscription_period = subscription_period.get_text(strip=True) if subscription_period else "미정"

        listing_date = td_list[0].select_one(".area_list .num")
        listing_date = listing_date.get_text(strip=True) if listing_date else "미정"

        writer.writerow([name, price, category, underwriter, competition_rate, subscription_period, listing_date])

print("IPO data saved to ipo_file.csv")
