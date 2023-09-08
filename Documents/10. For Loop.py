for i in range(1, 11):
    print(i)


fruits = ["Apple","Pear","Banana"]
for i in fruits:
    print(i)
    if i == "Pear":
        break


tup1 = (1,3,5,7)

for number in tup1:
    print(number)


list1 = [[1,2],[3,4]]

for x,y in list1:
    print(x)


list1 = [[1,2],[3,4],[5,6]]

for x,y in list1:
    print(x*y)


for i in range(6):
    print(i)
# From 0 up to the specified number.


for i in range(3,7):
    print(i)
# Numbers in the specified range.


for i in range(1,20,3):
    print(i)
# The 3rd value indicates the number of increments.


for x in range(6):
    print(x)
else:
    print("Finally completed!")


adjectives = ["Fresh","Delicious","Big"]
fruits = ["Apple","Pear","Banana"]

for x in adjectives:
    for y in fruits:
        print(x,y)