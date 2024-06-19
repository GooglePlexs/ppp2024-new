import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import csv

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)

# Function to send CSV data as Telegram message
def send_csv_data(chat_id, csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            message_text = ', '.join(row)  # Construct message text from row data
            bot.send_message(chat_id=chat_id, text=message_text)

# Updater and dispatcher
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# Handler for '/공모주' command
def handler(update, context):
    user_text = update.message.text
    if user_text == "/공모주":
        bot.send_message(chat_id=id, csv_file_path="ipo_result.csv")  
    else:
        bot.send_message(chat_id=id, text="향후 업데이트 예정입니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

# Start polling
updater.start_polling()
