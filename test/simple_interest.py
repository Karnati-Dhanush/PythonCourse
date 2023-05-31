# Write a function which takes P is the principal amount, T
# is the time, and R is the rate and calcualates Compound Interest
# formula=p*t*r/100
def simple_interest(p, t, r):
    interest = (p * t * r) / 100
    return interest


# driver code
p = 10000
t = 6
r = 10
result = simple_interest(p, t, r)
print("The interest value for Rs {0} time for {1} year rate of interest {2}% is {3}".format(p, t, r, result))
