# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def solution(N, M):
    # Implement your solution here
    if N == 1:
        return 1
    return int(N / gcd(M , N))
