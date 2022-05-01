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