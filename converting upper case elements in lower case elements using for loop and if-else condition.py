# converting upper case elements in lower case elements using for loop and if-else condition
A="MangOerP"
B=''
for i in A:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        B=B+i
    else:
        c=ord(i)
        d=c+32
        B=B+chr(d)
print(B) 
