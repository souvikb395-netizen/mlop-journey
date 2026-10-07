data = {"brand" : "ford" , "model"  : "mustang" , "year" : 2021 , }
print(data)
print(data.get("model"))
print(data["brand"])
data["color"] = "red"
data.pop("year")
print(data)

