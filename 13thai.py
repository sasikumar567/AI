import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                cells.append((i, j))
    return cells

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, 'X'):
        return -10 + depth
    if check_winner(board, 'O'):
        return 10 - depth
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = 'O'
            eval = alpha_beta(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = 'X'
            eval = alpha_beta(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_eval = -math.inf
    best_move = (-1, -1)
    alpha = -math.inf
    beta = math.inf
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = 'O'
        eval = alpha_beta(board, 0, alpha, beta, False)
        board[i][j] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move = int(input("Enter your move (1-9): "))
        row = (player_move - 1) // 3
        col = (player_move - 1) % 3

        if board[row][col] == ' ':
            board[row][col] = 'X'

            if check_winner(board, 'X'):
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            computer_move = best_move(board)
            board[computer_move[0]][computer_move[1]] = 'O'

            print("Computer's move:")
            print_board(board)

            if check_winner(board, 'O'):
                print("Computer wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
        else:
            print("That position is already taken. Try again.")

tic_tac_toe()
