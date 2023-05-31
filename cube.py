'''
 Write a Python function that takes a positive integer and returns the sum of the cube
 of all positive integers smaller than the specified number.
Example - if the input is 5, then the 4*4*4 + 3*3*3 + 2*2*2 + 1*1*1 = 100 is the answer
'''
def sum_of_cubes(n):
   if n < 0:
       raise ValueError('n must be positive number!')
   return n*n*(n*n-2*n+1)/4
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(4))
