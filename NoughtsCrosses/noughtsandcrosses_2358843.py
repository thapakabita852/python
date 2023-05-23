import random
import os.path #not needed in this case as file is in same folder
import json

random.seed()

def draw_board(board):
    """
    Draws the board on the console.
    """
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def welcome(board):
    """
    Prints the welcome message and draws the board.
    """
    print("Welcome to the 'Unbeatable Noughts and Crosses' game!")
    draw_board(board)

def initialise_board(board):
    """
    Sets all elements of the board to one space ' '.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Asks the user for the cell to put the X in, and returns row and col.
    """
    while True:
        try:
            move = int(input("Enter cell number (1-9): "))
            if move < 1 or move > 9:
                print("Invalid cell number. Please try again.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] != ' ':
                print("That cell is already occupied. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return row, col

def choose_computer_move(board):
    # check if any row, column or diagonal is about to win for the computer
    for mark in ['O', 'X']:
        for row in range(3):
            if board[row][0] == mark and board[row][1] == mark and board[row][2] == ' ':
                return row, 2
            elif board[row][0] == mark and board[row][2] == mark and board[row][1] == ' ':
                return row, 1
            elif board[row][1] == mark and board[row][2] == mark and board[row][0] == ' ':
                return row, 0

        for col in range(3):
            if board[0][col] == mark and board[1][col] == mark and board[2][col] == ' ':
                return 2, col
            elif board[0][col] == mark and board[2][col] == mark and board[1][col] == ' ':
                return 1, col
            elif board[1][col] == mark and board[2][col] == mark and board[0][col] == ' ':
                return 0, col

        if board[0][0] == mark and board[1][1] == mark and board[2][2] == ' ':
            return 2, 2
        elif board[0][0] == mark and board[2][2] == mark and board[1][1] == ' ':
            return 1, 1
        elif board[1][1] == mark and board[2][2] == mark and board[0][0] == ' ':
            return 0, 0

        if board[0][2] == mark and board[1][1] == mark and board[2][0] == ' ':
            return 2, 0
        elif board[0][2] == mark and board[2][0] == mark and board[1][1] == ' ':
            return 1, 1
        elif board[1][1] == mark and board[2][0] == mark and board[0][2] == ' ':
            return 0, 2
    
    # If no winning move, choose a random cell
    random.seed()
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    """
    Checks if either the player or the computer has won.
    Returns True if someone won, False otherwise.
    """
    for i in range(3):
        # Check for horizontal win
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
        # Check for vertical win
        elif board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True
    # Check for diagonal win
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    """
    Checks if all cells are occupied.
    Returns True if it is, False otherwise.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    # Set board cells to all single spaces ' '
    initialise_board(board)
    
    # Draw the board
    draw_board(board)
    
    while True:
        # Get player move
        print("Your turn (X)")
        row, col = get_player_move(board)
        board[row][col] = 'X'
        
        # Draw the board after player move
        draw_board(board)
        
        # Check for player win
        if check_for_win(board, 'X'):
            return 1
        
        # Check for draw
        if check_for_draw(board):
            return 0
        
        # Choose computer move
        print("Computer's turn (O)")
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        
        # Draw the board after computer move
        draw_board(board)
        
        # Check for computer win
        if check_for_win(board, 'O'):
            return -1
        
        # Check for draw
        if check_for_draw(board):
            return 0

def menu():
    choice = input("Enter your choice: \n1 - Play the game\n2 - Save score in file 'leaderboard.txt'\n3 - Load and display the scores from the 'leaderboard.txt'\nq - End the program\n1, 2, 3 or q? \n")
    
    return choice

def load_scores():
    leaders = {}
    try:
        with open('leaderboard.txt', 'r') as f:
            leaders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, return an empty dictionary
        pass
    return leaders

    
def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)
        
def display_leaderboard(leaders):
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")





