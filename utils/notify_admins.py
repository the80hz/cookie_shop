import logging
from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            await dp.bot.send_message(admin, "Бот запущен")
        except Exception as err:
            logging.exception(err)
