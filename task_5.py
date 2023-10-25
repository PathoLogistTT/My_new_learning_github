import random
from functools import reduce
# Модуль 5
def input_array_and_number():
    array = []
    while True:
        try:
            num_elements = int(input("введите количество элементов в массиве: "))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    print("Введите элементы массива:")
    for i in range(num_elements):
        while True:
            try:
                element = int(input(f"Элемент {i+1}: "))
                array.append(element)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    return array, num

def generate_array_and_number():
    num_elements = random.randint(1, 10)
    array = [random.randint(1, 10) for _ in range(num_elements)]
    num = random.randint(1, 10)
    return array, num

def get_subarrays_with_target_sum(array, num):
    def add_subarray(subarrays, element):
        new_subarrays = [subarray + [element] for subarray in subarrays]
        return subarrays + new_subarrays

    subarrays = reduce(add_subarray, array, [[]])

    result = []
    for subarray in subarrays:
        if sum(subarray) == num:
            result.append(subarray)

    return result

def subarray():
    array = []
    num = None
    point = False
    
    while True:
        print("\n1. Ввести массив и число  вручную или сгенерировать случайно")
        print("2. Выполнить алгоритм")
        print("3. Вывести результат")
        print("4. Вернуться к выбору заданий")
        
        choice = input("Выберите пункт: ")
        
        if choice == "1":
            print("\n1. Ввести массив и число вручную")
            print("2. Сгенерировать массив и число случайным образом")
            print("3. Вернуться на предыдущую страницу")
            
            sub_choice = input("Выберите пункт: ")
            
            if sub_choice == "1":
                array, num = input_array_and_number()
            elif sub_choice == "2":
                array, num = generate_array_and_number()
            elif sub_choice == "3":
                break
            else:
                print("Некорректный выбор.")
                
        elif choice == "2":
            if not array or num == None:
                print("Пожалуйста, введите массив и число.")
            else:
                result = get_subarrays_with_target_sum(array, num)
                print("Алгоритм выполнен")
                point = True
        
        elif choice == "3":
            if not array or num == None or point == False:
                print("Введите массив и число или не отработал алгоритм.")
            else:
                print("Результат:")
                print(f"Исходный массив: {array}")
                print(f"Число: {num}")
                print(f"Подмассивы, дающие сумму числа {num}: {result}")
                break
        
        elif choice == "4":
            break
        
        else:
            print("Некорректный выбор.")