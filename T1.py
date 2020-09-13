import os
from pprint import pprint as pp

x = range(1,5)
print(x)
y = list(zip(range(1,5), "abcdefgh"[:3]))
print(y)

rows , seats = (range(1,5), "abcdefgh"[:3])
z = [{s:str(r)+str(s) for s in seats} for r in rows]
pp(z)

z1 = [{s:f"{r}{s}" for s in seats} for r in rows]
pp(z1)

path = "D:/Dev/Python/Test1/Channel/"
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
pp(text_files)