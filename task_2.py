import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return 4 * x**3 - 5 * x + 15


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(
    "Графік інтегрування f(x) = 4x^3 - 5x + 15 від " + str(a) + " до " + str(b)
)

# Додамо рандомні точки
n = 10000
for _ in range(n):
    random_x = random.uniform(0, 2)
    random_y = random.uniform(0, max(y))
    color = "blue" if random_y <= f(random_x) else "green"
    ax.plot(random_x, random_y, marker="o", color=color, markersize=1)


plt.grid()
plt.show()


# Обчислення інтеграла за допомогою методу монте-карло
def monte_carlo_for_area_of_curvilinear_figure(f, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(0, y_max, num_points)
    under_curve = np.sum(y < f(x))
    area = (b - a) * (y_max - y_min) * (under_curve / n) 
    return area


def monte_carlo_for_definite_integral(f, a, b, n):
    x = np.random.uniform(a, b, n)
    y  = f(x)
    y_mean = sum(y) / n
    return (b - a) * y_mean


# Задання параметрів для генерації випадкових точок
n = 10000
a = 0
b = 2
y_min = 0
y_max = 50

# Обчислення інтеграла за допомогою методу Монте-Карло для площі криволінійної фігури
res_mc1 = monte_carlo_for_area_of_curvilinear_figure(f, a, b, y_min, y_max, n)
print(
    "Площа криволінійної фігури, обчислена за допомогою методу Монте-Карло: ", res_mc1
)

# Обчислення інтеграла за допомогою методу Монте-Карло для визначеного інтегралу
res_mc2 = monte_carlo_for_definite_integral(f, a, b, n)
print("Визначений інтеграл, обчислений за допомогою методу Монте-Карло: ", res_mc2)


# Обчислення інтеграла за допомогою scipy
res_scq, error = spi.quad(f, a, b)
print("Визначений інтеграл, обчисленний за допомогою scipy: ", res_scq)
