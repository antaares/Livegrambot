from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class Isbanned(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return False
