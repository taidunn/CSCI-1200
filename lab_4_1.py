#Tai Dunn
#CSCI 1200A
#Lab Exercise 4.1
#02/06/2019
#lab_4_1.py
print('------------------------------------------------------')
print('Task 1')
numbers = list(range(0, 1000000))

print('------------------------------------------------------')
print('Task 2')
print(len(numbers))

print('------------------------------------------------------')
print('Task 3')
print(min(numbers))

print('------------------------------------------------------')
print('Task 4')
print(max(numbers))

print('------------------------------------------------------')
print('Task 5')
print(sum(numbers))

print('------------------------------------------------------')
print('Task 6')
newnum=numbers[100:125]
print(newnum)

print('------------------------------------------------------')
print('Task 7')
print(len(newnum))

print('------------------------------------------------------')
print('Task 8')
newnum.append(42)
print(newnum)

print('------------------------------------------------------')
print('Task 9')
newnum.sort()
print(newnum)

print('------------------------------------------------------')
print('Task 10')
del newnum[0]
print(newnum)

print('------------------------------------------------------')
print('Task 11')
for value in newnum:
	value = value / 10
	value = value + 1
	print(value)

print('------------------------------------------------------')
print('Task 12')
print(newnum)
