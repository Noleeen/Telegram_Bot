from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

HELP = '''
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>список команд</em>
<b>/discription</b> - <em>описание</em>
<b>/pict</b> - <em>кидает фотку</em>
<b>/close</b> - <em>закрывает клавиатуру</em>'''

kb = ReplyKeyboardMarkup(resize_keyboard= True, # подгоняет размер под окно телеги
                         one_time_keyboard= True) # убирает клавиатуру после нажатия
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/discription')
b3 = KeyboardButton('/pict')
b4 = KeyboardButton('/close')

kb.add(b1).insert(b2).add(b3).insert(b4)

TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_com(message: types.Message):
    await message.answer('hello&',
                         reply_markup=kb)

@dp.message_handler(commands=['close'])
async def close_com(message: types.Message):
    await message.answer('keyboard goodbye',
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['help'])
async def help_com(message: types.Message):
    await bot.send_message(chat_id= message.from_user.id,
                           text = HELP,
                           parse_mode = "HTML")

@dp.message_handler(commands=['pict'])
async def pict_com(message: types.Message):
    await bot.send_photo(chat_id= message.chat.id,
                           photo = "https://img2.joyreactor.cc/pics/post/full/anon-%D0%9A%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0-2191131.jpeg")


@dp.message_handler(commands=['discription'])
async def pict_com(message: types.Message):
    await message.answer('тестируем кнопАчыки')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)