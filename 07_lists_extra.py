#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code



# -------------------- ZIP FUNCTION --------------------

# The zip() function lets you loop through iterables in parallel
# The zip() ends when the first container ends

names = ('Nigel', 'David', 'Derek') # tuple
ages = [52, 53, 49, 1, 2, 3]        # list

for (name, age) in zip(names, ages):
	print(name, age)


# -------------------- LIST COMPREHENSION --------------------

# Consider the following initialization code:

data = []
for i in range(10): data.append(0) #adds zero (append) 10 times (the range)
print(data)


# You can write this more succinctly with the * operator

data = [0] * 10 #writes 0 (inside brackets) 10 times (number after the *)
print(data)


# Another alternative is list comprehension

data = [0 for i in range(10)] #gives 0 for every i in the range of 10
print(data)


# List comprehension gets even more interesting...
# Here's a slightly more complex initialization


squares = []
for i in range(10):
	squares.append(i ** 2) # ** is exponential operator therefore squaring because exponent of 2
print(squares) #starts with 0 and goes to 9 and squares each one


# List comprehension turns 3 lines into 1

squares = [i ** 2 for i in range(10)]
print(squares)

# You can also include a conditional
# First the longer syntax


square3 = []
for i in range(10):
	if i % 3 == 0: #if i is divisible by three (when divided by three the remainder is zero), then square the value
		square3.append(i ** 2)
print(square3)

# Now list comprehension

square3 = [i ** 2 for i in range(10) if i % 3 == 0]
print(square3)

