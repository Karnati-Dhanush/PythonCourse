saree_price = 10000
festival = "newyear"
discount = 0
if festival == "dasara":
    discount = 20
elif festival == "diwali":
    discount = 10
elif festival == "newyear":
    discount = 2
else:
    discount = 0
discount_value = (discount * saree_price) / 100
net_price = saree_price - discount_value
print("the saree price is %i" % saree_price)
print("the festival is %r" % festival)
print("the discount is %i" % discount)
print("the discount amount is %i" % discount_value)
print("the net price of saree is %i" % net_price)
