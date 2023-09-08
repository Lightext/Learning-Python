letters = ["a", "b", "c", "d", "e"] * 100
for index, letter in enumerate(letters):
    if letter == "c":
        print("Letter '{}' in index {}.".format(letter,index))
        break
# Letter 'c' in index 2.