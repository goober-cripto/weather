import requests


async def get_geolocation(city: str) -> tuple[float, float]:
    """
    Получает геолокацию (широту и долготу) для заданного города.

    :param city: str - Название города, для которого необходимо получить геолокацию.
                     Должен быть строковым значением (например, "Москва", "Нью-Йорк").

    :return: tuple[float, float] - Кортеж, содержащий широту и долготу города в виде
                                    чисел с плавающей точкой. Если город не найден,
                                    возвращает (None, None).
    """
    geocoding_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
    geocoding_response = requests.get(geocoding_url)

    if geocoding_response.status_code == 200:
        geocoding_data = geocoding_response.json().get('results', [])
        if geocoding_data:
            latitude = geocoding_data[0]['latitude']
            longitude = geocoding_data[0]['longitude']
            return latitude, longitude
    return None, None
