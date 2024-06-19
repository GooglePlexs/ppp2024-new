import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import pandas as pd

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="공모주 일정 알리미 봇입니다. 공모주 를 입력하셔서 정보를 받아보세요!^^")

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text

    if user_text == "공모주":
        # CSV 파일 읽기
        with open('ipo_data.csv', 'r') as csvfile:
            # CSV 파일을 DataFrame으로 변환
            df = pd.read_csv(csvfile)

            # 각 행을 메시지로 보내기
            for row in df.itertuples():
                row_text = " ".join(row[1:])  # 각 행의 요소를 공백으로 연결
                context.bot.send_message(chat_id=id, text=row_text)
    else:
        context.bot.send_message(chat_id=id, text="향후 업데이트 예정입니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
