import logging
from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers

logging.basicConfig(level=logging.INFO)
async def on_startup(dispatcher):
    db.create_table_users()
    db.create_table_banned_users()
    db.create_messages_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
