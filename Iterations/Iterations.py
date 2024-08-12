def solution(N):
    # Implement your solution here
    if  N == 0:
        return 0

    b_N = format(N, 'b')
    b_gap_current = 0
    b_gap_final = 0
    reset = False
    for index in range(1, len(b_N)):
        if b_N[index] == "1":
            if not reset :
                if b_gap_current > b_gap_final:
                    b_gap_final = b_gap_current
                b_gap_current = 0
                reset = True
        else:
            if reset:
                reset = False
            b_gap_current += 1
    return b_gap_final

print(solution(1376796946))
print(format(1376796946, 'b'))
