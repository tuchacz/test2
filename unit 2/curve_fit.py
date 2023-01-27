import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear_model(x, a, b):
    return a * x + b


x = [0, 1, 2, 3, 4, 5]
y = [15, 10, 9, 6, 2, 0]
popt, pconv = curve_fit(linear_model, x, y)

print(popt)

plt.plot(x, y, 'or')

xstart = -1
xstop = 6
increment = 0.1
xmodel = np.arange(xstart, xstop, increment)

a = popt[0]
b = popt[1]

ymodel = a * xmodel + b

plt.plot(xmodel,ymodel, 'b')
