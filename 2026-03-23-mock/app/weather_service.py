# WE DO WANT TO TEST THIS MODULE

import app.weather_api_client as api

cities = ["Tel Aviv", "Jerusalem", "Haifa"]


def get_city_temp(city):
    if city in cities:
        data = api.get_weather(city)
        return data["temp"]
    else:
        return None


if __name__ == "__main__":
    print(get_city_temp("Jerusalem"))
    print(get_city_temp("Eilat"))
