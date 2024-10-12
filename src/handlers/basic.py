from aiogram import Bot
from aiogram.types import Message


async def comand_start(message: Message, bot: Bot):
    """
        Обрабатывает команду /start, отправляя приветственное сообщение пользователю.

        :param message: Сообщение, содержащее информацию о пользователе и чате.
        :param bot: Экземпляр бота, используемый для отправки сообщений.
        """
    chat_id = message.chat.id
    welcome_message = """<b>Привет! Я твой личный погодный бот 🌦️</b>\n\nС помощью меня ты сможешь узнать текущую погоду в любом городе мира! Просто введи название города, и я предоставлю тебе информацию о температуре, скорости ветра, влажности и описании погоды\n\n💡 <b>Примеры команд:</b>\n- <i>Moscow</i>\n- <i>New York</i>\n- <i>London</i>"""

    await bot.send_message(chat_id, welcome_message)


async def comand_info(message: Message):
    """
        Обрабатывает команду для получения информации о погоде,
        запрашивая у пользователя ввод названия города на английском языке.

        :param message: Сообщение, содержащее информацию о пользователе и чате.
        """
    await message.reply(
        f"""<b>Узнай погоду в своём городе!</b>
        \nВведи свой город на английском языке\n\n<i>например: Moscow</i>""",
        parse_mode="HTML")
