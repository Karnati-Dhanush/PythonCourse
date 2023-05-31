'''
Write a Python program to filter positive numbers from a list.
'''
number = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",number)
new_list = list(filter(lambda x: x >0, number))
print("Positive numbers in the said list: ",new_list)
