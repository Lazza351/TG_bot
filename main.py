from telebot.async_telebot import AsyncTeleBot
from telebot import types
bot = AsyncTeleBot('6147456112:AAERBvts7QYb9Fzy1u1vSpzPYGJC5IdQ7gk')

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):

    await bot.send_message( message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=webAppKeyboard()) 

    
def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppTest = types.WebAppInfo("https://lazza351.github.io/TG_bot/") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard



import asyncio
asyncio.run(bot.polling())