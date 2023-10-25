import numpy as np

# против часовой
def rotate_clockwise(matrix):
    return np.rot90(matrix, k=-1)

# по часовой
def rotate_counter_clockwise(matrix):
    return np.rot90(matrix)

# Ввод матрицы случайным образом
def generate_random_matrix():
    n, m = input_column_and_row()
    return np.random.randint(-10, 10, (n, m))

# Ввод строк и столбцов матрицы
def input_column_and_row():
    while True:
        try:
            n = int(input("\nВведите количество строк: "))
            m = int(input("Введите количество столбцов: "))
        
            if n <= 0 or m <= 0 or n != int(n) or m != int(m):
                raise ValueError
            else:
                return n, m
            
        except ValueError:
            print("\nОшибка: введено некорректное значение для количества строк или столбцов")

# Ввод матрицы вручную        
def matrix_manually(matrix):
    while True:
        try:
            n, m = input_column_and_row()
    
            for i in range(n):
                row = input(f"Введите строку {i+1} матрицы через пробел: ").split()
                row = [int(x) for x in row]
    
                if len(row) != m:
                    raise ValueError(f"Количество элементов в строке {i+1} не соответствует заданному количеству столбцов!")
    
                matrix.append(row)
    
            break 
    
        except ValueError as e:
            print("Ошибка:", str(e))
            matrix = []  
    
    return matrix
        
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))        

def matrix_rotate():
    matrix = []
    matrix_point = False
    while True:
        print("\n1. Ввести матрицу вручную или сгенерировать случайным образом")
        print("2. Выполнить алгоритм")
        print("3. Вывести результат")
        print("4. Вернуться к выбору заданий")
        
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            while True:
                print("\n1. Ввести матрицу вручную")
                print("2. Сгенерировать матрицу случайным образом")
                print("3. Вернуться на предыдущую страницу")

                sub_choice = input("\nВыберите пункт меню: ")

                if sub_choice == "1":
                    matrix = matrix_manually(matrix)
                    print("\nМатрица успешно введена")
                    print_matrix(matrix)
                    break
                elif sub_choice == "2":
                    matrix = generate_random_matrix()
                    print("\nМатрица успешно сгенерирована")
                    print_matrix(matrix)
                    break
                elif sub_choice == "3":
                    break
                else:
                    print("\nОшибка: введен некорректный пункт меню")
        elif choice == "2":
            if matrix is []:
                print("\nОшибка: матрица не задана")
            else:
                while True:
                    print("\n1. Повернуть по часовой стрелке")
                    print("2. Повернуть против часовой стрелки")
                    print("3. Вернуться на предыдущую страницу")

                    sub_choice = input("\nВыберите пункт меню: ")

                    if sub_choice == "1":
                        matrix = rotate_clockwise(matrix)
                        print("\nМатрица успешно повернута по часовой стрелке")
                        matrix_point = True
                        break
                    elif sub_choice == "2":
                        matrix = rotate_counter_clockwise(matrix)
                        print("\nМатрица успешно повернута против часовой стрелки")
                        matrix_point = True
                        break
                    elif sub_choice == "3":
                        break
                    else:
                        print("\nОшибка: введен некорректный пункт меню")
        elif choice == "3":
            if matrix is [] or matrix_point == False:
                print("\nОшибка: матрица не задана или не отработан алгоритм")
            else:
                print("\nРезультат: \n")
                print_matrix(matrix)
        elif choice == "4":
            break
        else:
            print("\nОшибка: введен некорректный пункт меню")