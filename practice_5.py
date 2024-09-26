#Задача №1

s = input("")
s = s.lower().replace(" ", "")
is_palindrome = True
length = len(s)

for i in range(length // 2):
    if s[i] != s[length - 1 - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Yes")
else:
    print("No")


#Задача №2

s = input("")
new_string = ""
space = False
for i in s:
    if i == " ":
        if not space:
            new_string += i
            space = True
    else:
        new_string += i
        space = False

print(new_string)