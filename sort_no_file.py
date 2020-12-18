# print numbers is a file and then print sort a numberes in a file
# num.txt
# 3 9 10 5 8 
import os
filename = 'num.txt' 
with open(filename, "r") as f_obj: 
    print(f_obj.read())   # print each line
    f_obj.close()
f_obj = open(filename, "r")
x = f_obj.read().splitlines()
print(x)   # x is now a list and it print a list of string
for i in range(0, len(x)): 
     x[i] = int(float(x[i]))
x.sort()
print(x)   # x now is list but digit numbers 
