data = {
    "name": "souvik" , 
    "age" : 22 ,
    "DOB" : 2004 ,
    "DOB" : 2003 ,#overwrite the previous data
    "likings" : ["sports" , "tv" , "Anime"] 
}
print(data)
print(data["DOB"])
print(len(data))
print(type(data))

data1 = dict(name = "soumi" , age = 18 , likings = ["makeup" , "skincare" ,"food"] )
print(data1)
x = data["age"]
print(x)
y = data1.get("likings")
print(y)
z = data.keys()
print(z)

data["fc"] = "black"

print(z)

v = data.values()
print(v)

data["fc"] = "white"
print(v)

i = data.items()
print(i)

data["fc"] = "brown"
print(i)

if "age" in data:
    print("yes")