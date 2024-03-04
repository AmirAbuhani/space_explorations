# Amir Abu Hani
# This is the second module. this module fetch a weather from an API. and print the galaxy weather that we launch to her

import requests


def exploring_the_galaxy():
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast?latitude=40.416775&longitude=-3.703790&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    # if the API not available
    response.raise_for_status()
    data = response.json()
    # get the field with the temperature in our galaxy
    galactic_weather = data["current"]["temperature_2m"]
    galaxy_name = "Whirlpool Galaxy"
    print(f"We explored the {galaxy_name}. The weather there is {galactic_weather}°C. Soon we will launch a spacecraft "
          f"to this galaxy!")


