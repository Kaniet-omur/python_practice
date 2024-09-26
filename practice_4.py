#Задача №1

n = int(input())

zeros = 0
for i in range (n):
    number = int(input())
    if number == 0:
        zeros += 1
print(zeros)


#Задача №2
import math
x = int(input())

divisors = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        divisors += 1
        if i != x // i:
            divisors += 1
print(divisors)


#Задача №3

a = int(input())
b = int(input())

for i in range (a, b + 1):
    if i % 2 ==0:
        print(i, end=" ")