# Вихідні дані про їжу:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Жадібний алгоритм:
def greedy_algorithm(items, budget):

    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for name, info in sorted_items:
        if info["cost"] <= remaining_budget:
            chosen_items.append(name)
            total_calories += info["calories"]
            remaining_budget -= info["cost"]

    return total_calories, budget - remaining_budget, chosen_items


# Динамічне програмування:
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            chosen_items.append(name)
            b -= items[name]["cost"]

    chosen_items.reverse()
    total_calories = dp[n][budget]
    used_budget = budget - b

    return total_calories, used_budget, chosen_items


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("\n")
    print("Жадібний алгоритм:")
    print(
        f"Калорії: {greedy_result[0]}, витрачено грошей: {greedy_result[1]}, вибрані страви: {greedy_result[2]}"
    )
    print("\n")
    print("Динамічне програмування:")
    print(
        f"Калорії: {dp_result[0]}, витрачено грошей: {dp_result[1]}, вибрані страви: {dp_result[2]}"
    )
    print("\n")
