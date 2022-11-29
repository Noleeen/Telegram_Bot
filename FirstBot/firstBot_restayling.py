from aiogram import Bot, Dispatcher, types, executor
import string
import random


HELP_COMAND = '''
/help - список команд
/start - начать работу с ботом
/description - описание бота
/random_letters - отвечает случайным символом из латинского алфавита
/count - количество вызовов данной функции
'''

TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0

@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer('тут пишем описание вашего бота')
    await message.delete()

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(text=HELP_COMAND)


@dp.message_handler(commands=['count'])
async def count_(message: types.Message):
    global count
    await message.answer(f'count = {count}')
    count += 1

@dp.message_handler(commands=['random_letters'])
async def rand_lett(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="start_bot")


if __name__ == "__main__":
    executor.start_polling(dp)