import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.types import Message
from config import TOKEN
import logging
from app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()
bot.parse_mode = 'html'


logging.basicConfig(level=logging.INFO)

async def main():

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ =='__main__':
    

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
