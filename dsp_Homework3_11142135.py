# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:10:02 2020

@author: LENOVO
"""

from thkdsp import *
from numpy import *
def dtft(n, s, F):
    M = len(F)
    N = len(s)
    S = s.dot(exp(-2j*pi * n.reshape(N, 1).dot(F.reshape(1, M))))
    return S


print("solution of PROBLEM 4.5:")
#SOLUTION A

n = lrange(-10,11,1)
s = (0.6)**abs(n) * (step(n+10) - step(n-11))
F = lrange(-0.5, 0.5, 1000)
S = dtft(n, s, F)
MaG = sqrt(S.real**2 + S.imag**2)
AngL = angle(S)
plot_signal(n, s, 'n','s')
plt.suptitle("Solution for 4.5(A)")
plot_signal(F, MaG,'f','s')
plot_signal(F, AngL, 'f', 's')
#The angle is changing fast within the phase interval of [−π,π] as it goes closer to zero.
 

#SOLUTION B

n = lrange(-1,25,1)
s = n*(0.9)**n * (step(n) - step(n-21))
F = lrange(-0.5, 0.5, 1000)
S = dtft(n, s, F)
MaG = sqrt(S.real**2 + S.imag**2)
AngL = angle(S)
plot_signal(n, s, 'n','s')
plt.suptitle("Solution for 4.5(B)")
plot_signal(F, MaG,'f','s')
plot_signal(F, AngL, 'f', 's')


#SOLUTION C

n = lrange(0,51,1)
s = (cos(0.5*pi*n) + 1j*sin(0.5*pi*n)) * (step(n) - step(n-51))
F = lrange(-0.5, 0.5, 1000)
S = dtft(n, s, F)
MaG = sqrt(S.real**2 + S.imag**2)
AngL = angle(S)
plot_signal(n, s, 'n','s')
plt.suptitle("Solution for 4.5(C)")
plot_signal(F, MaG,'f','s')
plot_signal(F, AngL, 'f', 's')
#from the magnitude plot,the maximum amplitude is at 0.25 and equals to 50 shows the energy of different frequency components.


#SOLUTION D

n = array([0, 1, 2, 3, 4, 5, 6, 7])
s = array([4, 3, 2, 1, 1, 2, 3, 4])
F = lrange(-0.5, 0.5, 1000)
S = dtft(n, s, F)
MaG = sqrt(S.real**2 + S.imag**2)
AngL = angle(S)
plot_signal(n, s, 'n','s')
plt.suptitle("Solution for 4.5(D)")
plot_signal(F, MaG,'f','s')
plot_signal(F, AngL, 'f', 's')
# From the angle plot,The angle is (mapping the phase back to the interval [−π,π]) and shows the different shift within the phase interval.

#SOLUTION E

n = array([0, 1, 2, 3, 4, 5, 6, 7])
s = array([4, 3, 2, 1, -1, -2, -3, -4])
F = lrange(-0.5, 0.5, 1000)
S = dtft(n, s, F)
MaG = sqrt(S.real**2 + S.imag**2)
AngL = angle(S)
plot_signal(n, s, 'n','s')
plt.suptitle("Solution for 4.5(E)")
plot_signal(F, MaG,'f','s')
plot_signal(F, AngL, 'f', 's')
# From the angle plot,The angle is (mapping the phase back to the interval [−π,π]) and shows the different shift within the phase interval.