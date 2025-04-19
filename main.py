import telebot
from telebot.types import Message
import random

bot = telebot.TeleBot("7684396044:AAFq2SKNGfQieFXCWWUM8TOX7t3FR252UBU")

@bot.message_handler(commands=['start'])
def start_cmd(message: Message):
    bot.send_message(message.chat.id, "Привет! Я тестовый бот:)")

@bot.message_handler(commands=['coin'])
def coin_cmd(message: Message):
    x = random.randint(0, 1)
    if x == 0:
        bot.send_message(message.chat.id, "Вам выпал орел!")
    else:
        bot.send_message(message.chat.id, "Вам выпала решка!")

@bot.message_handler(commands=['about'])
def about_cmd(message: Message):
    bot.reply_to(message, "Тут я!")

@bot.message_handler(commands=['help'])
def help_cmd(message: Message):
    text = "<b>Мои команды:</b>\n /start - <i>запуск бота</i>\n /coin - <i>монетка</i>\n /help - <i>о командах</i>"
    bot.send_message(message.chat.id, text, parse_mode='html')

@bot.message_handler(commands=['knb'])
def knb_cmd(message: Message):
    bot.send_message(message.chat.id, "Игра запустилась, напишите камень/ножницы/бумага или отмена (чтобы отменить игру)")
    bot.register_next_step_handler(message, knb_game)

def knb_game(message: Message):
  text = message.text.flower
  if text == "отмена":
    bot.send_message(message.chat.id, "Игра остановлена, вам снова доступны все команды")
    return
  
  if text not in ["камень", "ножницы", "бумага"]:
    bot.send_message(message.chat.id, "Вы написали что-то не то, игра остановлена, вам снова доступны все команды!")
    return
  comp=random. choice(['камень', 'ножницы", "бумага'])
  if text == comp:
    bot.send_message(message.chat.id, "Ничья, если хотите поиграть снова, напишите /knb")
    return
  elif (text == 'камень' and bot == 'ножницы') or (text == 'ножницы', and bot == 'бумага') or (text == 'бумага' and bot == 'камень')
    bot.send_message(message.chat.id, "Вы победили, если хотите поиграть снова, напишите /knb")
  else:
    return
    bot.send_message(message.chat.id, "Вы проиграли, если хотите поиграть снова, напишите /knb")
    return
@bot.message_handler(func_lamba message: message.text == 'привет')
def hello_text(message: Message):
  bot.send_message(message.chat.id, "и тебе привет!")
  
bot.infinity_polling()
