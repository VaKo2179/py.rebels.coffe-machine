dict1 = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

dict2 = {
    "water": 100,
    "milk": 50,
    "coffee": 75,
}

result = {}

for key in dict1:
    if key in dict2:
        result[key] = dict1[key] - dict2[key]

print(result)