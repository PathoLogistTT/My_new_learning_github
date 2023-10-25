import random

# ввод вручную
def manual_input():
    while True:
        array1 = input("\nвведите элементы первого массива через пробел: ").split()
        array2 = input("введите элементы второго массива через пробел: ").split()
        
        try:
            if all(0 <= int(num) <= 9 for num in array1) and \
               all(0 <= int(num) <= 9 for num in array2):
                # Преобразуем массивы в числа
                num1 = int(''.join(array1))
                num2 = int(''.join(array2))
                return num1, num2
            
            else:
                print("Пожалуйста, введите цифры от 0 до 9.")
                
        except ValueError:
            print("Ошибка: введён недопустимый символ")

# рандом
def generate_arrays():
    while True:
        
        try:
            size_array = int(input("Введите размер массивов: "))
            
            if size_array > 0:
                array1 = [random.randint(0, 9) for _ in range(size_array)]
                array2 = [random.randint(0, 9) for _ in range(size_array)] 
                num1 = int(''.join(map(str, array1)))
                num2 = int(''.join(map(str, array2)))
                print("Массив и число сгенерированы")
                return num1, num2
            
            else:
                print("Пожалуйста, введите положительное целое число.")
                
        except ValueError:
            print("Ошибка: введен недопустимый символ.")

def array_sum(num1, num2):
    result = num1 + num2
    return [int(digit) for digit in str(result)]  

def array_diff(num1, num2):
    result = num1 - num2
    return [int(digit) for digit in str(result)]  

def print_arrays(array1, array2, result):
    array1 = [int(digit) for digit in str(array1)]  
    array2 = [int(digit) for digit in str(array2)]
    print("\nПервый массив:", array1)
    print("Второй массив:", array2)
    print("Результат:", result)

def main_menu():
    print("\n1. Ввести массивы вручную или сгенерировать случайным образом")
    print("2. Выполнить алгоритм")
    print("3. Вывести результат")
    print("4. Вернуться к выбору заданий")

def input_menu():
    print("\n1. Ввести массивы вручную")
    print("2. Сгенерировать массивы случайным образом")
    print("3. Вернуться на предыдущую страницу")

def algorithm_menu():
    print("1. \nСумма массивов")
    print("2. Разность массивов")
    print("3. Вернуться на предыдущую страницу")

def print_result_menu():
    print("\n1. Вывести 2 исходных массива")
    print("2. Вывести 1 конечный массив")
    print("3. Вернуться на предыдущую страницу")

def sum_diff_array():
    array1 = []
    array2 = []
    result = []
    array_point = False
    
    while True:
        main_menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            while True:
                input_menu()
                inner_choice = input("Выберите пункт: ")
                if inner_choice == "1":
                    array1, array2 = manual_input()
                    break
                elif inner_choice == "2":
                    array1, array2 = generate_arrays()
                    break
                elif inner_choice == "3":
                    break
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")

        elif choice == "2":
            
            if array1 == [] or array2 == []:
                print("\nОшибка: массивы не заданы")
                
            else:    
                while True:
                    algorithm_menu()
                    algorithm_choice = input("Выберите пункт: ")
                    
                    if algorithm_choice == "1":
                        result = array_sum(array1, array2)
                        array_point = True
                        break
                    
                    elif algorithm_choice == "2":
                        result = array_diff(array1, array2)
                        array_point = True
                        break
                    
                    elif algorithm_choice == "3":
                        break
                    
                    else:
                        print("Некорректный выбор. Попробуйте еще раз.")

        elif choice == "3":
            
            if array1 == [] or array2 == [] or array_point == False:
                print("\nОшибка: массивы не заданы или не отработал алгоритм")
            
            else:
                print_arrays(array1, array2, result)
                break

        elif choice == "4":
            break
        
        else:
            print("Некорректный выбор. Попробуйте еще раз.")