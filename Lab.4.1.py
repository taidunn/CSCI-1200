#Tai Dunn
#CSCI 1200A
#Lab Exercise 4.1
#02/06/2019
#lab_4_1.py

numbers = list(range(0, 1000000))

print(len(numbers))

print(min(numbers))

print(max(numbers))

print(sum(numbers))


newnum=numbers[100:125]
print(newnum)

newnum.append(42)
print(newnum)

for value in newnum:
	value = value / 10
	value = value + 1
	print(value)

final = []
for value in newnum:
	final.append(value / 10 + 1)
print(final)
