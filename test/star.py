# Python Program to print star pattern
'''
*
* *
* * *
* * * *
* * * * *
'''


def star_pattern(n):
    for i in range(1, n + 1):

        for j in range(1, i + 1):
            print("* ", end="")

        print()


n = int(input("Enter number of rows:"))
star_pattern(n)
