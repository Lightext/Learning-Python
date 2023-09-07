list1 = ['a', 'b', 'c', 'd', 'e', 'a']
print(list1)
tup = ('a', 'b', 'c', 'd', 'e', 'a')
print(tup)

list1[0] = '1231231'
print(list1)

print("You cannot use a command like tup[0] = '1231231'. Because tuple is an immutable list format.")

print(tup.__add__("a"))
print(tup.count("a"))
print(tup.count(True))
# print(tup.index("b"))
print("When we try to use a command like 'tup.index(True)', it gives an error because True is not in the tup list. There is no chance of returning 0 because 0 specifies a location.")
print(tup)