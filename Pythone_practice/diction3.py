family = {
    "child1" : {
        "name": "souvik" ,
        "age" : 22 ,
        "Dob" : 2004
    } ,
    "child2" : {
        "name" : "sweety" ,
        "age" : 28 ,
        "Dob" : 1998
    } ,


}

print(family)
print(family["child1"])

daughter = {"name" : "soumi" , "age" : 18 , "fav" : "grey" }
mother = {"name" : "dont remember" , "age" : 35  , "fav" : "red"}
father ={ " name" :  "never heard it" , "age" : 45 , "fav" :"black"}

newfamily = {
    "daughter" : daughter ,
    "mother" : mother ,
    "father" : father

}
print(newfamily)
print(newfamily["father"]["fav"])

for x , y in newfamily.items():
    print(x)

    for z in y :
        print(z + ':' , y[z])