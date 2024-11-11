def print_numbers_between():
    # Функция для ввода и проверки числа
    def get_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: Пожалуйста, введите целое число.")
    
    # Ввод чисел a и b с проверкой
    a = get_integer("Введите число a: ")
    b = get_integer("Введите число b: ")

    # Определение диапазона и вывод чисел между a и b
    if a < b:
        numbers = range(a + 1, b)
    else:
        numbers = range(b + 1, a)

    print("Числа между a и b:", *numbers)

print_numbers_between()

