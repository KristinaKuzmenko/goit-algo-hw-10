import pulp


model = pulp.LpProblem(name="Maximalize quantity", sense=pulp.LpMaximize)


# Визначення змінних
A = pulp.LpVariable("A", lowBound=0, cat="Integer")  # Кількість лимонаду
B = pulp.LpVariable("B", lowBound=0, cat="Integer")  # Кількість фруктового пюре

# Функція цілі (Максимізація прибутку)
model += A + B, "Production volume"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження води
model += 1 * A <= 30  # Обмеження лимонного соку
model += 2 * B <= 40  # Обмеження фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Status: ", pulp.LpStatus[model.status])

for v in model.variables():
    print(f"Optimal quantity of  {v.name} = {v.varValue}")

print("The optimal value of the objective function is = ", pulp.value(model.objective))
