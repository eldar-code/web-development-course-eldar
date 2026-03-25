from unittest.mock import patch
from unittest import TestCase
from app import weather_service


class TestWeatherService(TestCase):

    

    @patch("app.weather_service.api.get_weather", return_value={"city": "Haifa", "temp": 25})
    def test_get_city_temp(self, mock_get_weather):
        temp = weather_service.get_city_temp("Haifa")
        self.assertEqual(25, temp, "Wrong temperature value")

        temp = weather_service.get_city_temp("Eilat")
        self.assertIsNone(temp, "Non existing city should return None")

        # check that we actually used the mock in the test
        mock_get_weather.assert_called_with("Haifa")
