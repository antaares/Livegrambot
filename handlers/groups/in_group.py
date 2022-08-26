from aiogram import types

from loader import dp, bot


from filters.group import IsGroup




@dp.message_handler(IsGroup(), content_types=types.ContentType.ANY)
async def echo(message: types.Message):
    await bot.leave_chat(message.chat.id)