def solution(A):
    if len(A) <= 1:
        return 0
    max_profit = 0
    current_min = A[0]
    for i in range(1,len(A)):
        if A[i] >= A[i-1]:
            continue
        else:
            if A[i-1] - current_min > max_profit:
                max_profit = A[i-1] - current_min
            if current_min > A[i]:
                current_min = A[i]
    if A[-1] - current_min > max_profit:
        max_profit = A[-1] - current_min
    return max_profit
