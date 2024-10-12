from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_comands(bot: Bot):
    commands = [
        BotCommand(
            command='info',
            description='Общая информация'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
