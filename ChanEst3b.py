from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import glob
import numpy as np

x = []
y = []
z = []

filesRead = 0
for name in glob.glob('D:\Dev\Python\Test1\ChannelGOM\*.txt'): 
    samplePt = 0
    with open(name,'r') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.strip(',')
            z.append(float(line))
            x.append(samplePt)
            y.append(filesRead)
            samplePt += 1
    filesRead += 1
    
fig = plt.figure()
ax = plt.axes(projection='3d')    
#ax.plot3D(x, y, z, 'blue')
#ax.scatter3D(x, y, z, c='r', marker='.')
ax.plot_trisurf(x, y, z, cmap=plt.cm.jet, linewidth=0.01)
ax.set_xlabel('Channel samples')
ax.set_ylabel('Time')
ax.set_zlabel('Channel estimate')
plt.show()

