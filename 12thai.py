def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")


tic_tac_toe()
