import math
def solution(A):
    n = len(A)
    dictA = dict()
    dictB = dict()
    leader = [None] * (n-1)
    leader_B = [None] * (n-1)
    for i in range(n-1):
        if not A[i] in dictA:
            dictA[A[i]] = 0
        dictA[A[i]] += 1
        if dictA[A[i]] > math.floor((i+1) / 2):
            leader[i]=A[i]
        elif i>=1:
            if leader[i-1] != None:
                if dictA[leader[i-1]] > math.floor((i+1) / 2):
                    leader[i]=leader[i-1]
        ### For dict B
        if not A[n-1-i] in dictB:
            dictB[A[n-1-i]] = 0
        dictB[A[n-1-i]] += 1
        if dictB[A[n-1-i]] > math.floor((i+1) / 2):
                leader_B[i]=A[n-1-i]
        elif i>=1:
            if leader_B[i-1] != None:
                if dictB[leader_B[i-1]] > math.floor((i+1) / 2):
                    leader_B[i]=leader_B[i-1]     
    result = 0
    for i in range(n-1):
        if leader[i] == leader_B[n-2-i]:
            if leader[i] != None:
                result += 1
    return result
