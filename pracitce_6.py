#Задача №1

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
reversed_numbers= numbers[::-1]
print(*reversed_numbers)


#Задача №2

n = int(input())

numbers = list(map(int, input().split()))

for i in range(n // 2):
    numbers[i], numbers[n - i- 1] = numbers[n - i -1], numbers[i]

print(*numbers)

# Задча №3

m = int(input())
n = int(input())

weights = [int(input()) for i in range(n)]
weights.sort()

left = 0
right = n -1 
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1
print(boats)