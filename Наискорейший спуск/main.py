import math
from array import *
from sympy import *

# ВВОД ЗНАЧЕНИЙ
w = 0.7
gamma = 0.5
last_x = -1         # Начальная точка
last_y = -2         # Начальная точка
eps = 0.01
# МОЖНО ИЗМЕНИТЬ, ЧТОБЫ ИЗМЕНИТЬ КОЛИЧЕСТВО ИТЕРАЦИЙ

x = Symbol('x')
y = Symbol('y')

# Функция
func = pow(pow(x, 2) - y, 2) + pow(x - 1, 2)


def fun(x_1, y_1):
    return (pow(pow(x_1, 2) - y_1, 2) + pow(x_1 - 1, 2))


# МЕТОД ГРАДИЕНТНОГО НАИСКОРЕЙШЕГО СПУСКА
k = 0       # номер шага


# Градиент
def grad_x(x_1, y_1):
    dx = diff(func, x)
    # print(dx)
    g_x = lambdify(x, dx)
    g_x1 = g_x(x_1)
    g_y = lambdify(y, g_x1)
    g_y1 = g_y(y_1)
    return (g_y1)


def grad_y(x_1, y_1):
    dy = diff(func, y)
    # print(dy)
    g_x = lambdify(x, dy)
    g_x1 = g_x(x_1)
    g_y = lambdify(y, g_x1)
    g_y1 = g_y(y_1)
    return (g_y1)


def g(x_1, y_1, kappa):
    return fun(x_1 - kappa * grad_x(x_1, y_1), y_1 - kappa * grad_y(x_1, y_1))


# Метод дихотомии
def dichotomia(a_0, b_0, epsilon, x_1, y_1):
    delta = 0.5 * epsilon
    ak = a_0
    bk = b_0
    while (bk - ak) >= epsilon:
        lk = (ak + bk - delta) / 2
        mk = (ak + bk + delta) / 2
        if g(x_1, y_1, lk) <= g(x_1, y_1, mk):
            bk = mk
        else:
            ak = lk
    return((ak + bk) / 2)


file = open("gradDescWithSpalStep.dat", "w")
while math.sqrt(pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)) > eps:
    kappa = dichotomia(-10, 10, 0.0001, last_x, last_y)
    next_x = last_x - kappa * grad_x(last_x, last_y)
    next_y = last_y - kappa * grad_y(last_x, last_y)
    file.write(str(last_x) + " " + str(last_y) + " " + str(fun(last_x, last_y)) + " " + str(kappa) + " " + str(
            math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)))) + "\n")
    print(k, "   ", last_x, " ", last_y, "   ", fun(last_x, last_y), "   ", kappa, "   ",
              math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2))))
    k = k + 1
    last_x = next_x
    last_y = next_y

file.close()







