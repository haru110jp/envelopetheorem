import matplotlib.pyplot as plt
import numpy as np
from __future__ import division



def f(x):
	return x**2  #sample

def slope(f,a):
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
x = np.linspace(-5, 5, 200)
y = f(x)
ax.plot(x, y, 'b-', linewidth=2)

t=[]
for i in range(-10,11):
	t.append(0.5*i)
	
for i in t:
	tan=x*slope(f,i)+f(i)-slope(f,i)*i
	ax.plot(x,tan,"b-",linewidth=1)
	
plt.show()
