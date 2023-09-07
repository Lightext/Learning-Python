print("Hello \t hi")
print("Hello \n hi")
print("My name is {}".format('Ozan'))
print("My name is {}, I'm {}".format('Ozan', 15)) # Places them in order

print("My name is {0}, I'm {1}".format('Ozan', 15))
print("My name is {1}, I'm {0}".format('Ozan', 15)) # False

print("My name is {name}, I'm {age}".format(name='Ozan', age=15))
print("My name is {age}, I'm {name}".format(name='Ozan', age=15)) # False

print("""Hello
Hi""") # Write in a row using a single print command