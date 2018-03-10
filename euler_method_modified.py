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
py = np.zeros([n])
py[0] = None

for i in range(1,n):
	py[i] = deltax*f(x[i-1],y[i-1]) + y[i-1]
	y[i] = deltax/2*( f(x[i],py[i]) + f(x[i-1],y[i-1]) ) + y[i-1]
print("x_n\t   py_n\t           y_n")
for i in range(n):
	print (x[i],"\t",format(py[i],'6f'),"\t",format(y[i],'6f'))

plt.plot(x,y,'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximation Solution with Modified Euler's Method")
plt.show()

#table 19-1
