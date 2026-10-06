import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        formatted_city = get_formatted_city(
            'santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')

unittest.main()
