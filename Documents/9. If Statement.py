#-----if-----


weather_forecast = "rainy"
if weather_forecast == "rainy":
    print("Take your umbrella!")



weather_forecast = "snowy"
if weather_forecast == "rainy":
    print("Take your umbrella!")


#-----if+else-----


weather_forecast = "snowy"
if weather_forecast == "rainy":
    print("Take your umbrella!")
else:
    print("No Problem :D")


#-----if+else+elif-----


weather_forecast = "snowy"
if weather_forecast == "rainy":
    print("Take your umbrella!")
elif weather_forecast == "snowy":
    print("Take your scarf!")
else:
    print("No Problem :D")



age = 35
if age > 18:
    print("Hello!")
else:
    print("You don't belong here.")



list1 = ['a','b','c']
target_letter = 'd'
if target_letter in list1:
    print("Target letter available.")
else:
    print("Target letter is not available.")



list1 = ['a','b','c']
target_letter = 'd'
if target_letter in list1:
    print("Target letter available.")
else:
    print("Target letter is not available.")
    list1.append(target_letter)
    print("Target letter has been added.")
    print("Updated List = {} ".format(list1))



list1 = ['a','b','c']
target_letter = 'd'
if (target_letter in list1) and (target_letter == list1[0]):
    print("Target letter available. And it is in the position of the first element")
elif target_letter in list1:
    print("Target letter available.")
else:
    print("Target letter available.değil.")
    list1.append(target_letter)
    print("Target letter has been added.")
    print("Updated List = {} ".format(list1))
