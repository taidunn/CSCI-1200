#Tai Dunn
#CSCI 1200A
#Lab Exercise 3.1
#01/28/2019
#lab_3_1.py


#Creating the list
print('------------------------------------------------------')
print('Task 1')
test = ['Sheldon', 'Leonard', 'Penny', 'Howard', 'Bernadette', 'Rajesh', 'Stuart']
print(test)

#Inserting Amy between Sheldon and Leonard
print('------------------------------------------------------')
print('Task 2')
test.insert(1, 'Amy')
print(test)

#Reverse the order of the list. Note: not reverse sort, just reverse().
print('------------------------------------------------------')
print('Task 3')
print(sorted(test,reverse = True))

#Reverse the order of the list again to revert to the original order.
print('------------------------------------------------------')
print('Task 4')
print(test)

#Print the list again using the temporary sort; sorted().
print('------------------------------------------------------')
print('Task 5')
print(sorted(test))

#Print the list again to demonstrate that you have not (yet) permanently changed the list.
print('------------------------------------------------------')
print('Task 6')
print(test)

#Now sort the list in reverse order. Print the list. Note: this is a permanent change to the list.
print('------------------------------------------------------')
print('Task 7')
test.sort(reverse=True)
print(test)

print('------------------------------------------------------')
print('Task 8')
test.sort()
print(test)

#Print the length of the list.
print('------------------------------------------------------')
print('Task 9')
print(len(test))

#Remove Stuart from the end of the list. Print the list.
print('------------------------------------------------------')
print('Task 10')
test.remove('Stuart')
print(test)

#Print the length of the list again.
print('------------------------------------------------------')
print('Task 11')
print(len(test))

print('------------------------------------------------------')
print('Task 12')
print(test[7])
