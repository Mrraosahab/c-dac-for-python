#printing array of elements in range 0-100
a=list(range(100))
n=3
list1=[a[i:i+n] for i in range(0,len(a),n)]
print(list1)
