def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


x = 5
y = fact(x)
print("the factorial of {0} is {1}".format(x, y))
