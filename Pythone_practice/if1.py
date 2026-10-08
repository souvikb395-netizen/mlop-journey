a = int(input("enter a number"))
b = int(input("enter second number"))

if b > a :
    print("b>a")
elif a == b:
    print("a=b")
else :
    print("a > b")
print("A") if a > b else print("B")
