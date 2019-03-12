#Tai Dunn
#CSCI 1200A
#Lab Exercise 7.1
#03/04/2019
#lab_7_1.py

# Task 1
print('------------------------------------------------------')
print('Task 1')

responses = {}
question = True

while question:
	name = input('What is your name? ')
	destination = input('Where are you going for Spring Break? ')
	
	responses[name] = destination
	
	repeat = input('Is anyone else going to take this poll yes/no? ')
	if repeat.title() == 'No':
		question = False

for name, response in responses.items():
	print(name.title() + ' is planning to go to ' + 
	response.title() + ' for vacation.') 

# Task 2
print('------------------------------------------------------')
print('Task 2')	
	
print(responses)
		
