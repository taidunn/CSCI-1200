#Tai Dunn
#CSCI 1200A
#Lab Exercise 9.1
#03/24/2019
#lab_9_1.py

#Greeting People
name = input('Greetings user what is your name? ')
print(name + ' we will now roll a six sided die 10 times... ')

#Importing Random
from random import randint

#Creating The Class
class Die():
	
	#Defining "roll_die"
	def roll_die():
		dice = randint(1,6)
		#Don't forget only to use 'return' not 'print' as 'print' will
		#return the number then "None" after every number"
		return(dice)

#Rolling the dice 10 times
for i in range(0,10):
	#Sending the imput back to the screen
    print(Die.roll_die())
