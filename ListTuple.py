a=input("Enter comma separated integers: ")
print("Input string: ",a)
list = a.split(",")
li = []
for i in list:
    li.append(i)
print("list : ", li)