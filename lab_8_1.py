#Tai Dunn
#CSCI 1200A
#Lab Exercise 8.1
#03/17/2019
#lab_8_1.py

# Task 1
print('------------------------------------------------------')
print('Task 1')

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
name = first_name + ' ' + last_name
name = name.title()

# Task 2
print('------------------------------------------------------')
print('Task 2')

num1 = input(name + ' please enter your first value: ')
num2 = input(name + ' please enter your second value: ')


# Task 3

num1 = int(num1)
num2 = int(num2)

# Task 3

added = num1 + num2
subtracted = num1 - num2
divided = num1 / num2
multiply = num1 * num2

# Task 4
print('------------------------------------------------------')
print('Task 4')

#Adding
print(name + ' when you add ' + str(num1) + ' ' + str(num2) +
 ' you will get ' + str(added) + '.')

#Subtracting
print(name + ' when you subtract ' + str(num1) + ' ' + str(num2) + 
' you will get ' + str(subtracted) + '.')

#Dividing
print(name + ' when you divide ' + str(num1) + ' ' + str(num2) +
 ' you will get ' + str(divided) + '.')
 
#Multiplying
print(name + ' when you multiply ' + str(num1) + ' ' + str(num2) +
 ' you will get ' + str(multiply) + '.')
