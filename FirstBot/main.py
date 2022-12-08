from aiogram import Bot, Dispatcher, executor, types
from config_reader import config

# бот - сервер, который будет взаимодействовать с API Telegram

# TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'
# bot = Bot(TOKEN_API)


# скрываем токен в файле .env и заносим его в gitignore
# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())  # УСТАНАВЛИВАЕМ pip install pydantic[dotenv]

dp = Dispatcher(bot)# диспетчер отвечает за функционал бота (отслеживание, анализ...)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="start_bot")

# @dp.message_handler()
# async def check_more_one_world(message: types.Message):
#     if message.text.count(' ') >= 1:
#        await message.answer(text=message.text.upper()) # повторяет сообщение пользователя, если в нём больше одного слова
#
# @dp.message_handler()
# async def echo_upper(message: types.Message):
#     await message.answer(text=message.text.upper()) # повторяет сообщение пользователя, переводя его в верхний регистр

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # повторяет сообщение пользователя


if __name__ == '__main__':
    executor.start_polling(dp)