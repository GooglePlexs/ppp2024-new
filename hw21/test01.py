import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = "7258921748:AAE5WbsngK62vocaeJHT4989kvNt8agcdPw"
id = "7440605409"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파운드와 킬로그램 변환 봇입니다. 사용 방법은 /도움말을 입력하세요.")


updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


def pound_to_kg(pound):
    kg = pound * 2.20462
    return kg


def kg_to_pound(kg):
    pound = kg * 0.453592
    return pound


def handler(update, context):
    user_text = update.message.text.lower()  

    if user_text == "/도움말":
        help_message = "파운드와 킬로그램 변환 봇입니다.\n\n사용 방법:\n* `숫자 파운드` 또는 `숫자 kg` 입력하면 변환 결과를 알려드립니다.\n* `/도움말` 입력하면 이 도움말 메시지를 보여드립니다."
        bot.send_message(chat_id=id, text=help_message)
        return

    try:
        
        value = float(user_text.split()[0])

        
        if user_text.endswith("kg"):
            converted_value = pound_to_kg(value)
            unit = "파운드"
        elif user_text.endswith("lb") or user_text.endswith("파운드"):
            converted_value = kg_to_pound(value)
            unit = "킬로그램"
        else:
            raise ValueError

        
        result_message = f"{value:.2f} {user_text.split()[1]}는 {converted_value:.2f} {unit}입니다."
        bot.send_message(chat_id=id, text=result_message)
    except ValueError:
        bot.send_message(chat_id=id, text="올바른 숫자와 단위를 입력하세요. (예: 10 kg, 5 lb)")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)