def print_board(board):
    """Prints the Sudoku board."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def is_valid(board, row, col, num):
    """Checks if it will be legal to assign num to the given row,col."""
    # Check the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check the box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    """Solves the Sudoku using backtracking."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True

def play_game(board):
    """Allows the user to play the Sudoku game."""
    while True:
        print_board(board)
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))
        
        if board[row][col] != 0:
            print("Position already filled. Try again.")
            continue
        
        if is_valid(board, row, col, num):
            board[row][col] = num
            if is_solved(board):
                print_board(board)
                print("Congratulations! You solved the Sudoku.")
                break
        else:
            print("Invalid move. Try again.")

def is_solved(board):
    """Checks if the Sudoku is solved."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku automatically
# solve_sudoku(board)
# print_board(board)

# Play the game interactively
play_game(board)

