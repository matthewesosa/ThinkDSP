# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:10:30 2020

@author: Akuba Godfrey Ojimah
"""

from thkdsp import *
from math import *
from scipy.interpolate import interp1d
from numpy import *
import matplotlib.pyplot as plt
from thkdsp.interpolation import ideal_interpolation



#slution for 3.4
# T=0.01
print("solution of 3.4 :")
T=0.01
n= lrange(-1,1,(1/T))
sn = sin(2*pi*10*n)
plot_signal(n,sn,'n','s')
plt.suptitle("Solution of 3.4(A), Graph of T = 0.01")

# T = 0.05
T= 0.05
n = lrange(-1,1,(1/T))
sn = sin(2*pi*10*n)
plot_signal(n,sn,'n','s')
plt.suptitle('Solution of 3.4(A), Graph of T = 0.05')

# T=0.1
T=0.1
n= lrange(-1,1,(1/T))
sn = sin(2*pi*10*n)
plot_signal(n,sn,'n','s')
plt.suptitle("Solution of 3.4(A), Graph of T = 0.1")


#ideal interpolation (Use Dt = 0.001)

#T=0.01
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,100) 
sn = sin(2*pi*10*n)
sr = ideal_interpolation(n, sn, t)
plot_signal(t,sr,'t','sr')
plt.suptitle("Solution of 3.4(B), Graph of T = 0.01")


#T=0.05
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20) 
sn = sin(2*pi*10*n)
sr = ideal_interpolation(n, sn, t)
plot_signal(t,sr,'t','sr')
plt.suptitle("Solution of 3.4(B), Graph of T = 0.05")


#T=0.01
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,10) 
sn = sin(2*pi*10*n)
sr = ideal_interpolation(n, sn, t)
plot_signal(t,sr,'t','sr')
plt.suptitle("Solution of 3.4(B), Graph of T = 0.1")




#cubic spline interpolation

#T=0.01
def s(t):
    return sin(2*pi*10*t)
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.01
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
plot_signal(t, s_sp,'t','s_sp' )
plt.suptitle("Solution of 3.4(C), Graph of T = 0.01")


#T=0.05
def s(t):
    return sin(2*pi*10*t)
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
plot_signal(t, s_sp,'t','s_sp' )
plt.suptitle("Solution of 3.4(C), Graph of T = 0.05")


#T=0.1
def s(t):
    return sin(2*pi*10*t)
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.1
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
plot_signal(t, s_sp,'t','s_sp' )
plt.suptitle("Solution of 3.4(C), Graph of T = 0.1")
#3.4(D)
'''from observation the graphs contain the continous and discrete time signals and it changes depending on the time intervals given. and also for the ideal interpolation and cubic spine interpolation to detemine the frequency.'''

print("solution of 3.5 :")
#####QUESTION 3.5
# T = 0.05 and Ɵ = 0
t = lrange(-1,1,20)
n = lrange(-1,1,20)
st = cos(2*pi*10*t)
sn = cos(2*pi*10*n)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, st, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(A), Graph of T = 0.05 and Ɵ = 0")

# T = 0.05 and Ɵ = pi/6
t = lrange(-1,1,20)
n = lrange(-1,1,20)
st = cos(2*pi*10*t + (pi/6))
sn = cos(2*pi*10*n + (pi/6))
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, st, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(A), Graph of T = 0.05 and Ɵ = pi/6")

# T = 0.05 and Ɵ = pi/4
t = lrange(-1,1,20)
n = lrange(-1,1,20)
st = cos(2*pi*10*t + (pi/4))
sn = cos(2*pi*10*n + (pi/4))
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, st, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(A), Graph of T = 0.05 and Ɵ = pi/4")

# T = 0.05 and Ɵ = pi/3
t = lrange(-1,1,20)
n = lrange(-1,1,20)
st = cos(2*pi*10*t + (pi/3))
sn = cos(2*pi*10*n + (pi/3))
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, st, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(A), Graph of T = 0.05 and Ɵ = pi/3")

# T = 0.05 and Ɵ = pi/2
t = lrange(-1,1,20)
n = lrange(-1,1,20)
st = cos(2*pi*10*t + (pi/2))
sn = cos(2*pi*10*n + (pi/2))
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, st, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(A), Graph of T = 0.05 and Ɵ = pi/2")


#ideal interpolation (Use Dt = 0:001)


# T = 0.05 and Ɵ = 0
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20)
sn = cos(2*pi*10*n)
sr = ideal_interpolation(n, sn, t)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, sr, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(B), Graph of T = 0.05 and Ɵ = 0")

# T = 0.05 and Ɵ = pi/6
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20)
sn = cos(2*pi*10*n + (pi/6))
sr = ideal_interpolation(n, sn, t)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, sr, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(B), Graph of T = 0.05 and Ɵ = pi/6")

#T = 0.05 and Ɵ = pi/4
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20)
sn = cos(2*pi*10*n + (pi/4))
sr = ideal_interpolation(n, sn, t)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, sr, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(B), Graph of T = 0.05 and Ɵ = pi/4")

#T = 0.05 and Ɵ = pi/3
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20)
sn = cos(2*pi*10*n + (pi/3))
sr = ideal_interpolation(n, sn, t)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, sr, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(B), Graph of T = 0.05 and Ɵ = pi/3")

# T = 0.05 and Ɵ = pi/2
m = 1/0.001
t = lrange(-1,1,m)
n = lrange(-1,1,20)
sn = cos(2*pi*10*n + (pi/2))
sr = ideal_interpolation(n, sn, t)
fig, ax = plot_signal(n, sn,'n', 'sn')
fig, ax = plot_signal(t, sr, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(B), Graph of T = 0.05 and Ɵ = pi/2")


#cubic spline interpolation

#T=0.05 and Ɵ = 0
def s(t):
    return cos(2*pi*10*t)
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
fig, ax = plot_signal(nT, sn,'n', 'sn')
fig, ax = plot_signal(t, s_sp, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(C), Graph of T = 0.05 and Ɵ = 0")


# T=0.05 and Ɵ = pi/6
def s(t):
    return cos(2*pi*10*t + (pi/6))
t = lrange(-1, 1, 1000) 
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
fig, ax = plot_signal(nT, sn,'n', 'sn')
fig, ax = plot_signal(t, s_sp, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(C), Graph of T = 0.05 and Ɵ = pi/6")

#T=0.05 and Ɵ = pi/4
def s(t):
    return cos(2*pi*10*t + (pi/4))
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
fig, ax = plot_signal(nT, sn,'n', 'sn')
fig, ax = plot_signal(t, s_sp, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(C), Graph of T = 0.05 and Ɵ = pi/4")


# T=0.05 and Ɵ = pi/3
def s(t):
    return cos(2*pi*10*t + (pi/3))
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
fig, ax = plot_signal(nT, sn,'n', 'sn')
fig, ax = plot_signal(t, s_sp, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(C), Graph of T = 0.05 and Ɵ = pi/3")


#T=0.05 and Ɵ = pi/2
def s(t):
    return cos(2*pi*10*t + (pi/2))
t = lrange(-1, 1, 1000)
# sampling period
tmax = 1
T = 0.05
r = 1/T
nmax = int(tmax/T)
n = lrange(-nmax, nmax)
# sampling points
nT = n*T
# samples = DT signal
sn = s(nT)
spline = interp1d(nT, s(nT), kind='cubic')
s_sp = spline(t)
fig, ax = plot_signal(nT, sn,'n', 'sn')
fig, ax = plot_signal(t, s_sp, figure=fig, axes=ax)
plt.suptitle("Solution of 3.5(C), Graph of T = 0.05 and Ɵ = pi/2")



##3.5(D)
'''The amplitude is given by cos Ɵ and the resulting amplitude has an amplitude that depend on the phase of the signal. Therefore, the sampling and reconstrucion of this signal is changing the signal to it original form without losing any information on the frequency. '''