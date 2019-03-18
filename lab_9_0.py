#Tai Dunn
#CSCI 1200A
#Lab Exercise 9.0
#03/18/2019
#lab_9_0.py

# Task 1
print('------------------------------------------------------')
print('Task 1')

class User():
	
	def __init__(self,username,first_name,last_name):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
		
	def describe_user(self):
		print('The user ' + self.username + ' is ' + 
		self.first_name.title() +  ' ' + self.last_name.title() + '.')
	
	def greet_user(self):
		print('Greetings ' + self.username)
		print('Good to see you again!')

# Task 2
#Declaring Users 
	
first = User('flamingeye','Fire','Eye')
second = User('sweldon','Steven','Weldon')

# Task 3
print('------------------------------------------------------')
print('Task 3')

print('A description of the users.')
first.describe_user()
second.describe_user()

# Task 4
print('------------------------------------------------------')
print('Task 4')

print('Greeting Users')
first.greet_user()
second.greet_user()
