items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

# Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості.
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    # Вибираємо страви, поки бюджет дозволяє
    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_calories += details["calories"]
            total_cost += details["cost"]

    # Обчислюємо залишок бюджету
    remaining_budget = budget - total_cost
    return selected_items, total_calories, total_cost, remaining_budget

# Алгоритм динамічного програмування для оптимального вибору страв
def dynamic_programming(items, budget):
    # Отримуємо список назв, вартостей і калорійностей
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(items)

    # Створюємо таблицю для динамічного програмування
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибрані страви
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    # Обчислюємо сумарну калорійність, вартість і залишок бюджету
    total_calories = dp[n][budget]
    total_cost = budget - w
    remaining_budget = w
    return selected_items, total_calories, total_cost, remaining_budget


# Приклад виклику функцій
budget = 100

# Жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Сумарна калорійність: {greedy_result[1]}")
print(f"Загальна вартість: {greedy_result[2]}")
print(f"Залишок бюджету: {greedy_result[3]}")

# Динамічне програмування
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print(f"Вибрані страви: {dp_result[0]}")
print(f"Сумарна калорійність: {dp_result[1]}")
print(f"Загальна вартість: {dp_result[2]}")
print(f"Залишок бюджету: {dp_result[3]}")