import aiogram
from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
# обработка команды старт
async def cmd_start(message: Message):
    await message.answer('hello')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('this is help command')


async def main():
    # функция запуска бота в работу
    await dp.start_polling(bot)


if __name__ == '__main__':
    # включение логирования для отслежки логов при работе бота
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
