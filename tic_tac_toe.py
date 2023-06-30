def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return (any(all(cell == player for cell in row) for row in board) or
            any(all(row[i] == player for row in board) for i in range(3)) or
            all(board[i][i] == player for i in range(3)) or
            all(board[i][2-i] == player for i in range(3)))

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    # Initialize the game board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Define the players
    players = ['X', 'O']

    # Game loop
    for turn in range(9):
        print_board(board)
        
        # Current player
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn")

        # Player makes a move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                
                # Check if the cell is empty
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers 0, 1, or 2.")
        
        # Check for a win or tie
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            return

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
