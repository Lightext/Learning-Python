range(10)# [start:end]

print(range(10))# range(0, 10)

type(range(10))# range

list(range(10))# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(11, 19))# [11, 12, 13, 14, 15, 16, 17, 18]

[*range(10)]# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[*range(11, 19)]# [11, 12, 13, 14, 15, 16, 17, 18]
[*range(0, 10, 2)]# [0, 2, 4, 6, 8]


'''

for number in range(10):
    if number == 5:
        print(number)

# 5


for number in range(10):
    if number < 5:
        print(number)

# 0
# 1
# 2
# 3
# 4

'''