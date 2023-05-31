# Write a program to reverse a number
num = 1234
rev_n = 0

while num != 0:
    digit = num % 10
    rev_n = rev_n * 10 + digit
    num //= 10

print("Reverse of a Number: " + str(rev_n))



