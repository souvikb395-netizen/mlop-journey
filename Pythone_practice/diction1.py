data ={"brand" : "Ford" , "model" : "mustang" , "year" : 1997}
data["year"] = 2018
print(data)

data.update({"year" : 2020})
print(data)

data["color"] = "red"
print(data)

data.update({"style" : "modern"})
print(data)

data.pop("style")
print(data)

data.popitem()
print(data)

for x in data :
    print(x)
    print(data[x])
for y in data.keys():
    print(y)
for o , p in data.items():
    print( o ,p)