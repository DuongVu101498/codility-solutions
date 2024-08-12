# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    current_path = set()
    X_set = set(range(1, X+1))
    for i in range(len(A)):
        current_path.add(A[i])
        if current_path == X_set:
            return i
    return -1
