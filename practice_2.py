# задание №1


import math

a = float(input("введите одну сторону "))
b = float(input("введите вторую сторону "))
c = float(input("введите третью сторону "))

print(f'Периметр треугольника: {round(a + b + c)}')
p = (a + b + c) / 2
print(f'Площадь треугольника: {round(math.sqrt(p * (p -a) * (p - b) * (p -c)))}')

# Задание №2

a = int(input())
ten_thousand = a // 10000
thousand = (a // 1000) % 10
hundred = (a // 100) % 10
ten = (a // 10) %10
units = a % 10

result = (ten ** units) * hundred / (ten_thousand - thousand)
print(result)