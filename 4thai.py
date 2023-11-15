from itertools import permutations

def solve_cryptarithmetic():
    for perm in permutations('0123456789', 10):
        mapping = { 'S': perm[0], 'E': perm[1], 'N': perm[2], 'D': perm[3], 'M': perm[4], 'O': perm[5], 'R': perm[6], 'Y': perm[7] }

        if '0' in (mapping['S'], mapping['M']):  
            continue

        send = int(''.join(str(mapping[c]) for c in 'SEND'))
        more = int(''.join(str(mapping[c]) for c in 'MORE'))
        money = int(''.join(str(mapping[c]) for c in 'MONEY'))

        if send + more == money:
            print(f"Solution found: SEND = {send}, MORE = {more}, MONEY = {money}")
            break
    else:
        print("No solution found.")

solve_cryptarithmetic()
