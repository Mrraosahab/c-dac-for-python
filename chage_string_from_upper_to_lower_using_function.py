def lowerc(a):
    for i in a:
        if 65<= ord(i) <= 90:
            new_str= ord(i)+32
            print(chr(new_str), end="")
a = input("enter string")
lowerc(a)
