import math
import numpy as np
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


# МЕТОД ГРАДИЕНТНОГО СПУСКА С ДРОБЛЕНИЕМ ШАГА
k = 0       # номер шага
kappa_0 = 1
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


file = open("gradDescWithSpalStep.dat", "w")
while math.sqrt(pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)) > eps:
    kappa = kappa_0
    next_x = last_x + kappa * grad_x(last_x, last_y)
    next_y = last_y + kappa * grad_y(last_x, last_y)
    if k == 0:
        file.write(str(last_x) + " " + str(last_y) + " " + str(fun(last_x, last_y)) + " " + str(kappa) + " " + str(
            math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)))) + "\n")
        print(k, "   ", last_x, " ", last_y, "   ", fun(last_x, last_y), "   ", kappa, "   ",
          math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2))))
    while fun(last_x, last_y) - fun(next_x, next_y) <= w * kappa * (pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)):
       kappa = kappa * gamma
       next_x = last_x - kappa * grad_x(last_x, last_y)
       next_y = last_y - kappa * grad_y(last_x, last_y)
    if k != 0:
        file.write(str(last_x) + " " + str(last_y) + " " + str(fun(last_x, last_y)) + " " + str(kappa) + " " + str(
            math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2)))) + "\n")
        print(k, "   ", last_x, " ", last_y, "   ", fun(last_x, last_y), "   ", kappa, "   ",
              math.sqrt((pow(grad_x(last_x, last_y), 2) + pow(grad_y(last_x, last_y), 2))))
    k = k + 1
    last_x = next_x
    last_y = next_y

file.close()






