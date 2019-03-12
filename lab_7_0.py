#Tai Dunn
#CSCI 1200A
#Lab Exercise 7.0
#02/27/2019
#lab_7_0.py

x = 1
while x <= 5:
	print(x)
	x += 1

# Task 1
print('------------------------------------------------------')
print('Task 1')

user_name = input('Please enter your name: ')

# Task 2
print('------------------------------------------------------')
print('Task 2')

party_size = input('Enter party size: ')
party_size = int(party_size)

# Task 3
print('------------------------------------------------------')
print('Task 3')

if party_size <= 0:
	print('Please leave.')
elif 1 <= party_size <= 2:
	print('Your seat is ready')
elif 3 <= party_size <= 4:
	print('Please wait you will be seated in approximately 10 – 12' 
	+ ' minutes')
elif 5 <= party_size <= 8:
	print('Please wait you will be seated in approximately 20 – 25' 
	+ ' minutes')
elif 9 <= party_size <= 12:
	print('Please wait you will be seated in approximately 30 – 40' 
	+ ' minutes')
else:
	print('Please wait you will be seated in approximately 1 hour' 
	+ ' minutes')
		
