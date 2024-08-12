def solution(A):
    # Implement your solution here
    n = len(A)
    missing = [True] * (n+1)
    #print(missing)
    #print(len(missing))
    for i in range(n):
        #print(A[i])
        missing[A[i]-1] = False
    for i in range(n+1):
        if missing[i]:
            return i+1
