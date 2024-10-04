import random

def create_hopscotch_board():
    """Creates a simple hopscotch board."""
    board = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ]
    return board

def print_board(board):
    """Prints the hopscotch board."""
    for row in board:
        print(" | ".join(map(str, row)))

def play_hopscotch():
    """Plays a simple text-based hopscotch game."""
    board = create_hopscotch_board()
    print_board(board)

    position = 0
    while position < 10:
        try:
            move = int(input("Enter a number to hop to: "))
            if move in board[position // 2]:
                position = move
                print("You hopped to:", position)
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Congratulations! You reached the end of the hopscotch board!")

if __name__ == "__main__":
    play_hopscotch()
