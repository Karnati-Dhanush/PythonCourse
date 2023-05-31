# Print only the words which are of even length
# Example :
# Input : My Name is Devi Reddy
# Ouput : Name Devi
# (since Name lenght is 4 which is even, and Devi Length is 4 which is even)
n = " My Name is Devi Reddy"
s = n.split(" ")
for i in s:
  if len(i) % 4 == 0:
    print(i)