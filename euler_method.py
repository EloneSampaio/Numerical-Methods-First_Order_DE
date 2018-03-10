import numpy as np
from matplotlib import pyplot as plt

x0 = 0
y0 = 0
xf = 1
n = 5
deltax = (xf-x0)/(n-1)
x = np.linspace(x0,xf,n)

def f(x,y):
	return x+2*y

y = np.zeros([n])
y[0] = y0

for i in range(1,n):
	y[i] = deltax*f(x[i-1],y0) + y0
	y0 = y[i]

print("x_n\t    y_n")
for i in range(n):
	print(x[i],"\t",format(y[i],'6f'))

plt.plot(x,y,'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximation Solution with Euler's Method")
plt.show()

#http://calculuslab.deltacollege.edu/ODE/7-C-1/7-C-1-h-c.html
