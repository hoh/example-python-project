import time

import requests


def get_weather(latitude: float, longitude: float):
    """Fetch weather data for a specific geolocation."""
    url_template = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    url = url_template.format(latitude=latitude, longitude=longitude)
    # Make a request to the API
    response = requests.get(url=url)
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()
    # Parse the JSON response
    data = response.json()
    return data


def get_current_date() -> str:
    """Return the current date and time as a string."""
    # Get the current timestamp in seconds
    current_timestamp = time.time()  # Do not edit, use a mock instead
    return time.ctime(current_timestamp)
