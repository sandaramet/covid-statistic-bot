
from bot.handler import HelpCommandHandler, UnknownCommandHandler, MessageHandler, FeedbackCommandHandler, \
    CommandHandler, NewChatMembersHandler, LeftChatMembersHandler, PinnedMessageHandler, UnPinnedMessageHandler, \
    EditedMessageHandler, DeletedMessageHandler, StartCommandHandler, BotButtonCommandHandler
from bot.bot import Bot
import covid
from datetime import date
import json
import os
from functions import dotEveryThreeNumber, haveWord
TOKEN = ""
bot = Bot(token=TOKEN)
today = str(date.today())


def favorites(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Текущая статистика по коронавирусу на " + today, inline_keyboard_markup="{}".format(json.dumps([[
        {"text": "Во всем мире",
         "callbackData": "allWorld",
         "style": "primary"},
        {"text": "Россия",
         "callbackData": "Russia",
         "style": "primary"},
        {"text": "Украина",
         "callbackData": "Ukraine",
         "style": "primary"},
        {"text": "Беларусь",
         "callbackData": "Belarus",
         "style": "primary"}
    ]])))


def callbackData(bot, event):
    bot.answer_callback_query(
        query_id=event.data['queryId'],
        text=covid.location(event.data['callbackData']),
        show_alert=True
    )


def start_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Привет " + event.data['from']['firstName'] + "! Чтобы узнать данные про коронавируса напишите название страны, например: America, Belarus, Russia и так далее․ \nЕсли вы хотите увидеть список стран, напишите /worldwide\nЕсли вы хотите увидеть топ, напишите top- и номер: например top-10")
    favorites(bot, event)


def buttons_answer_cb(bot, event):
    if event.data['callbackData'] == "allWorld":
        callbackData(bot, event)
    elif event.data['callbackData'] == "Russia":
        callbackData(bot, event)
    elif event.data['callbackData'] == "Ukraine":
        callbackData(bot, event)
    elif event.data['callbackData'] == "Belarus":
        callbackData(bot, event)


def message_cb(bot, event):
    if (event.text == "/worldwide"):
        bot.send_text(chat_id=event.from_chat, text=covid.getAllCountries())
        favorites(bot,  event)
    elif (haveWord(event.text, "top")):
        favorites(bot,  event)
        bot.send_text(chat_id=event.from_chat,
                      text=covid.getTopNumber(event.text))
    elif (event.text != "/start"):
        bot.send_text(chat_id=event.from_chat, text=covid.location(event.text))
    elif (event.text == "/start"):
        data = event.data['from'] 
        with open('users.txt', 'a') as outfile:
             json.dump( data, outfile)
   


bot.dispatcher.add_handler(StartCommandHandler(callback=start_cb))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))
bot.start_polling()
bot.idle()
