import asyncio
import asyncpg

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from middleware.dbmidelware import DbSession
from settings.config import data_settings

from handlers.commands import set_comands
from handlers.basic import comand_info, comand_start
from handlers.get_weather import get_weather


async def create_pool():
    return await asyncpg.create_pool(user=data_settings.setting.db_user,
                                     password=data_settings.setting.db_password,
                                     database=data_settings.setting.db_name,
                                     host=data_settings.setting.db_host,
                                     port=data_settings.setting.db_port,
                                     command_timeout=60)


async def start_bot(bot: Bot):
    await set_comands(bot)
    await bot.send_message(chat_id=data_settings.setting.tg_admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=data_settings.setting.tg_admin_id, text="Бот остановлен!")


async def start():
    bot = Bot(token=data_settings.setting.tg_bot_token, parse_mode='HTML')
    pool_connect = await create_pool()

    dp = Dispatcher()
    # на все виды событий регистрируем миделвар с базой данных
    dp.update.middleware.register(DbSession(pool_connect))

    # выполняем код на начало работы бота и конец
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # отработка команды первого запуска /start
    dp.message.register(comand_start, Command(commands='start'))

    # информация о боте
    dp.message.register(comand_info, Command(commands='info'))

    # На любое сообщение отвечает
    dp.message.register(get_weather)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
