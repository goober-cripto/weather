import requests
from datetime import datetime

from aiogram.types import Message

from utils.geolocation import get_geolocation
from utils.dictionaries import weather_codes, error_bot


async def get_weather(message: Message):
    """
        Обрабатывает запрос пользователя на получение данных о погоде в указанном городе.

        :param message: Сообщение, содержащее название города, для которого нужно получить данные о погоде.
        """
    city = message.text
    latitude, longitude = await get_geolocation(city)
    try:
        if latitude is not None and longitude is not None:
            weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m,weathercode'
            weather_response = requests.get(weather_url)

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                current_weather = weather_data.get('current_weather', {})
                hourly_data = weather_data.get('hourly', {})
                timestamps = hourly_data.get('time', [])

                # Определяем текущий час
                current_hour = datetime.utcnow().hour

                # Находим индекс, соответствующий текущему часу
                humidity_index = next(
                    (i for i, t in enumerate(timestamps) if datetime.fromisoformat(t).hour == current_hour), None)

                # Если индекс найден, выбираем влажность для текущего часа
                humidity = hourly_data.get('relativehumidity_2m', [])[
                    humidity_index] if humidity_index is not None else 'N/A'
                temperature = current_weather.get('temperature', 'N/A')
                windspeed = current_weather.get('windspeed', 'N/A')
                weather_code = current_weather.get('weathercode', 'N/A')
                weather_description = weather_codes.get(weather_code, "Неизвестный код погоды")

                await message.reply(
                    f"""🌡 <b>Погода в городе {city}:</b>
                    \nТемпература: {temperature}°C\nСкорость ветра: {windspeed} км/ч\nВлажность: {humidity}%\nОписание: {weather_description}""",
                    parse_mode="HTML")
            else:
                await message.reply(f"""❌ Ошибка получения данных о погоде""", parse_mode="HTML")
        else:
            await message.reply(f"""❌ Город {city} не найден""", parse_mode="HTML")
    except:
        await message.reply(error_bot, parse_mode="HTML")
