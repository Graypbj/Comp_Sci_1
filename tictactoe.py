import os
# Create board array
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Start with X as the first player
current_player = "X"

# No one has won yet so initialize that condition as False. Later it could be X or O
winner = None

# While no one has one the game should continue to run
game_running = True


# Print board function that takes board as an input
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Get player input
def player_input(board):
    grid_number: int = int(input("Enter a number 1-9: "))
    if grid_number >= 1 and grid_number <= 9 and board[grid_number - 1] == "-":
        board[grid_number - 1] = current_player
    else:
        print("This position is already taken or you choose an invalid number")


# Check to see if anyone has won
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    if board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    if board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[4]
        return True
    if board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("Tie")
        game_running = False


def check_win():
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board) == True:
        print_board(board)
        print(f"The winner is {winner}")
        game_running = False


# Switch players
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
        os.system('clear')
    else:
        current_player = "X"
        os.system('clear')


# Check to see if anyone has won
while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
