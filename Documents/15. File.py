file = open("test.txt", "w")
print("SECRET WORDS", file=file)
file.close()

import os
os.getcwd()

f = open("personal_informations.txt", "w")
print("Tom Hardy", file=f)
print("Mersin", file=f)
print("Windows", file=f)
f.close()
