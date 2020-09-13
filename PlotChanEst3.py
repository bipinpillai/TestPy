<<<<<<< HEAD
import matplotlib.pyplot as plt
from pathlib import Path

def GetChannel(filename):
    channelEst = []
     
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                l, _ = line.strip().split(',')
                channelEst.append(float(l))
        #print(channelEst[0])
    except:
      print("Something went wrong when reading the file")

    return channelEst


fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
plt.ion

dataFolder = Path("D:/Dev/Python/Test1/Channel/")
filename = "chanEst_87_1527434449.txt"
initChanEst = GetChannel(dataFolder / filename)
plt.plot(initChanEst, label='Initial')
plt.xlim(0, len(initChanEst))
#plt.ylim(-400, 500git diff0)
#plt.ylim(-3000, 6000)
plt.ylim(-500, 700)
plt.title('Channel Estimate')
#plt.show()

startFile = 4449 #9565 #2082 #677
lastFile = 8650 #2164 #789
ix = startFile
while ix < lastFile:
    filename = "chanEst_87_152743" + str(ix) + ".txt"
    filePath = dataFolder/filename
    if(Path(filePath).exists()):
        print(str(filePath))
        chanEst = GetChannel(filePath)
        plt.plot(chanEst, label=str(ix))
        plt.legend()
        plt.pause(0.5)
        if(ix < (lastFile - 1)):
            ax.lines.pop()    
    ix += 1
plt.waitforbuttonpress()
# plt.legend
# plt.show

