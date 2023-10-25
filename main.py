# Вариант-345 

import task_3
import task_4
import task_5

def main():
    while True:
        print("\nосновное меню:")
        print("1. Повернуть матрицу по или против часовой стрелки на 90 градусов")
        print("2. Сложение или вычитание массивов")
        print("3. Сумма подмножеств конкретного числа")
        print("4. Выход из программы")
        
        choice = input("Выберите пункт: ")
        
        if choice == "1":
            task_3.matrix_rotate()
            
        elif choice == "2":
            task_4.sum_diff_array()
            
        elif choice == "3":
            task_5.subarray()
            
        elif choice == "4":
            break
        
        else:
            print("/nНекорректный выбор. Пожалуйста, выберите один из доступных пунктов.")
            
    input("/nПрограмма завершена. Нажмите Enter, чтобы продолжить...")
    
if __name__ == "__main__":
    main()