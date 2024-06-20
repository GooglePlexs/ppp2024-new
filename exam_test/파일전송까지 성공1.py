import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd  

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="테스트 중입니다.")

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "공모주":
        # Open the CSV file
        with open('ipo_results.csv', 'rb') as csv_file:
            # Get the chat ID
            chat_id = update.message.chat_id
            # Send the CSV file
            context.bot.send_document(chat_id, document=csv_file)
    else:
        context.bot.send_message(chat_id=id, text="향후 업데이트 예정입니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)