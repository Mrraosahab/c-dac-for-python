#capatiliazation each first element of given string using for loop
a="hey i'm new here"
b=a.split()
for i in b:
    n=[i[0].upper()+i[1:]]
    n=' '.join(n)
    print(n,end=" ")
