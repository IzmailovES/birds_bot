from config_data import global_config
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram import Router

import logging

from database.database import birds

from .filters import IsAdmin
router = Router()

logger = logging.getLogger(__name__)


@router.message(Command(commands=['count']), IsAdmin())
async def admin_count(message:Message):
    await message.answer(f'count birds in base: {len(birds)}')
