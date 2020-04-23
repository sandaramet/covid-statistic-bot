

from bot.handler import HelpCommandHandler, UnknownCommandHandler, MessageHandler, FeedbackCommandHandler, \
    CommandHandler, NewChatMembersHandler, LeftChatMembersHandler, PinnedMessageHandler, UnPinnedMessageHandler, \
    EditedMessageHandler, DeletedMessageHandler, StartCommandHandler, BotButtonCommandHandler
from bot.bot import Bot
import covid
from datetime import date
from flask import Flask,request
import json
import os
TOKEN = "001.1635373522.2043998669:752127871"
bot = Bot(token=TOKEN)
today = str(date.today())
server = Flask(__name__)

def favorites(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Текущая статистика по коронавирусу на " + today, inline_keyboard_markup="{}".format(json.dumps([[
        {"text": "Во всем мире",
         "callbackData": "allWorld",
         "style": "primary"},
        {"text": "Россия",
         "callbackData": "russia",
         "style": "primary"},
        {"text": "Украина",
         "callbackData": "ukraine",
         "style": "primary"},
        {"text": "Беларусь",
         "callbackData": "belarus",
         "style": "primary"}
    ]])))


def start_cb(bot, event):
    bot.send_text(
        chat_id=event.data['chat']['chatId'],
        text="Привет " + event.data['from']['firstName'] + "! Чтобы узнать данные про коронавируса напишите название страны, например: America, Belarus, Russia и так далее․ \nЕсли вы хотите увидеть список стран, напишите /countries")
    favorites(bot, event)


def buttons_answer_cb(bot, event):
    if event.data['callbackData'] == "allWorld":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=covid.location("getAllCountries"),
            show_alert=True
        )

    elif event.data['callbackData'] == "russia":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=covid.location("russia"),
            show_alert=True
        )
    elif event.data['callbackData'] == "ukraine":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=covid.location("ukraine"),
            show_alert=True
        )
    elif event.data['callbackData'] == "belarus":
        bot.answer_callback_query(
            query_id=event.data['queryId'],
            text=covid.location("belarus"),
            show_alert=True
        )


def message_cb(bot, event):
    if (event.text == "/countries"):
        bot.send_text(chat_id=event.from_chat, text=covid.getAllCountries())
        favorites(bot, event)
    elif (event.text == "/favorites"):
        favorites(bot, event)
    elif (event.text != "/start"):
        bot.send_text(chat_id=event.from_chat, text=covid.location(event.text))


bot.dispatcher.add_handler(StartCommandHandler(callback=start_cb))
bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))
bot.start_polling()
bot.idle()

if __name__ == "__main__":
    server.run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))