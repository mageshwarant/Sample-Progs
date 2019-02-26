# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:14:34 2019

@author: hp
"""



#def add(add1,add2):
#    sum = add1+add2
#    return sum
def add(*args):
    sum =0
    for i in args:
        sum = sum+i
    return sum

sum =add(1,1,1,1,1,1,1,1,1)
print(sum)

import math
print(math.factorial(5))

#from functools import reduce
#lister =[1,2,3,4,5,6,7,8,9,10]
#
#x= filter(lambda x:x%2==0 , lister)
#
#print()

import glob

x= glob.glob("E:\\Magesh\\Camera\\*.jpg")

print(len(x))