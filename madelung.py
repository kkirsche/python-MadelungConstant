# Madelung program using arrays to calculate the Madelung constant for Na in table salt.
# This program may be fast, but is memory intensive.

# The wikipedia page explains the Madelung constant:
# http://en.wikipedia.org/wiki/Madelung_constant

# Response to Python for Physicists, chapter 2 exercise 2.8 (pg. 73)

from numpy import indices,sqrt

try:
    L = int(input("Enter the furthest atom distance (100) "))
except:
	print ("Furthest distance is 100")
	L = 100

L = L + 1 # This is because of zero indexing.

I = indices([L,L,L])[0,:,:,:] # x-axis
J = indices([L,L,L])[1,:,:,:] # y-axis
K = indices([L,L,L])[2,:,:,:] # z-axis

I[0,0,0] = 100 # to ensure that M[0,0,0] is not infinity

M = (1 - 2 * ((I+J+K)%2))/sqrt(I**2+J**2+K**2)

axes = M[0,0,1:].sum() + M[0,1:,0].sum() + M[1:,0,0].sum() # Calculate all values of each point on the axes.
faces = M[0,1:,1:].sum() + M[1:,0,1:].sum() + M[1:,1:,0].sum() # Calculate the planes
off_axis = M[1:,1:,1:].sum() # Calculate all the other points

madelung = (2 * axes) + (4 * faces) + (8 * off_axis)

print("The madelung constant for NaCl is: ", madelung) 
