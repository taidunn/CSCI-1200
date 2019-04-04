#Tai Dunn
#CSCI 1200A
#Lab Exercise 11.0
#04/03/2019
#lab_11_0.py

import unittest
from city_state_name import get_formatted_city_state_name

class CityStateNamesTestCase(unittest.TestCase):
	
	def test_get_formatted_city_state_name(self):
		formatted_name = get_formatted_city_state_name('augusta', 
		'georgia')
		self.assertEqual(formatted_name, 'Augusta, Georgia')
		
unittest.main()
	
