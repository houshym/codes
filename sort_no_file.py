# sort a numberes in a file
import os
import math

filename = 'num.txt' 

with open(filename, "r") as f_obj: 
    # for line in f_obj: 
    #     print(line.rstrip
    #x = f_obj.readlines()
    print(f_obj.read())
    f_obj.close()
f_obj = open(filename, "r")
x = f_obj.read().splitlines()
print(x)
for i in range(0, len(x)): 
     x[i] = int(float(x[i]))
x.sort()
print(x)
