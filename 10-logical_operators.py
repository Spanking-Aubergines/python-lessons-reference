# or - at least one condition true. if one condition true, the statement is true
# and - both conditions must be true
# not - invert the condition

temp = 30
is_sunny = False

# if temp > 35 or temp < 0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")    

if temp>=28 and is_sunny:
     print("hot")
     print("sunny")
elif temp <= 0 and is_sunny:
     print("cold")
     print("sunny")
elif 28 > temp > 0 and is_sunny:
     print("warm")
     print("sunny")
elif temp>=28 and not is_sunny:
     print("hot")
     print("cloudy")
elif temp <= 0 and not is_sunny:
     print("cold")
     print("cloudy")
elif 28 > temp > 0 and not is_sunny:
     print("warm")
     print("cloudy")