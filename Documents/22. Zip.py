countries = ["TR", "FR", "DE"]
sorting = range(1,4)

for country in zip(countries,sorting):
    print(country)
#('TR', 1)
#('FR', 2)
#('DE', 3)


countries = ["TR", "FR", "DE"]
sorting = range(1,4)
list1 = []

for country in zip(countries,sorting):
    list1.append(country)
print(list1)# [('TR', 1), ('FR', 2), ('DE', 3)]
print(len(list1))# 3