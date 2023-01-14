import time
import logging
from aiogram import Bot, Dispatcher, executor, types

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")

with open("info.txt", "r") as f:
    text = f.readline()
TOKEN = str(text)
MSG = "{}, choose an action:"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    time.sleep(1)
    # btns = types.InlineKeyboardMarkup(row_width=2)
    # btn_calc = types.InlineKeyboardButton('calculator', callback_data='calc')
    # btn_out = types.InlineKeyboardButton('quit', callback_data='out')
    # btns.add(btn_calc, btn_out)
    # await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)


# @dp.callback_query_handler(lambda c: c.data == 'out')
# async def callback_btn_out(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Goodbye! See you...',
#                            reply_markup=types.ReplyKeyboardRemove())

value = ""
old_value = ""
keyboard = types.InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton("C", callback_data="C"),
             types.InlineKeyboardButton("<=", callback_data="<="),
             types.InlineKeyboardButton("(", callback_data="("),
             types.InlineKeyboardButton("/", callback_data="/"))
keyboard.row(types.InlineKeyboardButton("7", callback_data="7"),
             types.InlineKeyboardButton("8", callback_data="8"),
             types.InlineKeyboardButton("9", callback_data="9"),
             types.InlineKeyboardButton("*", callback_data="*"))
keyboard.row(types.InlineKeyboardButton("4", callback_data="4"),
             types.InlineKeyboardButton("5", callback_data="5"),
             types.InlineKeyboardButton("6", callback_data="6"),
             types.InlineKeyboardButton("-", callback_data="-"))
keyboard.row(types.InlineKeyboardButton("1", callback_data="1"),
             types.InlineKeyboardButton("2", callback_data="2"),
             types.InlineKeyboardButton("3", callback_data="3"),
             types.InlineKeyboardButton("+", callback_data="+"))
keyboard.row(types.InlineKeyboardButton("0", callback_data="0"),
             types.InlineKeyboardButton(",", callback_data="."),
             types.InlineKeyboardButton(")", callback_data=")"),
             types.InlineKeyboardButton("=", callback_data="="))


# @dp.callback_query_handler(lambda c: c.data == 'calc')
# async def callback_btn_calc(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'I open the calculator',
#                            reply_markup=keyboard)


@dp.message_handler(commands=['calculator'])
async def start_handler(message: types.Message):
    if value == "":
        await bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@dp.callback_query_handler(lambda c: True)
async def callback_calc(query):

    global value, old_value
    data = query.data

    if data == "C":
        value = ""
    elif data == "<=":
        if value != "":
            if len(value) == 1:
                value = ""
            else:
                value = value[:len(value)-1]
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Error"
    else:
        value += data

    if (value != old_value and value != "") or ("0" != old_value and value == ""):
        if value == "":
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text="0", reply_markup=keyboard)
            old_value = "0"
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=value, reply_markup=keyboard)
            old_value = value

    if value == "Error":
        value = ""


if __name__ == '__main__':
    executor.start_polling(dp)
