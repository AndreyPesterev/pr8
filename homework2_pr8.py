while True:
    try:
        # Запрашиваем у пользователя ввод двух чисел
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        
        # Вычисляем сумму
        total = num1 + num2
        
        # Выводим результат
        print(f"Сумма {num1} и {num2} равна {total}.")
    except ValueError:
        print("Пожалуйста, введите корректные целые числа.")
