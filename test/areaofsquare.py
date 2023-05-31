# Write a function which takes A
# formula=A*A
def area_square(a):
    area = (a * a)
    return area


# driver code
a = 9
result = area_square(a)
print("The area of square for side {0} is {1}".format(a, result))
