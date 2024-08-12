# you can write to stdout for debugging purposes, e.g.
# (6, [3, 4, 5, 5, 2, 3, 4, 5, 6,4,2,6])
def solution(M, A):
    # Implement your solution here
    n = len(A)
    result = 0
    last_index = 0
    pre_last_index = 0
    temp = dict()
    for i in range(n):
        if not A[i]  in temp:
            result += i - last_index + 1
            temp[A[i]] = i
        else:
            pre_last_index = last_index
            last_index = temp[A[i]] + 1
            #print(temp)
            for j in range(pre_last_index, last_index):
                temp.pop(A[j])
                #print("here",temp)
            #print(temp)
            temp[A[i]] = i
            result += i - last_index + 1
    if result > 1000000000:
        return 1000000000
    return result
        
