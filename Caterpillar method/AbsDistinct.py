# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    result = set()
    for i in range(len(A)):
        result.add(abs(A[i]))
    return len(result)
