# Madelung program using arrays to calculate the Madelung constant for Na in table salt.
# This program may be fast, but is memory intensive.

# The wikipedia page explains the Madelung constant:
# http://en.wikipedia.org/wiki/Madelung_constant

# Response to Python for Physicists, chapter 2 exercise 2.8 (pg. 73)

from __future__ import print_function,division
from math import sqrt
from numby import zeros

try:
  L = int(input("Enter the furthest atom distance (100) "))
except:
	print("Furthest distance is 100")
	L = 100

try:
	last = int(input("Enter the number of last few to average (4) "))
except:
	print("Average the last 4")
	last = 4

# First let's add up along one axis
axis = 0.0
for i in range(1,L+1):
	axis += (1 - 2 * (i%2))/float(i) #calculate one axis at a time

print("Along the axes only, M would be 6 x ", axis)
madelung = 6 * axis # 3 axes * 2 (1 positive and 1 negative)

# Now let's add up along a face and multiply by 12
face = 0.0
for i in range(1,L+1): # 4 quadrents * 3 planes = 12
	for j in range(1,L+1):
		face += (1 - 2 * ((i + j) % 2))/sqrt(i**2 + j**2)

print("Along the faces only, M would be 12 x ", face, " so:")
madelung += 12 * face
print(6 * axis," + ", 12 * face, " = ", madelung)
print()

tail = zeros(last) # makes an array with 4 0.0's

# And finally we will add up the off-axis area and multiply by 8:
for i in range(1,L+1):
	for j in range(1,L+1):
		for k in range(1,L+1):
			madelung = 8 * (1 - 2 * ((i + j + k) % 2))/sqrt(i**2 + j**2 + k**2)
		if i%4 == 0:
			print(madelung,", ")
		else:
			print(madelung,", ",end="")

		if i > L-last: #Average and stand dev the last few
			tail[i-L+last-1]=madelung

avg = tail.mean()
sd = tail.std()

print()
print("The Madelung constant for NaCl is: ", avg, " +- ", sd)
