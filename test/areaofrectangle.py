# Write a function which takes L, B
# formula=L*B
def area_rectangle(l, b):
    area = (l * b)
    return area


#driver code
l = 6
b = 5
result = area_rectangle(l, b)
print("The area of rectangle for length {0} and breadth {1} is {2}".format(l, b, result))
