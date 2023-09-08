letters = ["a", "b", "c", "d"]
for letter in enumerate(letters):
    print(letter)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index, letter in enumerate(letters):
    print(index, letter)
# 0 a
# 1 b
# 2 c
# 3 d

for index, letter in enumerate(letters):
    print("{}. letter {}".format(index+1, letter))
#1. letter a
#2. letter b
#3. letter c
#4. letter d