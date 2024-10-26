import requests
from datetime import datetime
import json


def save(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S").replace(":", "-") + ".txt"

        with open(file_name, 'w') as f:
            f.write(json.dumps(result, indent=4))

        return result

    return wrapper


@save
def get_data(city: str):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e90fab7014064d2c88795d9fd95afa6f")
    data = response.json()
    return data


def show(data: dict):
    city = data['name']
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15, 1)  # Convert Kelvin to Celsius
    wind = wind_direction(data['wind']['deg'])

    print(f"City: {city}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temp} °C")
    print(f"Wind Direction: {wind}")

    res = {'city': city, 'weather': weather, 'temp': temp, 'wind': wind}
    return res


def wind_direction(deg: int):
    if 0 <= deg <= 45:
        return 'NE'
    elif 45 < deg <= 90:
        return 'EN'
    elif 90 < deg <= 135:
        return "ES"
    elif 135 < deg <= 180:
        return "SE"
    elif 180 < deg <= 225:
        return "SW"
    elif 225 < deg <= 270:
        return "WS"
    elif 270 < deg <= 315:
        return "WN"
    elif 315 < deg <= 360:
        return "NW"
    else:
        return 'NO WIND'


city = 'London'
data = get_data(city)
show(data)
