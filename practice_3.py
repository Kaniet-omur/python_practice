# задание №1

a = int(input())

if a == 0:
    print("нулевое число")
elif a < 0:
    print("отрицательное целое число")
elif a > 0:
    print("положительное целое число")
else:
    print("число с плавающей точкой")


#Задание №2

a = input()
vowels = 'aioue'
consonansts = 'bcdfghjklmnpqrstvywz'

sum_vowels = sum(1 for letter in a if letter in vowels)
sum_consonansts = sum(1 for letter in a if letter in consonansts)

print(f'Гласные: {sum_vowels}, Согласные: {sum_consonansts}')


#Задание №3

x = int(input())
a = int(input())
b = int(input())

if a >= x and b >= x:
    print('2')
elif a >= x and b < x:
    print('Mike')
elif b >= x and a < x:
    print('Ivan')
elif (a + b) > x:
    print('1')
else:
    print('0')
     



