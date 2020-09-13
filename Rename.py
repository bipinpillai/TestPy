import os

print(os.getcwd())
print(os.listdir())

myFiles = list(os.listdir())
cnt = 0
for name in myFiles:
    if(name.startswith("T")):
        os.rename(name, f"T{cnt}.py")
        cnt+=1

print(os.listdir())