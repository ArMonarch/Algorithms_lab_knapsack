def knapsack_fractional_greedy(weights: list[int], values: list[int], capacity: int):
    """
    Solves the Fractional Knapsack problem using the greedy method.
    Arguments:
        weights : List[int] : A list of weights of the items.
        values  : List[int] : A list of values of the items.
        capacity : int : Maximum weight the knapsack can carry.
    Returns:
        float : Maximum value that can be obtained within the given capacity.
    """
    n = len(weights)

    # Calculate value-to-weight ratio for each item
    ratios: list[tuple[float, int]] = [(values[i] / weights[i], i) for i in range(0, n)]

    # Sort items by the ratio in descending order
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    remaining_capacity = capacity
    
    # Go through sorted items and take as much as possible
    for _, index in ratios:
        if weights[index] <= remaining_capacity:
            # Take the whole item
            total_value += values[index]
            remaining_capacity -= weights[index]
        else:
            # Take the fractional part of the item
            total_value += values[index] * (remaining_capacity / weights[index])
            break  # No more items can be taken, the knapsack is full

    return total_value


# Test the Greedy Fractional Knapsack
if __name__ == "__main__":
    # Test case for Fractional Knapsack
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print("Maximum value (Fractional Knapsack - Greedy):", knapsack_fractional_greedy(weights, values, capacity))
