a = (1,2,3,3,4,5,6,8,9)
print(a)
#index operation
print(a.index(4))
#count operation for a element
print(a.count(3))
# addition off two tuples
b = ("pradeep", 1997, "jaipur")
c = a+b
print(c)
#check length of tuple
print(len(a))
print(len(b))
# multiplication of tuple
print(a*4)
print(b*3)
# check  elements in a tuple
print(3 in a)
print("pradeep" in b)
#print maximum value from tuple
print(max(a))
# this above function is useful only for int
#when we apply this, it will give the error, for example see bellow syntax
#print(max(b))
# to check minimum value in tuple
print(min(a))
#convert a list into tuple
list = [1,2,3,"math"]
tup1 = tuple(list)
print(tup1)
# remove comma and spaces in a tuple
# for first tuple
for i in a:
    print(i, end="")
#for second tuple
for j in b:
    print(j,  end="")
