import asyncio

from aiogram import Bot, Dispatcher



bot = Bot(token=TOKEN)
dp = Dispatcher()





async def main():
   await dp.start_polling(bot)


   


if __name__ == "__main__":
   try:
      asyncio.run(main())
   except KeyboardInterrupt:
      print("Бот выключен")