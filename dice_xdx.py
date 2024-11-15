import random as rd

# Украшательства вывода
line_separator = ("="*64)

# Количество граней
number_of_faces = 6

# Список со значениями граней (сейчас от 1 до n в порядке + 1)
list_of_faces = [i for i in range(1, number_of_faces+1)]


# Функция заданного количества броска кости
def cast(input_number: int) -> tuple:
    list_of_casts = []                          # Список значений бросков
    for j in range(input_number):
        new_value = rd.choice(list_of_faces)    # очередной бросок кости
        list_of_casts.append(new_value)         # дополнение списка значений бросков
        j += 1

    sum_of_casts = sum(list_of_casts)           # Сумма всех бросков
    mean_sum_of_casts = round(sum_of_casts/len(list_of_casts), 2)    # Средне арифметическое, округление до 2 цифр
    cast_results = (list_of_casts, sum_of_casts, mean_sum_of_casts)  # Кортеж с результатами функции
    return cast_results


# Функция печати одной серии бросков
def print_result(list_of_casts: list, sum_of_casts: int, mean_sum_of_casts):  # (список бросков, сумма, среднее)
    print(line_separator)
    print(f"Случайные броски кости с {number_of_faces} гранями:", list_of_casts, sep="\n")  # Вывод списка бросков
    print("Сумма всех бросков: ", sum_of_casts)
    print(f"Среднее арифметическое бросков: {mean_sum_of_casts:.2f}")
    print(line_separator)


# Цикл бросков
def main():
    while True:
        input_chars = input("Введите количество бросков (не число  - выход):")
        if input_chars.isdigit():                # Если ввод число
            input_number = int(input_chars)      # Перевод в натуральное
            cast_results = (cast(input_number))  # Вызов функции бросков
            print_result(*cast_results)          # Вызов функции печати (* = распаковка кортежа по 3 аргументам)
        else:
            print("Пока!")                       # Если ввод не число,
            return


if __name__ == "__main__":
    main()
