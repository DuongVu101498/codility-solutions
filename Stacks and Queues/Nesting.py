# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def IsPair(char, target):
    if char == '(' and target == ')':
        return True
    return False

def solution(S):
    # Implement your solution here
    stack = [ None ]
    n = len(S)
    for i in range(n):
        if IsPair(S[n-1-i],stack[-1]):
            stack.pop(-1)
        else:
            stack.append(S[n-1-i])
    if len(stack) == 1:
        return 1
    else:
        return 0 
