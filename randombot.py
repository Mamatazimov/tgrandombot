import logging



from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
import random as r
API_TOKEN = '5938627630:AAFguH8tOY7QM2emxaSvjSmZt_iz91eHt2g'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


button1=KeyboardButton("1dan9gacha👾")
button2=KeyboardButton("1dan6gacha👾")
button3=KeyboardButton("1dan100gacha\n10 ta tasodifiy son")

keyboard1=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False).add(button1,button2,button3)







@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum. \nBu bot sizga tasodifiy son aniqlab beradi ",reply_markup=keyboard1)



@dp.message_handler()
async def tson(message: types.Message):
    if message.text=="1dan9gacha👾":
    	xabar=r.randint(1,9)
    elif message.text=="1dan6gacha👾":
    	xabar=r.randint(1,6)
    elif message.text=="1dan100gacha\n10 ta tasodifiy son":
    	xabar=list()
    	for x in range(11):
    		a=r.randint(1,100)
    		xabar.append(a)
    	
    else:
    	xabar="Xatolik yuz berdi!"
    await message.answer(xabar)
    
    



	



	



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)