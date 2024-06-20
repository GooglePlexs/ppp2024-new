import requests
from bs4 import BeautifulSoup
import csv
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="공모주 일정 알리미 봇입니다. /공모주 를 입력하셔서 정보를 받아보세요! ^^")

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


def storage():
    url = "https://finance.naver.com/sise/ipo.nhn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    ipo_data = []

    for tr in soup.select("table.type_7 > tbody > tr"):
        td_list = tr.select("td")

        name = td_list[0].select_one(".item_name")
        name = name.get_text(strip=True) if name else "미정"

        price = td_list[0].select_one(".area_price .num")
        price = price.get_text(strip=True) if price else "미정"

        category = td_list[0].select_one(".area_type")
        category = category.get_text(strip=True) if category else "미정"

        broker = td_list[0].select_one(".area_sup")
        broker = broker.get_text(strip=True) if broker else "미정"

        competition_rate = td_list[0].select_one(".area_competition .num")
        competition_rate = competition_rate.get_text(strip=True) if competition_rate else "미정"

        offering_period = td_list[0].select_one(".area_private .num")
        offering_period = offering_period.get_text(strip=True) if offering_period else "미정"

        listing_date = td_list[0].select_one(".area_list .num")
        listing_date = listing_date.get_text(strip=True) if listing_date else "미정"

        ipo_entry = {
            "Name": name,
            "Price": price,
            "Category": category,
            "broker": broker,
            "Competition Rate": competition_rate,
            "Offering_period": offering_period,
            "Listing Date": listing_date,
        }
        ipo_data.append(ipo_entry)

    with open("ipo_data.csv", "w", newline="") as csvfile:
        fieldnames = ["Name", "Price", "Category", "broker", "Competition Rate", "Offering_period", "Listing Date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ipo_data)

    print("Results saved to ipo_data.csv")

storage()


def handler(update, context):
    user_text = update.message.text

    if user_text == "/공모주":
        with open('ipo_data.csv', 'r') as csvfile:
            df = pd.read_csv(csvfile)

            for row in df.itertuples():
                row_text = " ".join(row[1:]) 
                context.bot.send_message(chat_id=id, text=row_text)
    else:
        context.bot.send_message(chat_id=id, text="향후 업데이트 예정입니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)