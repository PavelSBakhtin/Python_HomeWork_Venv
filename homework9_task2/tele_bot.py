import time
import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

with open("info.txt", "r") as f:
    text = f.readline()
TOKEN = str(text)
MSG = "{}, how are you feeling today? ({}, {})"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hi, {user_full_name}!")

    for i in range(7):
        time.sleep(60*60*24)
        k = i + 1
        await bot.send_message(user_id, MSG.format(user_name, datetime.datetime.now().strftime('%a'), k))

if __name__ == '__main__':
    executor.start_polling(dp)
