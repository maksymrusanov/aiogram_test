import aiogram
from aiogram import Bot, Dispatcher
import asyncio
# импортируем руты
from app.handlers import router

from config import TOKEN
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    # подключаем руты из app/handlers.py
    dp.include_router(router)
    # функция запуска бота в работу
    await dp.start_polling(bot)


if __name__ == '__main__':
    # включение логирования для отслежки логов при работе бота
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
