import matplotlib.pyplot as plt
import sys
import glob
import errno
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
path = 'C:\Channel\*.txt'

x =[]
y=[]
z = []
row = []
files = glob.glob(path)
i = 1;
for name in files:
    for line in open(name,'r'):
        line = line.replace(',','')
        line = line.replace('\n','')
        line = line.replace(' ','')
        x.append(float(line));
    y.append(i);
    z.append(i); 
    break;

i = i +1;    
print(x)
print(y)
print(z)
    
ax.scatter(z, y, x, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
