#  клавиатура с кнопками
#  на отправленное сердечко с клавиатуры бот отправляет стикер
#  при нажатии кнопки отправляем пользователю рандомную точку на карте

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from config_reader import config
from random import randrange

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)


kb = ReplyKeyboardMarkup(resize_keyboard= True)

k1 = KeyboardButton('/help')
k2 = KeyboardButton('/description')
k3 = KeyboardButton('/close')
k4 = KeyboardButton('❤️')

kb.add(k1).insert(k2).insert(k3).add(k4).insert(KeyboardButton('/random_location'))

HELP = '''
помоги себе <em>сам</em> =)
/help - список команд
/start - запускает клавиатуру
/'❤️'- за сэрца паказвае табе годны стыкер)
description - 
/random_location - показывает случайную точку на карте
/close - 
'''

async def on(_):
    print('бот запущен (сильно сильно запущен...))')

@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    await message.answer('hello-text',reply_markup=kb)


@dp.message_handler(commands=['help'])
async def com_help(message: types.Message):
    await message.answer(text= HELP, parse_mode = "HTML")

@dp.message_handler(commands=['description'])
async def com_discr(message:types.Message):
    await message.answer('asdgkfad;gkjhadsg')

@dp.message_handler(commands=['random_location'])
async def rand_loc(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude = randrange(0,100),
                            longitude= randrange(0,100))

@dp.message_handler(commands=['close'])
async def com_close(message: types.Message):
    await message.answer('bye', reply_markup = ReplyKeyboardRemove())

@dp.message_handler()
async def com_hart(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id = message.chat.id, sticker="CAACAgIAAxkBAAIB3GOR6OvjVuQnzXvr-XXqghRq5zkCAAJ5AAOAIPs1nzRNHFQSLGQrBA")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on, skip_updates=True)

