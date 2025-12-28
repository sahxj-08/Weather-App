import requests

api_key = '0452e7a8b1aaad6cc6f14c75327e776e'

user_input = input("Enter a city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Sorry, no city found ...")

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

    def celsius(temp):
        return (temp - 32) * (5/9)

    cel = round(celsius(temp))

    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature in {user_input} is {cel}°C")