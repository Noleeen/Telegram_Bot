from aiogram import Bot, Dispatcher, executor, types

# бот - сервер, который будет взаимодействовать с API Telegram

TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)# диспетчер отвечает за функционал бота (отслеживание, анализ...)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # написать сообщение text

if __name__ == '__main__':
    executor.start_polling(dp)