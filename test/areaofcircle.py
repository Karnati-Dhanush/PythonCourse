# Write a function to calculate the area of a circle. Program should
# take the radius as input program


# Write a function which takes R
# formula=R*R
def area_circle(r):
    area = (3.14 * r * r)
    return area


# driver code
r = 8
result = area_circle(r)
print("The area of circle for radius {0} is {1}".format(r, result))
