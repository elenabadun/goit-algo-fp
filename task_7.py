import random
import matplotlib.pyplot as plt


# Симуляція кидків:
def simulate_dice_rolls(num_rolls):
    results = []

    for _ in range(num_rolls):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2
        results.append(total)

    # Підрахунок кількості кожної суми:

    sum_count = {}
    for total in range(2, 13):
        sum_count[total] = results.count(total)

    # Обчислення ймовірностей
    probabilities = {}
    for total in sum_count:
        probabilities[total] = sum_count[total] / num_rolls

    return probabilities


def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    plt.bar(sums, probs, tick_label=sums, color="darkgreen")
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title(f"Ймовірність суми чисел (Кількість кидків: {num_rolls})")

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center")

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        for total in sorted(probabilities):
            print(f"Сума {total}: {probabilities[total]*100:.2f}%")

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities, accuracy)

        """
        Результати, отримані за допомогою методу Монте-Карло, добре узгоджуються з аналітичними розрахунками з таблиці. 
        Імовірності, знайдені в симуляції, наближаються до теоретичних значень, особливо при великій кількості кидків. 
        Але варто зазначити, що цей метод не є абсолютно точним. Через випадковий характер моделювання можливі 
        незначні відхилення, особливо при невеликій кількості повторень.
        """
