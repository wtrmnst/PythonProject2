def greedy_knapsack(items, capacity):
    total_weight = 0
    total_cost = 0
    for w, c in sorted(items, key=lambda item: item[1], reverse=True):
        if total_weight + w <= capacity:
            total_weight += w
            total_cost += c 
    return total_cost
    
