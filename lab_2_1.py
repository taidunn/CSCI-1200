# Tai Dunn
# CSCI 1200A
# Lab Exercise 2.1
# 1/16/2019
 
#***********************************************************************
print('Lab 2.1')
print()

# Task 1
print('*****')
print('Task 1')
print(' ')

# Declare a variable
# Set the string's value to your first name in title case (ex. Eric)
# Be sure to follow variable naming conventions
# Enter your code in the line below
first_name = "tai";
first_name = first_name.title();


# Declare another variable
# Set the string's value to your last name in title case (ex. Idle)
# Be sure to follow variable naming conventions
# Enter your code in the line below
last_name = "dunn";
last_name = last_name.title();


# Print your first and last name to the screen using concatenation
# Include one space between your first and last names
print(first_name + ' ' + last_name);

# Declare another variable to hold your full name in title case
# Concatenate the values of your first and last name variables
# (ex. Eric Idle)
# Save them as your full name in the line below
full_name = first_name + ' ' + last_name


# Now convert your full name to all lower case 
# Save the value to be the new value of your full name variable
# (ex. eric idle)
full_name = full_name.lower()


# Print the value of your full name variable
print(full_name)

# Print the value of your full name varible using the title() function
print(full_name.title())

# Print the value of your full name variable again, without title()
# Note: This demonstrates you haven't changed the value
print(full_name)


print(' ') # For whitespace
#***********************************************************************

# Task 2
print('*****')
print('Task 2')
print(' ')

# Declare an integer variable
# Give this variable the value of your favorite integer
favorite_int = 5389

# Print your variable's value to the screen
print(favorite_int)

# Declare another variable with a float value
# Give this variable the value of your favorite float
favorite_float = 3.141592

# Print this variable's value to the screen
print(favorite_float)

# Divide your integer by your float (int / float)
# Print this calculation to the screen
print(favorite_int / favorite_float)


# Now divide your float by your integer (float / int)
# Print this calculation to the screen as well
print(favorite_float / favorite_int)


#***********************************************************************
print()
print('*****')
print()
print('End Lab 2.1')
