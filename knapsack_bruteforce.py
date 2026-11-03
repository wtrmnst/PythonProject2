def knapsack_bruteforce(items, capacity):
    def go(i, weight, cost):
        if weight > capacity:
            return 0
        if i == len(items):
            return cost
        w, c = items[i]
        return max(go(i+1, weight, cost),(go(i+1, weight + w, cost + c)))
    return go(0,0,0)
    
