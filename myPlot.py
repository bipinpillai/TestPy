import matplotlib.pyplot as plt
import numpy as np

def myPlot(minV, maxV, incV):
    #x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    x = np.linspace(minV, incV, maxV)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.show()                   # Display the plot

#myPlot(0, 100, 20)
#myPlot(0, 1000, 50)