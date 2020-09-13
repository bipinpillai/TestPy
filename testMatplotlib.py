from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1, 200, 100)
y=np.arange(0, 50, 1)
print(y)
#plt.plot([1, 2, 3, 4])
plt.plot(y)
plt.ylabel('some numbers')
plt.show()

print(np.version.version)

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')
print(len(xline))
print(len(yline))
print(len(zline))

# Data for three-dimensional scattered points
zdata = 15 * np.random.rand(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
plt.show()
print(len(xdata))
print(len(ydata))
print(len(zdata))