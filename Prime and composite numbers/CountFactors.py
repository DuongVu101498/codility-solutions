# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def find_first_primary_factor(N):
    if N == 2 or N == 3 or N == 5:
        return N
    for i in range(2,int(N/2)+1):
        if i > int(math.sqrt(N)):
            return N
        elif N % i == 0:
            return i
def find_all_primary_factor(N): #not count 1 and N
    dict_N = dict()
    remain_N=N
    N_first_primary_factor = find_first_primary_factor(remain_N)
    while remain_N != N_first_primary_factor:
        if not N_first_primary_factor in dict_N:
            dict_N[N_first_primary_factor] = 1
        else: 
            dict_N[N_first_primary_factor] += 1
        remain_N = remain_N / N_first_primary_factor
        N_first_primary_factor = find_first_primary_factor(remain_N)
    if not remain_N in dict_N:
        dict_N[remain_N] = 1
    else:
        dict_N[remain_N] += 1
    return dict_N
def solution(N):
    if N == 1:
        return 1
    dict_N = find_all_primary_factor(N)
    #print(dict_N)
    if N in dict_N:
        return 2
    count = 1
    for factor in dict_N:
        count = count*(dict_N[factor]+1)
    return count
