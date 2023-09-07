strvariable = "Python"
print(strvariable)

print(strvariable[:3]) # Prints characters from the first index to the third index (first index 0).

print(strvariable[2:]) # Prints all characters from the second index to the last index.

print(len(strvariable)) # Print the number of letters in the word.

print("Learn " + strvariable + " !")

strvariable = "Learn " + strvariable + " !"

print(strvariable * 5) 

print(strvariable.upper())
print(strvariable.lower())
print(strvariable.split())
print(strvariable.split("o"))
print(strvariable.split(sep="!", maxsplit=1))

"""
.upper # Returns a string where all characters are in upper case.
.lower # Returns a string where all characters are lower case.
.split # Splits a string into a list (string.split(separator, maxsplit)).
"""