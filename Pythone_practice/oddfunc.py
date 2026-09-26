def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "odd"

    
y = int(input("enter a number"))
z = int(input("enter a number"))
print(evenOdd(y))
print(evenOdd(z))
