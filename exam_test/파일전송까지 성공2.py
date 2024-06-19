import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd  # CSV 파일 처리를 위한 라이브러리 추가

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
        # CSV 파일 읽기
        with open('ipo_results.csv', 'r') as csv_file:
            csv_text = csv_file.read() 
            # 채팅 ID 가져오기
            chat_id = update.message.chat_id
            # CSV 파일 텍스트 보내기
            context.bot.send_message(chat_id, text=csv_text)
    else:
        context.bot.send_message(chat_id=id, text="향후 업데이트 예정입니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
