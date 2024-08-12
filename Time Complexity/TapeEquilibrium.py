def solution(A):
    # Implement your solution here
    N = len(A)
    P = [0] * (N-1)
    sum_slice_A = 0
    sumA=sum(A)
    for i in range(1, N):
        if i == 1:
            sum_slice_A = A[i-1]
        else:
            sum_slice_A = sum_slice_A + A[i-1]
        #print("sum_slice_A: ",sum_slice_A)
        #print("A[i-1]: ",A[i-1])
        P[i-1] = abs(sumA - 2*sum_slice_A)
    return min(P)
