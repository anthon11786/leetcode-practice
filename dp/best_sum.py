"""
Write a funciton 'best_sum(target_sum ,numbers) that takes in a targetsum and 
an array of numbers as arguments. 

The funciton should return an array containing the shortest combination of 
numbers that add up to exactly the target sum. 

if there is a tie for shortest combination, retunr any one of the shortest 
"""


def best_sum(target_sum, numbers, memo):
    """
    """
    #  base cases
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    shortest_combo = None  # reason start none -> if isn't any way to gen target

    # branch logic
    for num in numbers:
        remainder = target_sum - num
        res = best_sum(remainder, numbers, memo)

        if res is not None:
            curr_combo = res + [num]  # linear time operation
            # First time find one the shortest_combo will be null
            if shortest_combo is None or (len(curr_combo) < len(shortest_combo)):
                shortest_combo = curr_combo
                memo[target_sum] = shortest_combo

    return shortest_combo


# m = target_sum
# n = len(numbers)

# Brute Force
# Time: O(n^m * m)  Usually branching factor ^ tree height
# Space: O(m^2)  Usually just the height of the recursion, i.e. m
# Every recursive call needs shortest_combo so m (for stack depth) * m (store array per recrusive call)

# Memoization
# Time: O(n*m^2)
# Space: O(m^2)

print(best_sum(7, [5, 3, 4, 7], {}))
print(best_sum(8, [2, 3, 5], {}))
print(best_sum(8, [1, 4, 5], {}))
print(best_sum(100, [1, 2, 5, 25], {}))
