#Tai Dunn
#CSCI 1200A
#Lab Exercise 8.0
#03/11/2019
#lab_8_0.py

# Task 1
print('------------------------------------------------------')
print('Task 1')

def describe_city(city, country='United States'):
	if country.title() == 'United States':
		print(city + ' is a city in the ' + country)
	else: 
		print(city + ' is a city in ' + country)
		
describe_city('San Diego', 'UnIted States')
describe_city('Hidden Hills')
describe_city(country='Russia', city='St. Petersburg')
