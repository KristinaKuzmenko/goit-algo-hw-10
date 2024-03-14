## Завдання 1

Умови завдання:

- "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
- "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
- Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
- Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
- Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".
За допомогою бібліотеки Pulp побудовано модель максимізації кількості виробництва 2 видів продукції. До моделі додано обмеження використання ресурсів: води, лисонного соку та фруктового пюре. Обмеження використання цукру при виробництві А <= 50 не додавалось до системи обмежень, оскільки нерівність виконується при заданні обмеження використання лимонного соку А <= 30. Задача має один оптимальний розв'язок: оптимальна кількість виробництва лимонаду 30 одиниць, оптимальна кількість виробництва фруктового пюре 20 одиниць. Максимальна загальна кількість виробництва складає 50 одиниць продукції.

## Завдання 2
За допомогою методу Монте-Карло розраховано приблизне значення визначеного інтегралу функції. Площа криволінійної фігури буде розраховуватись як середнє значення функції, помножене на довжину інтервалу інтегрування. Середнє значення функції було розраховано як середнє арифметичне значень функції від випадково згенеровних і рівномірно розподілених значень аргументу функції в межах інтервалу інтегрування  (кількість згеенерованих значень задано 100000). Отримане значення визначеного інтервалу приблизно дорівнює значенню, розрахованому за допомогою scipy.integrate. При цьому, чим більше випадкових значень генерується, тим точніше отриманий результат. 

Отримані розрахунки також співпадають з аналітичним розв'язком:
- первісна від функції $f(x) = 4 x ^ 3 - 5 x + 15 $

  $F(x) = x ^ 4 - \frac{5}{2} x ^ 2 + 15 x + C$
- визначений інтеграл даної функції на проміжку від 0 до 2 складає

  $F(2) - F(0) = 2 ^ 4 - \frac{5}{2}  * 2 ^ 2 + 15 * 2 - 0 = 36$
