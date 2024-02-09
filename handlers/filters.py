from aiogram.filters import BaseFilter
from aiogram.types import Message
from config_data import global_config

import logging

logger = logging.getLogger(__name__)

class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self.admin_id = global_config.tg_bot.admin

    async def __call__(self, message:Message):
        ret = message.from_user.id == self.admin_id
        logger.debug(f'{message.from_user.id}, {self.admin_id}, ret: {ret}')
        return ret

