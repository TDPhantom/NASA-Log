import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 8, 1, 10])
ypoints = np.array([0, 1, 2, 3])
zpoints = np.array([4, 7 ,9 ,10,25])

plt.plot(xpoints, ypoints, 'X:r')
plt.subplot(2, 1, 1)


plt.xlabel("Fornite Players")
plt.ylabel('Minecraft Players')



plt.grid()
plt.show()
