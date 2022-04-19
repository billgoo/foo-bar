Minion Work Assignments
=======================
Just *Brute Force* remove the elements that occur more than **n** times.

Time Complexity: $O(n^2)$
Space Complexity: $O(n)$

Solution:
```python
def solution(data, n):
    # Your code here
    return [x for x in data if data.count(x) <= n]
```
