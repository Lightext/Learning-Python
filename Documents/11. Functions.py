# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def print_five():
    print(5)
print_five()

def trump_family(fname):
    print(fname + " Trump")
trump_family("Donald")
trump_family("Melania")
trump_family("Eric")

# Arguments are often shortened to args in Python documentations.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_name(fname, lname):
    print(fname + " " + lname)
my_name("Ozan", "K")

def age_of_kids(*kids):
  print("The youngest child is " + kids[2])
age_of_kids("Emil", "Tobias", "Linus")

# If you do not know how many arguments that will be passed into your function, add a "*" before the parameter name in the function definition.

# You can also send arguments with the key = value syntax.

def sorting_name(name1, name2, name3):
    print("The best name is " + name1)
sorting_name(name1 = "Jack", name2 = "Amber", name3 = "Frankin")

def country_function(country = "Norway"):
  print("I am from " + country)
country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")

def food_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
food_function(fruits)

def multiplication_w_five(x):
    return 5 * x
print(multiplication_w_five(4))
print(multiplication_w_five(2))
print(multiplication_w_five(15))
print(multiplication_w_five(7))

# Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def untitled_function():
    pass

# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)
