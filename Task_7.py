import random
import matplotlib.pyplot as plt
from collections import Counter

def monte_carlo_simulation(num_rolls):
    # Ініціалізація підрахунку сум
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]
    counts = Counter(sums)

    # Обчислення ймовірностей
    probabilities = {s: (counts[s] / num_rolls) * 100 for s in range(2, 13)}
    return probabilities

def analytical_probabilities():
    # Табличні аналітичні ймовірності
    total_outcomes = 36
    probabilities = {
        2: 1 / total_outcomes,
        3: 2 / total_outcomes,
        4: 3 / total_outcomes,
        5: 4 / total_outcomes,
        6: 5 / total_outcomes,
        7: 6 / total_outcomes,
        8: 5 / total_outcomes,
        9: 4 / total_outcomes,
        10: 3 / total_outcomes,
        11: 2 / total_outcomes,
        12: 1 / total_outcomes,
    }
    return {k: v * 100 for k, v in probabilities.items()}

def plot_results(mc_probs, an_probs):
    # Побудова графіків
    labels = list(mc_probs.keys())
    mc_values = list(mc_probs.values())
    an_values = list(an_probs.values())

    x = range(len(labels))

    plt.bar(x, mc_values, width=0.4, label="Monte Carlo", align="center", alpha=0.7)
    plt.bar([i + 0.4 for i in x], an_values, width=0.4, label="Analytical", align="center", alpha=0.7)

    plt.xticks([i + 0.2 for i in x], labels)
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.legend()
    plt.show()

def main():
    num_rolls = 1000000  # Кількість ітерацій симуляції
    mc_probs = monte_carlo_simulation(num_rolls)
    an_probs = analytical_probabilities()

    # Виведення результатів
    print("Результати Монте-Карло:")
    for s, p in mc_probs.items():
        print(f"Сума {s}: {p:.2f}%")
    
    print("\nАналітичні ймовірності:")
    for s, p in an_probs.items():
        print(f"Сума {s}: {p:.2f}%")

    # Побудова графіка
    plot_results(mc_probs, an_probs)

if __name__ == "__main__":
    main()