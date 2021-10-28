from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


b1 = KeyboardButton('🍫Maxsulotlar🍫')
b2 = KeyboardButton('✍️Haqimizda✍️')
# b3 = InlineKeyboardButton(text='Manzilga o`tish', url='https://goo.gl/maps/uVAMtEYpucFwNVwR7')
b3 = KeyboardButton('📍Manzil📍')
b4 = KeyboardButton('💡Fikr💡')
b5 = KeyboardButton('📞Bog`lanish📞')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3).insert(b4).row(b5)

