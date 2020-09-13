import matplotlib.pyplot as plt
from pathlib import Path

def GetChannel(filename):
    channelEst = []
     
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                l, _ = line.strip().split(',')
                channelEst.append(float(l))
        print(channelEst[0])
    except:
      print("Something went wrong when reading the file")

    return channelEst


fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
plt.ion

dataFolder = Path("C:/Work/MxR/NorwayChannelEstimatesLF300AfterStrokeFix/")
filename = "chanEstPreamble_87_1554609565.txt"
initChanEst = GetChannel(dataFolder / filename)
plt.plot(initChanEst, label='Initial')
plt.xlim(0, len(initChanEst))
#plt.ylim(-400, 500)
#plt.ylim(-3000, 600)
plt.ylim(-200, 200)
plt.title('Channel Estimate (LF300) Norway 4th run')

startFile = 9565 #2082 #677
lastFile = 9768 #2164 #789
ix = startFile
while ix < lastFile:
    filename = "chanEst_40_155460" + str(ix) + ".txt"
    chanEst = GetChannel(dataFolder / filename)
    plt.plot(chanEst, label=str(ix))
    ix += 1
    plt.legend()
    plt.pause(0.5)
    ax.lines.pop()    

plt.waitforbuttonpress()
# plt.legend
# plt.show

