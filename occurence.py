'''
Write a Python program to count the number of occurrences of a specific character in a string.
'''
count = 0
string = "Karnati Dhanush Reddy"
char = "a"
for i in string:
    if i == char:
        count += 1
print(count)
