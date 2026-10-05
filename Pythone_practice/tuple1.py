tup1 = (0 , 1 , 2 , 3 , 4)
tup2 = ('souvik', 'soumi' , 'rahul')
tup3 = tup1 + tup2
print(tup3)

tup = tuple('souvikbiswas')
print(tup[1:])
print(tup[:1])
print(tup[::-1])
print(tup[3:6])
print(tup[5])

tup4 = (0 ,2 ,3 ,4 )
del tup4

tup5 = (0,2, 3, 5, 6)
a , *b , c = tup5
print(a)
print(b)
print(c)
