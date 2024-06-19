import telegram
from telegram.ext import Updater, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=chat_id, text="테스트 중입니다.")

def ipo():
    """Extracts and returns IPO data from Naver Finance website."""
    url = "https://finance.naver.com/sise/ipo.nhn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []
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

        data.append({
            "name": name,
            "price": price,
            "category": category,
            "underwriter": underwriter,
            "competition_rate": competition_rate,
            "subscription_period": subscription_period,
            "listing_date": listing_date
        })

    return data

def handler(update, context):
    user_text = update.message.text

    if user_text == "공모주":
        ipo_data = ipo()
        formatted_data = "\n".join([f"{entry['name']} | {entry['price']} | {entry['category']} | {entry['underwriter']} | {entry['competition_rate']} | {entry['subscription_period']} | {entry['listing_date']}" for entry in ipo_data])
        bot.send_message(chat_id=chat_id, text=formatted_data)
    else:
        bot.send_message(chat_id=chat_id, text="업데이트 예정입니다.")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
updater.start_polling()
