from aiogram.types import Message
from aiogram import Router
import logging

logger = logging.getLogger(__name__)
router = Router()

@router.message()
async def default_answer(message:Message):
    logger.debug(str(message.from_user.id) + '- ' + message.from_user.username + ': ' + message.text)
    await message.answer('default answer fot not handling message')
