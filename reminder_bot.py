import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import asyncio

API_TOKEN = os.getenv("TG_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

reminders = {}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот-напоминальщик. \n\nИспользуй /set чтобы создать напоминание.")

@dp.message_handler(commands=['set'])
async def set_reminder(message: types.Message):
    reminders[message.from_user.id] = message.text.split("/set", 1)[1].strip()
    await message.reply(f"Напоминание установлено: {reminders[message.from_user.id]}")
    await asyncio.sleep(10)  # Напоминаем через 10 секунд, вы можете заменить это на любое другое значение
    await message.reply(f"Напоминание: {reminders[message.from_user.id]}", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
