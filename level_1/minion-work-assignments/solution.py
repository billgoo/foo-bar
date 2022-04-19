def solution(data, n):
    # Your code here
    return [x for x in data if data.count(x) <= n]
