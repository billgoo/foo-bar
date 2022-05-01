Minion Work Assignments
=======================

Just *Brute Force* count the results by using a *hash map*.

Time Complexity: $O(n^2)$
Space Complexity: $O(n)$

Solution:

```python
def solution(l):
    # Your code here
    result = 0
    n = len(l)
    lucky_tuple_count = [0 for _ in range(n)]

    # find tuple i, j
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if l[j] % l[i] == 0:
                lucky_tuple_count[j] += 1

    # find tuple j, k
    for j in range(1, n - 1):
        for k in range(j + 1, n):
            if l[k] % l[j] == 0:
                result += lucky_tuple_count[j]

    return result
```
