# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_A = int(input('Введите координату X для точки А: '))
y_A = int(input('Введите координату Y для точки В: '))
x_B = int(input('Введите координату X для точки А: '))
y_B = int(input('Введите координату Y для точки В: '))

x = x_A - x_B
y = y_A - y_B
distance = (x ** 2 + y ** 2) ** (1/2)
print(round(distance, 3))
