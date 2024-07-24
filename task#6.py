def greedy_algorithm(items, budget):
    ratios = {item: values["calories"] / values["cost"] for item, values in items.items()}
    
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, _ in sorted_items:
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_calories += calories
    
    return selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print("Жадібний алгоритм:", greedy_algorithm(items, budget))

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_choice = [[0] * (budget + 1) for _ in range(len(items))]
    
    items_list = list(items.keys())
    
    for i, item in enumerate(items_list):
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        
        for j in range(budget, cost - 1, -1):
            if dp[j - cost] + calories > dp[j]:
                dp[j] = dp[j - cost] + calories
                item_choice[i][j] = 1
    
    selected_items = []
    w = budget
    for i in range(len(items_list) - 1, -1, -1):
        if item_choice[i][w] == 1:
            selected_items.append(items_list[i])
            w -= items[items_list[i]]["cost"]
    
    return selected_items

print("Динамічне програмування:", dynamic_programming(items, budget))
