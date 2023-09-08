#The dict() function creates a dictionary.
#A dictionary is a collection which is unordered, changeable and indexed

dict1 = {'name': 'Ozan', 'age': 15, 'location': 'Mersin' }
print(dict1)
#{'name': 'Ozan', 'age': 15, 'location': 'Mersin'}

dict1 = {
    'name':'Ozan',
    'age':15,
    'location':'Mersin'
}

dict2 = {
    'name':'Ozan',
    'age':15,
    'livingcity':'Mersin',
    'bornCity':'Mersin',
    #'location':
}
print(dict2)
#{'name': 'Ozan', 'age': 15, 'livingcity': 'Mersin', 'bornCity': 'Mersin'}

dict3 = {
    'name':'Ozan',
    'age':15,
    'location':{
        'livingcity':'Mersin',
        'bornCity':'Samsun',
    }
}
print(dict3)
#{'name': 'Ozan', 'age': 15, 'location': {'livingcity': 'Mersin', 'bornCity': 'Samsun'}}

print(dict2["age"])
#15
print(dict2.get("age"))
#15

print(dict3['location']['livingcity'], dict3['location']['bornCity'])
#Mersin Samsun

print(dict3.get("location").get("livingcity"))
#Mersin

print(dict2.keys())
#dict_keys(['name', 'age', 'livingcity', 'bornCity'])
print(dict2.values())
#dict_values(['Ozan', 15, 'Mersin', 'Mersin'])
print(dict2.items())
#dict_items([('name', 'Ozan'), ('age', 15), ('livingcity', 'Mersin'), ('bornCity', 'Mersin')])