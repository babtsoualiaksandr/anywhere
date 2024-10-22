from django.core.management.base import BaseCommand
from django.conf import settings

import telebot
from telebot import types
from telebot.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import random
from random import choice
import os
from bot.management.commands import menu

print("Bot TLG Start...")
bot = telebot.TeleBot(settings.BOT_TOKEN)
print("Bot TLG Start...")
bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("command1", "command1 description"),
        telebot.types.BotCommand("command2", "command2 description")
    ],
)
WEB_URL = "https://pytelegrambotminiapp.vercel.app" 

@bot.message_handler(commands=["start"])
def start(message):
    reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard_markup.row(KeyboardButton("Start MiniApp", web_app=WebAppInfo(WEB_URL)))

    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(InlineKeyboardButton('Start MiniApp', web_app=WebAppInfo(WEB_URL)))

    bot.reply_to(message, "Click the bottom inline button to start MiniApp", reply_markup=inline_keyboard_markup)
    bot.reply_to(message, "Click keyboard button to start MiniApp", reply_markup=reply_keyboard_markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    bot.reply_to(message, f'Your message is "{message.web_app_data.data}"')

class Command(BaseCommand):
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков 
        bot.infinity_polling()