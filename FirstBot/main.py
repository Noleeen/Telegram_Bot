from aiogram import Bot, Dispatcher, executor, types

# бот - сервер, который будет взаимодействовать с API Telegram

TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)# диспетчер отвечает за функционал бота (отслеживание, анализ...)
@dp.message_handler()
async def check_more_one_world(message: types.Message):
    if message.text.count(' ') >= 1:
       await message.answer(text=message.text.upper()) # повторяет сообщение пользователя, если в нём больше одного слова

@dp.message_handler()
async def echo_upper(message: types.Message):
    await message.answer(text=message.text.upper()) # повторяет сообщение пользователя, переводя его в верхний регистр

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # повторяет сообщение пользователя


if __name__ == '__main__':
    executor.start_polling(dp)