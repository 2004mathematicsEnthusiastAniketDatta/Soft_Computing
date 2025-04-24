import matplotlib.pyplot as plt
import numpy as np
c=float(input("Enter the mean:"))
var=float(input("Enter the variance:"))
sig=np.sqrt(var)
x_axis=(np.arange(-10,10,0.001))
y_axis = np.exp(-((x_axis - c) ** 2) / (2 * var))
plt.plot(x_axis, y_axis)
plt.title(f"Gaussian Function (Mean={c}, Variance={var})")
plt.show()
