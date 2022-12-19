import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 1, 2, 3])
ypoints = np.array([3, 8, 1, 10])
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.plot(xpoints, ypoints, 'X:r')
plt.subplot(2, 1, 1)

plt.subplot(2, 1, 2)
plt.plot(x,y)


plt.grid()
plt.show()
