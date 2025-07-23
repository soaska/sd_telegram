from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import ALLOWED_USERS

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return not ALLOWED_USERS or message.from_user.id in ALLOWED_USERS