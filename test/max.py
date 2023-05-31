def maximum_2(a, b):
    if a > b:
        return a
    else:
        return b


# maximum of three numbers
def maximum_3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


def maximum_4(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d


def maximum_5(a,b,c,d,e):
    if a > b and a > c and a > d and a > e:
        return a
    elif b > c and b > d and b >e:
        return b
    elif c > d and c > e:
        return c
    elif d > e:
        return d
    else:
        return e


num1 = 170
num2 = 270
num3 = 270
num4 = 230
num5 = 100
print("maximum of {0} and {1} is {2}".format(num1, num2, maximum_2(num1, num2)))
print("maximum of {0}, {1} and {2} is {3}".format(num1, num2, num3, maximum_3(num1, num2, num3)))
print("maximum of {0}, {1} ,{2} and {3} is {4}".format(num1, num2, num3, num4, maximum_4(num1, num2, num3, num4)))
print("maximum of {0}, {1} ,{2} , {3} and {4} is {5}".format(num1, num2, num3, num4, num5, maximum_5(num1, num2, num3, num4, num5)))