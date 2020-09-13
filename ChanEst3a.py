from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import glob
import numpy as np

x = []
y = []
z = []
files = glob.glob('D:\Dev\Python\Test1\Channel\*.txt')

filesRead = 0
for name in files:
    samplePt = 0
    for line in open(name,'r'):
        line = line.strip()
        line = line.strip(',')
        z.append(float(line))
        x.append(samplePt)
        y.append(filesRead)
        samplePt += 1
    filesRead += 1
    
# We are going to do 20 plots, for 20 different angles
#for angle in range(70,210,2):
fig = plt.figure()
#ax = plt.axes(projection='3d')    
ax = fig.gca(projection='3d')
#ax.plot3D(x, y, z, 'blue')
#ax.scatter3D(x, y, z, c='r', marker='.')
ax.plot_trisurf(x, y, z, cmap=plt.cm.jet, linewidth=0.01)
#ax.plot_trisurf(x, y, z, cmap=plt.cm.viridis, linewidth=0.2)
ax.set_xlabel('Channel samples')
ax.set_ylabel('Time')
ax.set_zlabel('Channel estimate')
plt.show()

    # # Set the angle of the camera
    # ax.view_init(30,angle)

    # filename='./Animation/ChEst3D'+str(angle)+'.png'
    # plt.savefig(filename, dpi=96)
    # plt.gca()
