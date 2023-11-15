from collections import deque

def get_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
                    moves.append(new_state)
                if i < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
                    moves.append(new_state)
                if j > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
                    moves.append(new_state)
                if j < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
                    moves.append(new_state)
    return moves

def solve_8_puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path

        visited.add(tuple(map(tuple, current_state)))

        for next_state in get_moves(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solve_8_puzzle(initial_state)
if solution:
    print("Solution steps:")
    for i, state in enumerate(solution):
        print(f"Step {i + 1}:")
        for row in state:
            print(row)
        print("------")
else:
    print("No solution found.")
