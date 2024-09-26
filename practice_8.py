#Задача №1

pets = {}
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")


pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

if 11 <= pet_age % 100 <= 19:
    age_suffix = "лет"
elif pet_age % 10 == 1:
    age_suffix = "год"
elif 2 <= pet_age % 10 <= 4:
    age_suffix = "года"
else:
    age_suffix = "лет"

pet_info = (
    f"Это {pets[pet_name]['Вид питомца']} по кличке \"{pet_name}\". "
    f"Возраст питомца: {pets[pet_name]['Возраст питомца']} {age_suffix}. "
    f"Имя владельца: {pets[pet_name]['Имя владельца']}."
)



print(pet_info)



#Задача №2


my_dict = {}
for i in range(10, -6, -1):
    my_dict[i] = i ** i
print(my_dict)