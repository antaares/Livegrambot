from aiogram import executor

from loader import dp
import middlewares, filters, handlers


async def on_startup(dispatcher):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
