def knapsack_dp(items, capacity):
    dp = [0] * (capacity+1)
    for w, cost in items:
        for c in range(capacity, w-1,-1):
            dp[c] = max(dp[c], dp[c-w]+cost)
    return dp[capacity]
    
