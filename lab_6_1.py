#Tai Dunn
#CSCI 1200A
#Lab Exercise 6.1
#02/25/2019
#lab_6_1.py

# Task 1
print('------------------------------------------------------')
print('Task 1')
cities = {
	'New York City' : {
	'county' : 'Manhattan',
	'state' : 'New York',
	'population' : '8.623 million',
	},
	'Seattle' : {
	'county' : 'King County',
	'state' : 'Washington',
	'population' : '724,745',
	},
	'Hollywood' : {
	'county' : 'Los Angeles',
	'state' : 'California',
	'population' : '4 million',
	},
	}	


# Task 2
print('------------------------------------------------------')
print('Task 2')

for key, value in cities.items():
	print(key.title() + ' is located in ' + value['county'] + ',' +
	value['state'])
	print ('It has the population of ' + value['population'])

