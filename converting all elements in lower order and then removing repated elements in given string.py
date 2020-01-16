# converting all elements in lower order and then removing repated elements in given string
a="aAdDrpnt".lower()
new=" "
counter=0
for i in a:
    if new[counter]!=i:
        new += i
        counter += 1
print(new)
