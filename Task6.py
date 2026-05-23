def greedy_algorithm(items, budget):
    ratio_items = [
        (v["calories"] / v["cost"], k, v["cost"], v["calories"])
        for k, v in items.items()
    ]

    ratio_items.sort(reverse=True, key=lambda x: x[0])

    total_cost = 0
    result = []
    total_calories = 0

    for ratio, name, cost, calories in ratio_items:
        if total_cost + cost <= budget:
            result.append(name)
            total_cost += cost
            total_calories += calories

    return result, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= cost:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + calories)

    w = budget
    result = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            result.append(name)
            w -= items[name]["cost"]

    return result[::-1], dp[n][budget]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 80

    print("Greedy:", greedy_algorithm(items, budget))
    print("DP:", dynamic_programming(items, budget))


if __name__ == "__main__":
    main()