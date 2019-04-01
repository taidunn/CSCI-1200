#Tai Dunn
#CSCI 1200A
#Lab Exercise 10.0
#04/01/2019
#lab_10_0.py

yon = 'yes'

while yon != 'no':
	yon = input('Would you like to continue? ')
	yon = yon.lower()
	if yon == 'no':
		exit()
	else:
		email = input('Please enter your email: ')
		print('Welcome ' + email)
		filename = 'output_filename.txt'
		with open(filename, 'a') as file_object:
			file_object.write(email + '\n')
