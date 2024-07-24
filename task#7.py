import random
import matplotlib.pyplot as plt

def roll_dice():
    """Генерує випадкові числа для двох кубиків і повертає їх суму."""
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    """Імітує кидання кубиків num_rolls разів і повертає ймовірності кожної суми."""
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll_sum = roll_dice()
        sum_counts[roll_sum] += 1
    
    probabilities = {s: count / num_rolls for s, count in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    """Будує графік ймовірностей для кожної суми."""
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(range(2, 13))
    plt.grid(True)
    plt.show()

def main():
    num_rolls = 100000  # Велика кількість кидків для точності
    probabilities = monte_carlo_simulation(num_rolls)
    plot_probabilities(probabilities)
    
    # Порівняння з аналітичними розрахунками
    analytical_probabilities = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    print("Симуляційні ймовірності:")
    for s in range(2, 13):
        print(f"Сума {s}: {probabilities[s]:.4f}")

    print("\nАналітичні ймовірності:")
    for s in range(2, 13):
        print(f"Сума {s}: {analytical_probabilities[s]:.4f}")

if __name__ == "__main__":
    main()

