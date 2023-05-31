# Write a program to reverse words
'''
Example :
Input - My Name is Anushka
Ouput - Anushka is My Name
'''

my_string = "I Love India"
words = my_string.split()
print(words)
for i in range(2, -1, -1):
    print(words[i])

