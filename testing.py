'''
Write a Python program to test whether all numbers in a list are greater than a certain number
'''
list = [1, 7, 5, 6, 3, 8]
k = 2
print("The list : " + str(list))
count = 0
for i in list:
	if i > k:
		count = count + 1
print("The numbers greater than 2 : " + str(count))
