import myPlot

myPlot.myPlot(0, 100, 20)

cnt=0
try:
    logfile = open("C:\Dev\Python\PythonTests\TestLog.log", "r")
    print("Enter search string: ")
    searchString = input()

    for line in logfile:
    #    if line.find('TiWorker') >= 0:
        if searchString in line:
            cnt+=1
            print(line)
except:
      print("Something went wrong when writing to the file")
finally:
    logfile.close()
    
print("Number of instances of " + searchString + "= " + str(cnt))
