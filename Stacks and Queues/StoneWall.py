# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # Implement your solution here
    n = len(H)
    stack = []
    result = 0
    for i in range(n):
        if i == 0:
            stack.append(H[i])
            result += 1
            continue
        if H[i] == stack[-1]:
            continue
        if H[i] > stack[-1]:
            stack.append(H[i])
            result += 1
            continue
        if H[i] < stack[-1]:
            while len(stack) > 0:
                if H[i] < stack[-1]:
                    stack.pop(-1)
                    continue
                elif H[i] > stack[-1]:
                    stack.append(H[i])
                    result += 1
                    break
                elif H[i] == stack[-1]:
                    break
            if len(stack) == 0:
                stack.append(H[i])
                result += 1
                continue
    return result

        
