
# from functools import cache


def how_sum(target_sum, numbers, memo):
    """

    """
    # if memo is None:
    #     memo = {}
    # Base cases
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    # Branching logic
    for num in numbers:
        remainder = target_sum - num
        # same numbers array because can reuse #'s
        res = how_sum(remainder, numbers, memo)
        if res is not None:
            # Early return because can return any valid combo
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # Python nuance ! use '+' to concatenate lists not .append()
            memo[target_sum] = res + [num]
            return memo[target_sum]

    memo[target_sum] = None
    return None

# Time Complexity
# m = target sum
# n = numbers.length

# Memoization
# Time: O()
# Space: O(m)


print(how_sum(7, [2, 3], {}))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7], {}))  # [4, 3]
print(how_sum(7, [2, 4], {}))  # null
print(how_sum(8, [2, 3, 5], {}))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14], {}))  # null


@cache
def how_sum_cached(target_sum, numbers):
    """

    """
    # Base cases
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    # Branching logic
    for num in numbers:
        remainder = target_sum - num
        # same numbers array because can reuse #'s
        res = how_sum(remainder, numbers)
        if res is not None:
            # Early return because can return any valid combo
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # Python nuance ! use '+' to concatenate lists not .append()
            return res + [num]

    return None


print(how_sum_cached(300, [7, 14]))  # null
