import math

def BoardPrint(board):
    symbols = [' ' if cell == '' else cell for cell in board]
    print(f"{symbols[0]} | {symbols[1]} | {symbols[2]}")
    print("--|---|--")
    print(f"{symbols[3]} | {symbols[4]} | {symbols[5]}")
    print("--|---|--")
    print(f"{symbols[6]} | {symbols[7]} | {symbols[8]}")

def CheckWin(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    if '' not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    winner = CheckWin(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    print("-----------------------------------------------------------------------")
    print("----------------------------Welcome In---------------------------------")
    print("--------------------------- Tic Tac Toe -------------------------------")
    print("--------------------------- Game(T T T) -------------------------------")
    print("-----------------------------------------------------------------------")

    board = [''] * 9
    turn = 'X'

    while True:
        BoardPrint(board)
        if turn == 'X':
            value = int(input("\nEnter the value (0-8): "))
            if board[value] == '':
                board[value] = 'X'
                turn = 'O'
            else:
                print("Invalid move! Try again.")
        else:
            print("\nComputer's turn (O):")
            move = best_move(board)
            board[move] = 'O'
            turn = 'X'

        winner = CheckWin(board)
        if winner:
            BoardPrint(board)
            if winner == 'Tie':
                print("\nThe game is a tie!")
            else:
                print(f"\n{winner} wins the game!")
            break

    print("Thanks For Playing ")

