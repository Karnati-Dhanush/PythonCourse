# Write a program to print first n fibonacci numbers

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


n_terms = 12
if n_terms <= 0:
    print("enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibo(i))
