# The Walrus operator
# Разрешить присваивание и возрать значения в одном вырожении

from timeit import timeit
import random
import statistics
import math
from importlib import metadata
inputs = list()
while (current := input("Написать что-то: ")) != "выход":
    inputs.append(current)

# Как указать только пазиционные аргументы

def greet(name, /, greeting="Привет"):
    return f"{greeting}, {name}"

greet("Артём")
greet("Артём", greeting="Сегодня на работу")

# Более точные типы:
# Python поддерживает необезательные подсказки типов обычно в виде
# анатаций в вашем коде : пишем код в терминале


def double(number: float) -> float:
    return 2 * number

double(3.14)
double("I'm not a float")

# Проверки статического типа
# Для начало импортируем библиотеку python3 -m pip install mypy

def double(number: float) -> float:
    return 2 * number

double(3.14)
double(2.14)

# Упрощенная отладка с помощью f-строк

name = "Артём"
f"{name = :>10}"
f"{name.upper()[::-1] = }"

# Вы узнаете о новом модуле в стандартной библиотеке
# Python 3.8 importlib.metadata.
# Через этот модуль вы можете получить доступ к информации
# об установленных пакетах в вашей установке Python. Вместе со
# своим компаньоном модулем importlib.resources,
# importlib.metadataулучшает функциональность старше pkg_resources.
# В качестве примера вы можете получить некоторую информацию о pip:

metadata.version("pip")
# '21.0.1'
pip_metadata = metadata.metadata("pip")
list(pip_metadata)
# ['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python']

pip_metadata["Home-page"]
# 'https://pip.pypa.io/'

pip_metadata['Requires-Python']
# '>=3.6'

len(metadata.files("pip"))
# 762

# Математические и статистические функции
# Новая функция math.isqrt(). Вы можете использовать, isqrt()чтобы найти целую часть квадратных корней :

math.isqrt(9)
# 3
math.sqrt(9)
# 3.0
math.isqrt(15)
# 3
math.sqrt(15)
# 3.872983346207417

# Наконец, теперь вы можете более легко работать с n -мерными точками и векторами в стандартной библиотеке. Вы можете найти расстояние между двумя точками с помощью math.dist(), а длину вектора с помощью math.hypot():

point_1 = (16, 25, 20)
point_2 = (8, 15, 14)

math.dist(point_1, point_2)
# 14.142135623730951
math.hypot(*point_1)
# 35.79106033634656
math.hypot(*point_2)
# 22.02271554554524

# statistics.fmean() вычисляет среднее значение чисел с плавающей запятой.
# statistics.geometric_mean() вычисляет среднее геометрическое чисел с плавающей запятой.
# statistics.multimode() находит наиболее часто встречающиеся значения в последовательности.
# statistics.quantiles()вычисляет точки отсечения для разделения данных на n непрерывных интервалов с равной вероятностью.

data = [9, 3, 2, 1, 1, 2, 7, 9]
statistics.fmean(data)
# 4.25
statistics.geometric_mean(data)
# 3.013668912157617
statistics.multimode(data)
# [9, 2, 1]
statistics.quantiles(data, n=4)
# [1.25, 2.5, 8.5]

# В Python 3.8 появился новый statistics.NormalDistкласс, который делает более удобной работу с нормальным распределением Гаусса . Чтобы увидеть пример использования NormalDist, вы можете попробовать сравнить скорость нового statistics.fmean()и традиционного statistics.mean():

import random
import statistics
from timeit import timeit

# Create 10,000 random numbers
data = [random.random() for _ in range(10_000)]

# Measure the time it takes to run mean() and fmean()
t_mean = [timeit("statistics.mean(data)", number=100, globals=globals())
          for _ in range(30)]
t_fmean = [timeit("statistics.fmean(data)", number=100, globals=globals())
           for _ in range(30)]

# Create NormalDist objects based on the sampled timings
n_mean = statistics.NormalDist.from_samples(t_mean)
n_fmean = statistics.NormalDist.from_samples(t_fmean)

# Look at sample mean and standard deviation
n_mean.mean, n_mean.stdev
# (0.825690647733245, 0.07788573997674526)
n_fmean.mean, n_fmean.stdev
# (0.010488564966666065, 0.0008572332785645231)
# Calculate the lower 1 percentile of mean
n_mean.quantiles(n=100)[0]
# 0.6445013221202459
