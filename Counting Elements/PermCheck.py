# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    set_A = set(range(1, len(A)+1))
    actual_set = set(A)
    if set_A == actual_set:
        return 1
    else:
        return 0
