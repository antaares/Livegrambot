import logging
from aiogram import executor

import aioschedule, asyncio

from loader import dp, db
import middlewares, filters, handlers

logging.basicConfig(level=logging.INFO)
async def on_startup(dispatcher):
    db.create_table_users()
    db.create_table_banned_users()
    db.create_messages_table()


async def delete_messages():
    db.delete_old_messages()

async def scheduler(time_):
    # aioschedule.
    aioschedule.every().day.at(time_).do(delete_messages)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.create_task(scheduler('00:00'))
    executor.start_polling(dp, on_startup=on_startup)
