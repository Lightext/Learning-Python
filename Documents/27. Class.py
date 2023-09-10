# A Class is like an object constructor, or a "blueprint" for creating objects.

class Class1:
  x = 5
print(Class1)

class Class2:
    y = 10
p1 = Class2()
print(p1.y)

# __init__ # The init method in Python is a constructor for a class that initializes the object's state by assigning values to the data members of the class.
# The self parameter refers to the instance of the object and binds the attributes with the given arguments.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# __str__ # The str() method in Python is a special method that is called during the printing of an instance of a class.
# This method returns the string representation of the instance and is used during the printing of instances

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

# You can delete properties on objects and objects directly by using the "del" keyword.

del p1.age
del p1
