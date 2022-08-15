#!/usr/bin/env python3

import math

str1 = "Hello World"
print(str1)

for i in range(1,100):
	if i%3==0 and i%5!=0 : print("Fizz")
	elif i%5==0 and i%3!=0 : print("Buzz")
	elif (i%3 and i%5)==0 : print("FizzBuzz")
	else : print(i)
	
str2 = str1 + ", again!"
print(str2)


