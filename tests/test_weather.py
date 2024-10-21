from unittest import mock

import pytest

from cool_project.weather import get_current_date, get_weather


def test_get_weather_fake_api():
    """Test the get_weather function with a fake API call."""
    # mock the requests.get function
    with mock.patch("requests.get") as mock_get:
        # set the return value of the mock
        mock_get.return_value.json.return_value = {
            "current": {
                "temperature_2m": 20,
                "wind_speed_10m": 5,
            }
        }
        data = get_weather(50.8505, 4.3488)
        assert "current" in data
        assert "temperature_2m" in data["current"]
        assert "wind_speed_10m" in data["current"]


@pytest.mark.networking
def test_get_weather_with_network():
    """Test the get_weather function with a real API call."""
    data = get_weather(50.8505, 4.3488)
    assert "current" in data
    assert "temperature_2m" in data["current"]
    assert "wind_speed_10m" in data["current"]


def test_get_current_date():
    assert get_current_date() == "Mon Oct 21 14:55:46 2024"
