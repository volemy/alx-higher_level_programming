#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at [row, col] on the board.

    Args:
        board (list): The current state of the board.
        row (int): The row to check for queen placement.
        col (int): The column to check for queen placement.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """
    Find and print all possible solutions to the N-Queens problem.

    Args:
        N (int): The size of the N×N chessboard and the number of queens.

    Prints:
        List of solutions, where each solution is a list of queen positions.
    """
    if N < 4:
        print("N must be at least 4")
        return

    def backtrack(row):
        if row == N:
            solutions.append([(i, board[i]) for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * N
    backtrack(0)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
