# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:34:49 2022

@author: msii
"""
 
from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "5553622461:AAGrIDTaD1pxNzefDIYcirRyW5BVWPMLYpA"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu aleykum, Xush kelibsiz!"
    answer += "\nMatn kiriting: "
    bot.reply_to(message, answer)
    
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        msg = message.text
        answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
        bot.reply_to(message, answer(msg))

bot.polling()

#matn = input("Biror bir matin kiriting: ")

#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
 #    print(to_latin(matn))     