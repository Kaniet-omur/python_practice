#Задание №1
import math

def factorial_list(n):
    factorial_n = math.factorial(n)

    result = [math.factorial(i) for i in range(factorial_n, 0, -1)]
    
    return result


#Задание №2
pets = {}

def create(pet_info):
    pets[pet_info['name']] = pet_info


def read(pet_name):
    if pet_name in pets:
        pet_info = pets[pet_name]
        print(f"Это {pet_info['species']} по кличке '{pet_info['nickname']}'. Возраст питомца: {pet_info['age']} лет. Имя владельца: {pet_info['owner']}")
    else:
        print("Питомец с таким именем не найден")



def update(pet_name, new_data):
    if pet_name in pets:
        pets[pet_name].update(new_data)
    else:
        print(f"{pet_name} не существует")


def delete(pet_name):

    if pet_name in pets:
        del pets[pet_name]
    else:
       print(f"{pet_name} не существует")



