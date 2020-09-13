import matplotlib.pyplot as plt
from pathlib import Path

dataFolder = Path("C:/Work/MxR/ChannelEstimateFiles/")

def GetChannel(filename):
    channelEst = []
     
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                l, na = line.strip().split(',')
                channelEst.append(float(l))
        print(channelEst[0])
    except:
      print("Something went wrong when reading the file")

    return channelEst



plt.figure(1)
maxRow = 5
maxCol = 3
pltIndex = 1
filename = "chanEstPreamble_116_1553888676.txt"
chanEst = GetChannel(dataFolder / filename)
ax1 = plt.subplot(maxRow, maxCol, pltIndex)
#plt.title(filename)
plt.xlim([0, len(chanEst)])
plt.plot(chanEst)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888677.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888678.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888679.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888680.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

# 2nd column
pltIndex=2
chanEst = GetChannel(dataFolder / "chanEst_30_1553888690.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888700.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888710.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888720.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888730.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3


# 3rd column
pltIndex=3
chanEst = GetChannel(dataFolder / "chanEst_30_1553888740.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888750.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888760.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888770.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

chanEst = GetChannel(dataFolder / "chanEst_30_1553888789.txt")
ax2 = plt.subplot(maxRow, maxCol, pltIndex, sharex = ax1, sharey = ax1)
plt.plot(chanEst)
plt.setp(ax2.get_xticklabels(), visible=False)
pltIndex+=3

#plt.tight_layout()
plt.show()


plt.figure(2)
filename = "chanEstPreamble_116_1553888676.txt"
chanEst = GetChannel(dataFolder / filename)
plt.plot(chanEst, label='Initial')

filename = "chanEst_30_1553888677.txt"
chanEst = GetChannel(dataFolder / filename)
plt.plot(chanEst, label='Initial+1')

filename = "chanEst_30_1553888678.txt"
chanEst = GetChannel(dataFolder / filename)
plt.plot(chanEst, label='Initial+2')

filename = "chanEst_30_1553888679.txt"
chanEst = GetChannel(dataFolder / filename)
plt.plot(chanEst, label='Initial+3')

# filename = "chanEst_30_1553888680.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+4')

# filename = "chanEst_30_1553888681.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+5')

# filename = "chanEst_30_1553888682.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+6')

# filename = "chanEst_30_1553888683.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+7')

# filename = "chanEst_30_1553888684.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+8')

# filename = "chanEst_30_1553888685.txt"
# chanEst = GetChannel(dataFolder / filename)
# plt.plot(chanEst, label='Initial+9')


plt.legend()
plt.show()
