use std::cmp::max;

/// A naive recursive implementation of 0-1 Knapsack Problem
pub fn knapsack(capacity: i32, weights: &[i32], values: &[i32], counter: usize) -> i32 {
    // base case
    if counter == 0 || capacity == 0 {
        return 0;
    }

    // if weight of the nth element is greater than than knapsack capacity. then this item cannot
    // be included in the optimal solution.
    //
    // else return the maximum of the two cases:
    // - nth item included
    // - nth item not included OR without nth item
    if weights[counter - 1] > capacity {
        return knapsack(capacity, weights, values, counter - 1);
    } else {
        let left_capacity = capacity - weights[counter - 1];
        // calculate with the nth item included
        let new_value_included =
            values[counter - 1] + knapsack(left_capacity, weights, values, counter - 1);
        // calculate without the item included
        let without_new_value = knapsack(capacity, weights, values, counter - 1);
        return max(new_value_included, without_new_value);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_knapsack_basic() {
        let weights: Vec<i32> = vec![25, 84, 31, 16, 45, 9, 75, 15, 32, 24];
        let values: Vec<i32> = vec![87, 95, 24, 30, 46, 18, 68, 69, 48, 15];
        let knapsack_capacity: i32 = 180;
        let total_value: i32 = knapsack(knapsack_capacity, &weights, &values, 10);
        println!("{}", total_value);
    }
}

fn main() {}
