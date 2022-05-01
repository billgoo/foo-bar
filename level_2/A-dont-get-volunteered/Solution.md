Minion Work Assignments
=======================

It is a simple *DP* with memo.

1. Step 1

    Sort the input `L` in **descending order**.

2. Step 2: Iteration

    From largest number to smallest number, each step we need to maintain the max value, the remainder of which divided by 3 is 0, 1 and 2.

    Base case:

    ```python
    max_value_0 % 3 == 0
    max_value_1 % 3 == 1
    max_value_2 % 3 == 2
    ```

    State transition equation:

    ```python
    max_value_0 = max(prev_max_value_0, 10 * prev_max_value_0 + current_digit)
    max_value_1 = max(prev_max_value_1, 10 * prev_max_value_1 + current_digit)
    max_value_2 = max(prev_max_value_2, 10 * prev_max_value_2 + current_digit)
    ```

3. Find end point

    Find final `max_value_0` is the end point of *DP*.

Time Complexity: $O(n)$
Space Complexity: $O(1)$

Solution:

```python
def solution(l):
    # Your code here
    # map of result for three remainders
    dp = {0: 0, 1: 0, 2: 0}
    for d in sorted(l, reverse=True):
        for remainder, max_value in dp.items():
            new_value = 10 * max_value + d
            r = new_value % 3   # new remainder
            if dp[r] < new_value:
                # update max value in this remainder
                dp[r] = new_value
    return dp[0]
```
