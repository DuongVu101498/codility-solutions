# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter
def solution(N, A):
    last_max = 0
    last_max_index = -1
    # Implement your solution here
    for i in range(len(A)):
        if A[i] != N+1:
            continue
        else:
            if i == 0:
                last_max_index = i
                continue
            elif last_max_index + 1 == i:
                last_max_index = i
                continue
            else:
                tmp_offset = Counter(A[last_max_index+1:i])
                # print("tmp_offset",tmp_offset)
                # print("last_max_index",last_max_index)
                last_max += max([tmp_offset[counter] for counter in tmp_offset])
                last_max_index = i
    if last_max_index == len(A) - 1:
        return [last_max] * N
    else:
        currnet_offset = Counter(A[last_max_index + 1:])
        result = [last_max] * N
        for counter in currnet_offset:
            result[counter-1] += currnet_offset[counter]
        return result
