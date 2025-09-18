import math

x = float(input())

if x > 0:
    y = math.log2(x) - x**2
    print(y)
elif -1 <= x <= 0:
    y = math.cos(x) + math.sin(x)
    print(y)
elif x < -4:
    try:
        y = math.exp(x) + math.pow(x, math.e)
        print(y)
    except ValueError:
        print("значення не є дійсним")
else:
    print("функція не визначена для цього x")
