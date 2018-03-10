import numpy as np
from matplotlib import pyplot as plt

x0 = 0
y0 = 2
xf = 1
n = 11
deltax = (xf-x0)/(n-1)
x = np.linspace(x0,xf,n)
def f(x,y):
	return y-x

y = np.zeros([n])
y[0] = y0
for i in range(1,n):
	k1 = deltax*f(x[i-1],y0)
	k2 = deltax*f(x[i-1]+deltax/2,y0+k1/2)
	k3 = deltax*f(x[i-1]+deltax/2,y0+k2/2)
	k4 = deltax*f(x[i-1]+deltax,y0+k3)
	y[i] =  y0 + (k1 + 2*k2 + 2*k3 + k4)/6
	y0 = y[i]

print("x_n\t    y_n")
for i in range(n):
	print(x[i],"\t",format(y[i],'6f'))

plt.plot(x,y,'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximation Solution with Runge-Kutta Method")
plt.show()

#table 19.3
