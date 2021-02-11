import itertools


# Простая генерация:

# data = [i for i in range(0, 10) ]
# print(data)

# data = [i for i in "Alimpiev"]
# print(data)

# Генератор с условием:

# data = [i for i in range(0, 50) if i % 2 == 0]
# print(data)

# Генератор с циклом

# data = [i * j for i in range(0, 30) for j in range(0, 30)]
# print(data)

# Генерация вложенных списков:

# data = [[ i * j for i in range(0, 30)] for j in range(0, 30)]
# print(data)

# data = [[0 for x in range(5)] for y in range(3)]
# print(data)

# Генератор списка с lambda:

# data = [(lambda i: i*i)(i)for i in range(10)]
# print(data)

# Применение itertools:

# data = [i for i in itertools.repeat(1, 10)]
# print(data)

# Сумма цифр:

# num = int(input("Ведите челое число"))
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Сумма цифр числа равна: ", sum)

# Произведение цифр:

# num = int(input("Ведите челое число:"))
# mult = 1
# while (num != 0):
#     mult = mult * (num % 10)
#     num = num // 10
# print("Произведение цифр равно: ", mult)

# Задано дробное число:

# num = input("Ведите дробное число:")
# # разделим введённое (тип данных строка) на две части
# x = num.split(".")
# a = int(x[0])  # целая часть
# b = int(x[1])  # дробная часть
# mult = 1
# while (a != 0):  # перемножаем числа целой части
#     mult = mult * (a % 10)
#     a = a // 10

# while (b != 0):
#     mult = mult * (b % 10)
#     b = b // 10

# print("Произведение цифр равно:", mult)

# При приведении к действительному:

# num = float(input("Введите дробное: ")) # Преобразуем строку в дробное
# a = int(num) # целая часть, например, 5
# b = num - int(num) # дробная часть, например, 0.55
# print("a =", a)
# print("b =", b)
# mult = 1
# while (a != 0): # перемножаем числа целой части
#     mult = mult * (a % 10)
#     a = a // 10
# while (b != 0): # b никогда не будет равно 0
#     mult = mult * int(b*10) # 0.55 * 10 = 5.5, int(5.5) = 5
#     b = b * 10 - int(b * 10)
# print("Произведение цифр равно:", mult)

# Числа Фибоначчи:

# prew = cur = 1
# element = input('Введите номер искомого элемента : ')
# element = int(element)
# for n in range(int(element-2)):
#     tmp = prew + cur
#     prew = cur
#     cur = tmp
# print(str(element)+' элемент последовательности равен ' + str(cur))

# Рекурсия:

# def fibonacci(n):
#     cur = 1
#     if n > 2:
#         cur = fibonacci(n-1) + fibonacci(n-2)
#     return cur

# element = input('Введите номер искомого элемента : ')
# element = int(element)
# value = fibonacci(element)
# print(str(element)+' элемент последовательности равен ' + str(value))

# Конечно, пример с рекурсией интересен. Но он будет работать гораздо медленнее.
# А если вы решите вычислить, допустим 1000-ый элемент последовательности. Используя цикл, мы его очень быстро рассчитаем. А вот в случае с рекурсией получим ошибку превышения максимального количества рекурсий:

# Генератор списка:

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(20))
print(data)


