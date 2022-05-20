# Telegram Bot
# by Master PC

# 匯入相關套件/Importing the modules
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
import logging

from telegram import (
    KeyboardButton,
    KeyboardButtonPollType,
    Poll,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)

from telegram.ext import (
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PollAnswerHandler,
    PollHandler,
    filters,
)

import requests
import json

# 設定 token / setting up the token
token = '5215799092:AAFQHymHjUKgY7_9Nt0De5zR-xzh1ecXyjg'

# 初始化bot / Initializing the bot
updater = Updater(token=token, use_context=False)

# 設定一個dispatcher(調度器) / Setting a dispatcher
dispatcher = updater.dispatcher

# 定義收到訊息後的動作(新增handler) / Add a handler for each action done.
def start(bot, update): # 新增指令/start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI  ' + str(chat['id']))    

dispatcher.add_handler(CommandHandler('start', start))

# 開始運作bot / Start the bot
updater.start_polling()



# 發指定對象訊息 / Setting up personal details
who = '5185744693'
welcomeMsg1 = 'Prism Dragon Bot at your Service!'
dispatcher.bot.send_photo(chat_id=who, photo="https://d2dcan0armyq93.cloudfront.net/photo/odai/600/ca56bcfd04dd2a75e09c441ab2336d39_600.jpg")
dispatcher.bot.send_message(chat_id=who, text=welcomeMsg1) # 發送訊息 / Sending the message.

markUp=InlineKeyboardMarkup([[
    InlineKeyboardButton('Company Address', url="https://www.google.com/maps/place/%E5%85%83%E7%9B%9B%E7%94%9F%E5%8C%BB%E9%9B%BB%E5%AD%90/@25.0523529,121.533905,17z/data=!3m2!4b1!5s0x3442abdfe7352309:0xe33ddf8b12d35b98!4m5!3m4!1s0x3442a96f0c9f0407:0x55fbb0e4af2cb0e9!8m2!3d25.0523529!4d121.536099"),
    InlineKeyboardButton('你的網路生活教授Nash', url="https://pixnashlife.pixnet.net/blog"),
    InlineKeyboardButton('恩哥Python量化教室', url="https://pixnashpython.pixnet.net/blog"),
    InlineKeyboardButton('Bot Tutorial 1', url="https://www.youtube.com/watch?v=AHYh5eL2oQw&t=347s&ab_channel=Gunther"),
    InlineKeyboardButton('Bot Tutorial 2', url="https://www.youtube.com/watch?v=HXVi2zT7l_c&ab_channel=Gunther"),
    InlineKeyboardButton('Geeks for Geeks', url="https://www.geeksforgeeks.org/python-programming-language/")
]])

dispatcher.bot.send_message(chat_id=who, text="""
How may I help you?

Enter the following commands:
- /poll for poll
- [More coming soon.]

""", reply_markup=markUp)


################# FUNCTIONS #########################
def echo(bot, update): # 其他訊息 / Other Messages
    message = update.message
    text = message.text + "  <<< I don't understand what you are saying :/"
    update.message.reply_text(text=text)
    update.message.reply_photo(photo="https://pbs.twimg.com/profile_images/924511616355282944/eTE8S6cS_400x400.jpg")


def poll(bot, update):
    base_url = "https://api.telegram.org/bot5215799092:AAFQHymHjUKgY7_9Nt0De5zR-xzh1ecXyjg/sendPoll"
    pollParams = {
        "chat_id" : who,
        "question" : "Are you investing in Bitcoin or Dogecoin?",
        "options" : json.dumps(["Bitcoin", "Ethereum"])
    }

    resp = requests.get(base_url, data = pollParams)
    print(resp.text)
################# HANDLERS ########################

dispatcher.add_handler(CommandHandler('poll', poll))
dispatcher.add_handler(MessageHandler(Filters.text, echo)) # Filters如果是文字就呼叫start

# 待命 若要停止按Ctrl-C 就好
#updater.idle()


# 離開
#updater.stop()