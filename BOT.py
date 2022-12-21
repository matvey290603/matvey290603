import config
import logging
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)
bot = Bot(token="5667467600:AAEUmUdxOJZhqOMZ1NDUAJrK_THWgR67-aU")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [" обычные шутки", "черные шутки","шутки 18+","закрыть"]
    keyboard.add(*buttons)
    await message.answer("Хочешь скоротать время? Почитай наши шутки", reply_markup=keyboard)

urlkb=InlineKeyboardMarkup(row_width=2)
A=InlineKeyboardButton(text="норм шутка", callback_data="www")
B=InlineKeyboardButton(text="удали это", callback_data="www")
urlkb.add(A, B)
@dp.message_handler(lambda message: message.text == "обычные шутки")
async def without_puree(message: types.Message):
    await message.answer(random.choice(config.Shutka), reply_markup=urlkb)

@dp.callback_query_handler(text="www")
async def www_call(callback: types.CallbackQuery):
    await callback.answer("как скажешь")

@dp.message_handler(lambda message: message.text == "черные шутки")
async def without_puree(message: types.Message):
    await message.answer(random.choice(config.CH), reply_markup=urlkb)

@dp.message_handler(lambda message: message.text == "шутки 18+")
async def without_puree(message: types.Message):
    await message.answer(random.choice(config.SEX), reply_markup=urlkb)
   
@dp.message_handler(lambda message: message.text == "закрыть")
async def without_puree(message: types.Message):
    await message.reply("Ну и иди дальше занимайся своими делами")


    

if __name__ == "__main__":
    executor.start_polling(dp)
