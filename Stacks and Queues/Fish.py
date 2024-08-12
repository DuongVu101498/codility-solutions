# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    stack = [None]
    n = len(A)
    for i in range(n):
        #print(stack)
        if len(stack) == 1:
            #print("here 1")
            stack.append(n-1-i)
            continue
        if B[stack[-1]] == 1:
            #print("here 2")
            stack.append (n-1-i)
            continue
        if B[n-1-i] == 0 and B[stack[-1]] == 0:
            #print("here 3")
            stack.append (n-1-i)
            continue
        if B[n-1-i] == 1 and B[stack[-1]] == 0:
            #print("here 4")
            while True:
                if len(stack) == 1:
                    stack.append (n-1-i)
                    break
                elif B[stack[-1]] == 1:
                    stack.append (n-1-i)
                    break
                elif A[n-1-i] > A[stack[-1]]:
                    stack.pop()
                elif A[n-1-i] < A[stack[-1]]:
                    break
    return len(stack)-1


