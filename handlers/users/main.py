from aiogram import types

from loader import dp, db
from data.config import ADMINS


from filters.admins import IsAdmin


@dp.message_handler(IsAdmin(), commands=['ban'], is_reply=True)
async def ban_user(message: types.Message):
    if message.reply_to_message.forward_from and message.reply_to_message.forward_from.id:
        db.add_banned_user(message.reply_to_message.forward_from.id)
    else:
        user = db.get_message_chat_id(message.reply_to_message.message_id)
        db.add_banned_user(user)
    await message.reply("Foydalanuvchi bloklandi.")




@dp.message_handler(IsAdmin(), commands=['unban'], is_reply=True)
async def unban_user(message: types.Message):
    if message.reply_to_message.forward_from and message.reply_to_message.forward_from.id:
        db.remove_banned_user(message.reply_to_message.forward_from.id)
    else:
        user = db.get_message_chat_id(message.reply_to_message.message_id)
        db.remove_banned_user(user)
    await message.reply("Foydalanuvchi qayta qabul qilindi.")


@dp.message_handler(IsAdmin(), content_types = types.ContentTypes.ANY)
async def admin_reply(message: types.Message):
    if isinstance(message.reply_to_message, types.Message):
        reply_m = message.reply_to_message
        if reply_m.forward_from and reply_m.forward_from.id:
            await message.copy_to(reply_m.forward_from.id, reply_markup=message.reply_markup)
        else:
            message_id_ = reply_m.message_id
            chat_id = db.get_message_chat_id(message_id_)
            await message.copy_to(chat_id, reply_markup=message.reply_markup)
    else:
        pass

