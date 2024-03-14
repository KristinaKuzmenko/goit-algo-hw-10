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
plt.grid()
plt.show()


# Обчислення інтеграла за допомогою методу монте-карло
def monte_carlo_integration(f, a, b, n):
    x = [random.uniform(a, b) for _ in range(n)]
    y = [f(x_i) for x_i in x]
    y_mean = sum(y) / n
    return (b - a) * y_mean


result = monte_carlo_integration(f, a, b, 100000)
print("Інтеграл, обчисленний за допомогою методу Монте-Карло: ", result)


# Обчислення інтеграла за допомогою scipy
a = 0  # нижня межа
b = 2  # верхня межа

result, error = spi.quad(f, a, b)

print("Інтеграл, обчисленний за допомогою scipy: ", result)
