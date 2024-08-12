def solution(A, K):
    temp_array = [0] * len(A)
    rotate_index = [0] * len(A)
    for i in range (0, len(A)):
        rotate_index[i] =  (i  + K) % len(A)
    for i in range (0, len(A)):
        temp_array[rotate_index[i]] = A[i]
    return temp_array
