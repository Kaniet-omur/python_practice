#Задача №1

n= int(input())
numbers = set(map(int, input().split()))

print(len(numbers))


#Задача №2

n = int(input())
first_list = {int(input()) for i in range(n)}

m = int(input())
second_list = {int(input()) for i in range(m)}

elements = first_list & second_list
print(len(elements))

#Задча №3

numbers = list(map(int, input().split()))
seen = set()

for number in numbers:
    if number in seen:
        print('Yes')
    else:
        print('No')
        seen.add(number)