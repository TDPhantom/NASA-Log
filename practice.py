import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 1, 2, 3])
ypoints = np.array([3, 8, 1, 10])
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
z = np.array([50,100,150,200])

plt.subplot(2, 1, 2)
plt.plot(xpoints, ypoints, 'X:r')

plt.subplot(2, 2, 1)
plt.plot(x,y)

plt.subplot(2,2,3)
plt.plot(z)

plt.grid()
plt.show()
