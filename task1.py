x = int(input("Введіть трьохзначне число: "))
a = x // 100
b = (x // 10) % 10
c = x % 10
digits = [a, b, c]
digits.sort()
asc = digits[0]*100 + digits[1]*10 + digits[2]
desc = digits[2]*100 + digits[1]*10 + digits[0]
print("Зростання:", asc)
print("Спадання:", desc)
