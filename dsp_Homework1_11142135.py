# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:10:42 2020

@author: LENOVO
"""

from thkdsp import *


print("convolution solution 2.4 (A):")
sN=[2,-4,5,3,-1,-2,6]
hN=[1,-1,1,-1,1]
g=conv(hN,sN)
print("g", "=", g)
m=lrange(-4,6)
plot_signal(m,g,xlabel='m',ylabel='g')
plt.suptitle("Graph of 2.4(A)")



#next is solution B


print("convolution solution 2.4 (B):")
hN=[1,-2,-3,4]
sN=[1,1,0,1,1]
g=conv(sN,hN)
print("g", "=", g)
m=lrange(-5,2)
plot_signal(m,g,xlabel='m',ylabel='g')
plt.suptitle("Graph of 2.4(B)")


#next is solution C


print("convolution solution 2.4 (C):")
n=lrange(-1,4)
hN=step(n)-step(n-5)
sN=((1/4)**(-n))*(step(n+1)-step(n-4))
g=conv(sN,hN)
print("g", "=", g)
m=lrange(-2,8)
plot_signal(m,g,xlabel='m',ylabel='g')
plt.suptitle("Graph of 2.4(C)")


#next is solution D


print("convolution solution 2.4 (D):")
n=lrange(-2,5)
hN=2*(step(n+2)-step(n-3))
sN=(n/4)*(step(n)- step(n-6))
g=conv(sN,hN)
print("g", "=", g)
plot_signal(g,xlabel='m',ylabel='g')
plt.suptitle("Graph of 2.4(D)")
