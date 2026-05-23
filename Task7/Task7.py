import random
import matplotlib.pyplot as plt


def monte_carlo_dice(num_trials):
    # всі можливі суми (2–12)
    counts = {i: 0 for i in range(2, 13)}

    # симуляція кидків
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1

    # переводимо у ймовірності
    probabilities = {k: v / num_trials for k, v in counts.items()}

    return probabilities


def theoretical_probabilities():
    # аналітичні значення (36 комбінацій)
    return {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }


def print_table(mc, theo):
    print("Сума | Монте-Карло | Теорія")
    print("-" * 35)
    for s in range(2, 13):
        print(f"{s:>4} | {mc[s] * 100:10.2f}% | {theo[s] * 100:7.2f}%")


def plot_results(mc, theo):
    sums = list(range(2, 13))

    mc_values = [mc[s] for s in sums]
    theo_values = [theo[s] for s in sums]

    plt.plot(sums, mc_values, marker="o", label="Monte Carlo")
    plt.plot(sums, theo_values, marker="s", label="Theoretical")

    plt.xlabel("Sum of dice")
    plt.ylabel("Probability")
    plt.title("Dice roll probabilities: Monte Carlo vs Theory")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    trials = 100000  # чим більше — тим точніше

    mc = monte_carlo_dice(trials)
    theo = theoretical_probabilities()

    print_table(mc, theo)
    plot_results(mc, theo)


if __name__ == "__main__":
    main()