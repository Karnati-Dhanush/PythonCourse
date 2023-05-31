# Write a program to check if the given number is fibonacci number

n = int(input("Enter the number: "))
c = 0
a = 1
b = 1
if n == 0 or n == 1:
    print("entered number is a fibonacci number")
else:
    while c < n:
        c = a + b
        b = a
        a = c
    if c == n:
        print("Yes,the entered number is a fibonacci number")
    else:
        print("No,the entered number is not a fibonacci number")
