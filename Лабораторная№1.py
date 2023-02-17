from math import sqrt

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminant = b ** 2 - 4 * a * c  # формула дискриминанта
print("Дискриминант D = %.2f" % discriminant)

if discriminant > 0:  # есть ли корни уравнения
    x1 = (-b + sqrt(discriminant)) / (2 * a)  # первый корень
    x2 = (-b - sqrt(discriminant)) / (2 * a)  # второй корень
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))

elif discriminant == 0:  # если один корень
    x = -b / (2 * a)
    print("x = %.2f" % x)

else:  # если корней нет
    print("Корни отсутствуют")
