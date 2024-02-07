#!/usr/bin/env python3

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import dotenv
import os

from database import database

dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

birds = database.load_birds('dbb')


@dp.message(Command(commands=['start']))
async def process_start_command(message:Message):
    await message.answer('Hello! This is birds bot')


@dp.message(Command(commands=['list']))
async def list_of_birds(message:Message):
    lst = map(lambda x: x['short_name'], birds)
    string = '\n'.join(lst)
    await message.answer(f'list of birds:\n{string}')


@dp.message(Command(commands=['list_images']))
async def list_of_birds(message:Message):
    await message.answer('list of birds with images')


@dp.message(Command(commands=['count']))
async def birds_count(message:Message):
    await message.answer(f'count of birds  in base: {len(birds)}')


@dp.message()
async def default_answer(message:Message):
    print(message.__dict__)
    await message.answer('default answer to non-handling message')

if __name__ == '__main__':
    dp.run_polling(bot)
