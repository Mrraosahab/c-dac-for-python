#simple syntax of dictionary
dict1 = {"name":"pradeep", "city":"jaipur", "age":22}
print(dict1)
#print a particular index
print(dict1["name"])
print(dict1["age"])
# updating dictionary
dict1["school"]="vgu"
print(dict1)
#deleting dictionary
del dict1["name"]
print(dict1)
#len operation in dictionary
print(len(dict1))
#check the type/class of a entry in dictionary
print(type("city"))
#convert a dict into a string
print(str(dict1))
#check type of cnverted dictionary
print(type(str(dict1)))
#copy the dictionary
dict2 = dict1.copy()
print(str(dict2))
#create dictionary from set and key
seq = ("age", "name", "city")
print(seq)
dict3 = dict.fromkeys(seq,10)
print(dict3)
