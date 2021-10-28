from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import button_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands=['7oo7'], is_chat_admin=True) pAr01!
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Labbay shef!', reply_markup=button_admin.button_case_admin)
    await message.delete()


async def cm_start(message: types.Message):
    if message.from_user.id ==  ID:
        await FSMAdmin.photo.set()
        await message.reply('Rasmni yuklang')


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id ==  ID:
        current_state = await state.get_state()
        if current_state is None:
            return 
        await state.finish()
        await message.reply('OK')



async def load_photo(message: types.Message, state = FSMContext):
    if message.from_user.id ==  ID:
        async  with state.proxy() as data:
            data['Rasm'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Maxsulot nomi?')

#Second answer


async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id ==  ID:
        async with state.proxy() as data:
            data['Maxsulot nomi'] = message.text
        await FSMAdmin.next()
        await message.reply('Maxsulot haqida')

#Third answer


async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id ==  ID:
        async with state.proxy() as data:
            data['Maxsulot haqida'] = message.text
        await FSMAdmin.next() 
        await message.reply('Maxsulot narxi')



async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id ==  ID:
        async with state.proxy() as data:
            data['Maxsulot narxi'] = message.text
        await sqlite_db.sql_add_command(state)
        sqlite_db.cur
        await state.finish()

#exit -> cancel

# @dp.message_handler(state="*", commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} o`chirildi', show_alert=True)

@dp.message_handler(commands='ochirish')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nTa`rifi: {ret[2]}\nNarxi {ret[-1]}')
            await  bot.send_message(message.from_user.id, text='☝️☝️☝️', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'{ret[1]} ni o`chirish ', callback_data=f'del {ret[1]}')))

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, text=['Yuklash'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='ochirish', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['7oo7'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands='ochirish')
   




