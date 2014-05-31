from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

# parameter a = P_INCREMENT * P_COUNT_MIN, P_INCREMENT * (P_COUNT_MIN + 1),
#               ..., P_INCREMENT * P_COUNT_MAX
P_COUNT_MAX = 10
P_COUNT_MIN = -P_COUNT_MAX
P_INCREMENT = 0.5

# As a,we're gonna define x. 
x_max=5
x_min = -x_max
x_increment= 0.05
x_ticks = 2*x_max/x_increment

def f(x):
	return x**2  #sample

def slope(f,a): #approximating the slope of a tangent line
	return (f(a+0.0001)-f(a))/0.0001


def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    return fig, ax


fig, ax = subplots()  # Call the local version, not plt.subplots()
ax.tick_params(which="both",bottom="off",top="off",left="off",right="off",labelbottom="off",labeltop="off",labelleft="off",labelright="off")
ax.set_ylim(-10,30) # Moving x-axis downward 
x = np.linspace(x_min,x_max,x_ticks)
y = f(x)
ax.plot(x, y, 'k-', linewidth=3)

for i in range(P_COUNT_MIN, P_COUNT_MAX+1):
	tan=x*slope(f,P_INCREMENT*i)+f(P_INCREMENT*i)-slope(f,P_INCREMENT*i)*(P_INCREMENT*i)
	ax.plot(x,tan,"b-",linewidth=1) #drawing tangent lines


ax.set_title("Envelope Theorem")
plt.show()