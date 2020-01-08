def repeat(a):
    new=" "
    counter=0
    for i in a:
        if new[counter]!=i:
            new+=i
            counter+=1   
    print(new)
a="aAppSsfsuv".lower()
repeat(a)
