from aiogram import types, Dispatcher
from aiogram.dispatcher.dispatcher import Dispatcher
from create_bot import bot 
from data_base import sqlite_db
from keyboards import client_kb

# @dp.message_handler(commands=['start'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hush kelibsiz\nSizga qanday yordam beraolamiz?', reply_markup= client_kb.kb_client)
        await message.delete()
    except:
        await message.reply('Go to LC:\nhttps://t.me/quva_qandolat_bot')


async def about(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,"""Eduon Onlayn Ta'lim platformasi \nU yerda ta'limga, IT, Biznesga yo'naltirilgan video-kurslar mavjud\nEduon O;zbekistondagi ilk onlayn talim platfomrasi,\n@MFaktoruz tomonidan tashkil etilgan loyixa,\n4000+ foydalanuvchiga ega!\nEduonga Xush Kelibsiz""")
        await message.delete()
    except:
        await message.reply('Kechirasiz Xatolik yuz berdi!\nBotni o`ziga(Lichkasiga)yozib ko`ring:\nhttps://t.me/quva_qandolat_bot\nYoki Dasturchi bilan bog`laning:\nhttps://t.me/The_7oo7')



async def location(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=40.511826, longitude=72.071399, reply_markup=client_kb.kb_client)
    await message.delete()


# @dp.message_handler(commands=['maxsulotlar'])
async def products(message: types.Message):
    await sqlite_db.sql_read(message)
    await message.delete()


async def fikr(message: types.Message):
    await bot.send_message(message.from_user.id,'Fikr yoki Takliflaringiz bo`lsa yozib qoldirishingiz mumkin.')
    await message.delete()

   
async def contacts(message: types.Message):
    await bot.send_message(message.from_user.id,'Bizning ishonch telefon raqamlarimiz:')
    await bot.send_contact(chat_id=message.from_user.id, first_name=message.from_user.first_name, phone_number='000')
    await bot.send_contact(chat_id=message.from_user.id, first_name=message.from_user.first_name, phone_number='000')
    await message.delete()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(about, text='✍️Haqimizda✍️')
    dp.register_message_handler(location, text=['📍Manzil📍'])
    dp.register_message_handler(fikr, text=['💡Fikr💡'])
    dp.register_message_handler(products, text=['🍫Maxsulotlar🍫'])
    dp.register_message_handler(contacts, text=['📞Bog`lanish📞'])

