# lambda arguments : expression #
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

fonk = lambda a, b: a + b # This is an addition function.
print(fonk(15, 16))

dong = lambda a, b: a * b # This is a multiplication function.
print(dong(5, 6))

dang = lambda a, b, c: a + b + c # This is a summarize function.
print(dang(11, 10, 8))

# The power of lambda is better shown when you use them as an anonymous function inside another function.

def omfg(n):
    return lambda a : a * n
doubler = omfg(2)
print(doubler(11))