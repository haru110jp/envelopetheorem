from numpy import sin,linspace,power
from pylab import plot,show
from __future__ import division


def f(x): # sample function
   return x**3

x = linspace(0,10,150)
y = f(x)

def linapprox(f,a,b,n,x2):
    length_of_interval = b - a
    num_subintervals = n - 1
    step = length_of_interval / num_subintervals  
    point = a
    while point < x2:
        point = point + step
    u, v = point - step, point
    
    return (x2 - u) * (f(v) - f(u)) / (v - u)

tan =x*linapprox(f,0,10,100,4)+f(x2)

# plot of the function and the tangent
plot(x,y,'b',x,tan,'--r')
show()
