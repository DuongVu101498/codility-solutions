def solution(A):
    # Implement your solution here
    n=len(A)
    if n <3:
        return 0
    A.sort()
    count = 0
    for i in range(n-2):
        last_index = i+2
        for j in range(i+1,n-1):
            if last_index > j + 1:
                count += (last_index - j - 1)
            k=max(last_index,j+1)
            while  k < n and A[i]+A[j] > A[k]:
                k += 1
                count += 1
            if k == n-1 and A[i]+A[j] > A[k]:
                last_index = n
            else:
                last_index = k          
    return count
