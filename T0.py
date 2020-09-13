fruits = ["apple", "banana", "cherry","pomegranate", "mango", "orange","strawberry"]
for item in fruits:
    if item == "banana":
        break
    print(item)
print ("done")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 


for x in range(6):
  print(x)
else:
    print("Finally finished!")