from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

# parameter a = P_INCREMENT * P_COUNT_MIN, P_INCREMENT * (P_COUNT_MIN + 1),
#               ..., P_INCREMENT * P_COUNT_MAX
P_COUNT_MAX = 10
P_COUNT_MIN = -P_COUNT_MAX
P_INCREMENT = 0.5


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

x = np.linspace(-5, 5, 200)
y = f(x)
ax.plot(x, y, 'b-', linewidth=2)

t=[]
for i in range(P_COUNT_MIN, P_COUNT_MAX+1):
    t.append(P_INCREMENT*i)  # Constants defined at the beginning

for i in t:
	tan=x*slope(f,i)+f(i)-slope(f,i)*i
	ax.plot(x,tan,"b-",linewidth=1) #drawing tangent lines

plt.show()
