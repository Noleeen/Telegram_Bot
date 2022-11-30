from aiogram import Bot, Dispatcher, types, executor
import string
import random

HELP_COMAND = '''
/help - список команд
/<b>start</b> - <em>начать работу с ботом</em>
/description - описание бота
/random_letters - отвечает случайным символом из латинского алфавита
/count - количество вызовов данной функции
# /count2 - кол-во "b" в сообщении пользователя 
#/send_user_id - отправляет личное сообщение написавшему пользователю
/check_zero - проверяет есть ли в сообщении 0
/sticker - отправляет вам стикер
/id_stiker - показывает пользоватедю id стикера, который он отправил
/emoji - отвечать 
/картинка - выводит фото (указываем либо пть к файлу, либо ссылку с интернета)
/location - отправляет пользовател карту с точкой по заданным координатам
'''
TOKEN_API = '5834874802:AAGfg5faAVAf3Ra5aaBkjZlJM42_r9n207k'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0

async def on(_):
    print('бот запущен (сильно сильно запущен...))')



@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    # await bot.send_message(chat_id=message.from_id, text=HELP_COMAND, parse_mode='HTML') # отправляет в личку
    # await message.delete() # удаляет сообщение пользователя
    await message.reply(text=HELP_COMAND, parse_mode='HTML') # отправляет в чат

# @dp.message_handler()
# async def count_b(message: types.Message):
#     await message.answer(text=str(message.text.count('b')))
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="start_bot")

@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer('тут пишем <em>описание</em> вашего <b>бота</b>', parse_mode='HTML') # МОЖНО РЕДАКТИРОВАТЬ НАЧЕРТАНИЕ РАЗМЕТКОЙ HTML
    await message.delete()


@dp.message_handler(commands=['count'])
async def count_(message: types.Message):
    global count
    await message.answer(f'count = {count}')
    count += 1

@dp.message_handler(commands=['random_letters'])
async def rand_lett(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))


@dp.message_handler(commands=['check_zero'])
async def check_zero(message: types.Message):
    if '0' in message.text:
        return await message.answer('yes')
    await message.answer('no')


@dp.message_handler(commands=['sticker'])
async def stick(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEGnGBjhjFF0NrUltTf1A9gypK1sAAB8k8AAiAZAAJLDYlKFctt7myEf8srBA")


@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['emoji'])
async def em(message: types.Message):
    await message.reply(message.text + '\n 😂')

@dp.message_handler(commands='картинка')
async def image_send(message: types.Message):
    await bot.send_photo(chat_id=message.from_id,
                         photo='https://img2.akspic.ru/previews/5/8/2/8/6/168285/168285-astronavt-risovanie-kosmos-kosmicheskoe_prostranstvo-multfilm-500x.jpg')

@dp.message_handler(commands='location')
async def location_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=54.430827,
                            longitude=28.710073)
    await message.delete()


# @dp.message_handler()
# async def send_user_id(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,text="helloolo") # не работает из чата(((


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on, skip_updates= True) #skip_updates=True бот при включении не обрабатывает запросы, которые посылались ему когда он был выключен
