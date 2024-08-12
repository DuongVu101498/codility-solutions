def solution(A):
    # Implement your solution here
    slim_A = [ num for num in A if num > 0]
    n=len(slim_A)
    if n <3:
        return 0
    slim_A.sort()
    for i in range(n-2):
        if slim_A[i]+slim_A[i+1]>slim_A[i+2]:
            return 1
    return 0
