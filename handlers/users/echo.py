from aiogram import types

from loader import dp, db
from data.config import ADMINS


from filters.admins import IsAdmin








# Echo bot
@dp.message_handler(state='*')
async def bot_echo(message: types.Message):
    is_ban = db.is_banned_user(message.from_user.id)
    if is_ban:
        return await message.answer("Siz qora ro'yxatdasiz!")
    message_ = await message.forward(ADMINS[0])
    import datetime
    prev = datetime.datetime.today()
    prev_date = prev.strftime("%Y-%m-%d")
    db.add_message(message.chat.id, message_.message_id, push_date=prev_date)



