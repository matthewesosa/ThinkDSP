# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:27:36 2020

@author: Godfrey
"""

from thkdsp import *
import numpy as np
from thkdsp.ztransform import residue, residuez, zplane
from numpy import poly, array
from scipy.signal import lfilter
from matplotlib import *
from math import *


print("Solution to Problem 5.8")

#solution 5.8

zn1 = 0.8
zn2 = 0.1
zp1 = -1
zp2 = -0.9

x = (5/4)*poly([zn1, zn2])
print('x=',x)
y = poly([zp1, zp1])
print('y=',y)

r, p, c = residue(x, y)
print('r=',r)
print('p=',p)
print('c=',c)

ih = (5/4)*poly([0])
jh = poly([zp1, zp2])
r, p, c = residue(ih, jh)

n = lrange(-5, 20)
hn = c*delta(n)

for k in range(0, len(p)):
    hn = hn + step(n-1)*(r[k]*p[k]**(n-1))
hn = np.real(hn)

fig, ax = plot_signal(n, hn, xlabel="n", ylabel="h")
fig.suptitle("Solution 5.8 through PFE of h(z)")

gn = lfilter(y, x, np.sin(2*pi*n/4)*step(n))

fig, ax = plot_signal(n, gn, xlabel="n", ylabel="g")
fig.suptitle("Solution 5.8, with lfilter g[n]")


print("Solution to Problem 5.9")

#solution 5.9(a)






#the impulse response within the range -5 <= n <= 20

zn1 = -1
zn2 = -0.7
zp1 = 0.9
zp2 = 0.8
y = (0.25)*poly([zn1, zn2])
print('y=',y)
x = poly([zp1, zp2])
print('x=',x)
n = lrange(-5, 20)
c = 1/4
hX = c*(delta(n) + 2*delta(n-1) + delta(n-2))

fig, ax = plot_signal(n, hX, xlabel="n", ylabel="h")
fig.suptitle("Solution 5.9(a), of IMPULSE RESPONSE" )









#solution 5.9B

#the impulse response within the range -5 <= n <= 20

zn1 = 0
zn2 = -0.5
zp1 = -1
zp2 = 0



Y = poly([zn1, zn2])
X = poly([zp1, zp2])


r, p, c = residue(Y, X)
n = lrange(-5, 20)
hY = c*delta(n)
for k in range(0, len(p)):
    hY = hY + step(n-1)*(r[k]*p[k]**(n-1))
    
fig, ax = plot_signal(n, hY, xlabel="n", ylabel="h")
fig.suptitle("Solution 5.9(b), of IMPULSE RESPONSE")









#solution 5.9C

#the impulse response within the range -5 <= n <= 20

zn1 = 0
zp1 = 1.2
Y = 2*poly([zn1])
X = poly([zp1])
r, p, c = residue(Y, X)

n = lrange(-5, 20)
hZ = c*delta(n)
for k in range(0, len(p)):
    hZ = hZ + step(n-1)*(r[k]*p[k]**(n-1))
    
fig, ax = plot_signal(n, hZ, xlabel="n", ylabel="h")
fig.suptitle("Solution 5.9(c), of IMPULSE RESPONSE")











