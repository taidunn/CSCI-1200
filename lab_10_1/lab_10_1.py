#Tai Dunn
#CSCI 1200A
#Lab Exercise 10.1
#04/01/2019
#lab_10_1.py

#starting = 'pg32032.txt'
starting = input('Please enter a file without the .txt: ')
starting = starting + '.txt'

try:
	with open(starting) as input_f_object:
		contents = input_f_object.read()
except FileNotFoundError:
	msg = 'The file ' + starting + ' does not exist.'
	print(msg)
else:
	#Counting
	words = contents.split()
	number = len(words)
	print(number)
	
	#Writing to file
	filename = 'lab_10_1.results.txt'
	with open(filename, 'a') as file_object:
		file_object.write('The word count for file ' + starting + 
		' is exactly ' + str(number) + ' words.' + '\n')
