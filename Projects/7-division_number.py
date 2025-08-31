#start

a = int(input("print your number: "))
b = int(input("print your number: "))
if a > b:
    c = a % b
    print(c)
elif b > a:
    c = b % a
    print(c)
else:
    print("Equal")
    
#finish