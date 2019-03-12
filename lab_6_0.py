#Tai Dunn
#CSCI 1200A
#Lab Exercise 6.0
#02/20/2019
#lab_6_0.py

# Task 1
print('------------------------------------------------------')
print('Task 1')
python_terms = {
	'Lists' : 'A list of items', 
	'Tuple' : 'is a finite ordered list', 
	'Dictionaries' : 'A collection of key-value pairs', 
	'Floats' : 'defines a variable with a fractional value', 
	'STEVE' : "It's Steve!"
	}

# Task 2
print('------------------------------------------------------')
print('Task 2')
for key, value in python_terms.items():
	print('The definition of a ' + key + ' is the following... ' + 
	value)
