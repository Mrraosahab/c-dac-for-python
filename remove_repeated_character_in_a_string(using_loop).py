a="aAppSsfsuv".lower()
new=" "
counter=0
for i in a:
    if new[counter]!=i:
        new+=i
        counter+=1
print(new)
