list1 = ['a', 'b', 'c', 'd', 'e', 'a']
print(list1)

list1 = list1 + ['f']
print(list1)

print(list1[0], "is the first letter of the alphabet")
print(list1[3:5])

print(list1.append('g')) # .append # Appends an element to the end of the list.
print(list1)

print(list1.pop()) # .pop # Removes the element at the specified position.
print(list1)
print(list1.pop(5))
print(list1)

numbers = [123, 12321, 312, 45435, 35, 345, 1, 1]

numbers.sort() # .sort # Sorts the list ascending by default (default = "list.sort(reverse=True|False, key=myFunc)").

print(numbers)

numbers.reverse() # .reverse # Reverses the sorting order of the elements.
print(numbers)

print(set(numbers))