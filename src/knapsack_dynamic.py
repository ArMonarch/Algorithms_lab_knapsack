def knapsack_01_dynamic(weights: list[int], values: list[int], capacity: int):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    Arguments:
        weights : List[int] : A list of weights of the items.
        values  : List[int] : A list of values of the items.
        capacity : int : Maximum weight the knapsack can carry.
    Returns:
        int : Maximum value that can be obtained within the given capacity.
    """
    n = len(weights)

    # Initialize the DP table with 0s
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:  # Item i can be included in the knapsack
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:  # Item i cannot be included in the knapsack
                dp[i][w] = dp[i-1][w]

    # The maximum value is at dp[n][capacity]
    return dp[n][capacity]

# Test the 0/1 Knapsack with dynamic programming
if __name__ == "__main__":
    # Test case for 0/1 Knapsack
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print("Maximum value (0/1 Knapsack - Dynamic Programming):", knapsack_01_dynamic(weights, values, capacity))
