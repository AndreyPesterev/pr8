while True:
    # Проверка ввода первого числа
    try:
        num1 = int(input("Введите первое целое число: "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
        continue

    # Проверка ввода второго числа
    try:
        num2 = int(input("Введите второе целое число: "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
        continue

    # Вывод суммы чисел
    print(f"Сумма: {num1 + num2}")
