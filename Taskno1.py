import tkinter as tk
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

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [''] * 9
        self.turn = 'X'
        self.buttons = []
        self.create_buttons()
        self.status_label = tk.Label(root, text="Player X's turn", font=('Helvetica', 14))
        self.status_label.pack(side="bottom")
        self.restart_button = None

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            button = tk.Button(frame, text='', font=('Helvetica', 20), width=5, height=2, command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == '' and self.turn == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X')
            self.turn = 'O'
            self.status_label.config(text="Computer's turn (O)")
            self.check_game_status()
            self.root.after(500, self.computer_move)

    def computer_move(self):
        move = best_move(self.board)
        if move != -1:
            self.board[move] = 'O'
            self.buttons[move].config(text='O')
            self.turn = 'X'
            self.status_label.config(text="Player X's turn")
        self.check_game_status()

    def check_game_status(self):
        winner = CheckWin(self.board)
        if winner:
            if winner == 'Tie':
                self.status_label.config(text="The game is a tie!")
            else:
                self.status_label.config(text=f"{winner} wins the game!")
            self.disable_buttons()
            self.show_restart_button()

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def show_restart_button(self):
        if not self.restart_button:
            self.restart_button = tk.Button(self.root, text="Restart Game", font=('Helvetica', 14), command=self.restart_game)
            self.restart_button.pack(side="bottom")

    def restart_game(self):
        self.board = [''] * 9
        self.turn = 'X'
        for button in self.buttons:
            button.config(text='', state="normal")
        self.status_label.config(text="Player X's turn")
        if self.restart_button:
            self.restart_button.pack_forget()
            self.restart_button = None

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
