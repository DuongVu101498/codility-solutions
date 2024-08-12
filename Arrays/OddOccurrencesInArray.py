def solution(A):
    # Implement your solution here
    count_A = dict()
    for i in range(len(A)):
        if A[i] in count_A:
            count_A[A[i]] += 1
        else:
            count_A[A[i]] = 1
        #print(count_A)
    for num in count_A:
        if count_A[num] % 2 == 1:
            return num
