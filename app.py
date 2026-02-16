import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("N-Queen Visualization (Backtracking)")

st.write("This app visualizes the N-Queen problem using Backtracking.")

# Safety Check
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


# Solve N-Queen
def solve_n_queens(board, row, n, steps):
    if row == n:
        steps.append(board.copy())
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            steps.append(board.copy())

            if solve_n_queens(board, row + 1, n, steps):
                return True

            board[row] = -1
            steps.append(board.copy())

    return False


# Draw Board
def draw_board(board, n):
    fig, ax = plt.subplots(figsize=(5, 5))

    chess = (np.indices((n, n)).sum(axis=0) % 2)
    ax.imshow(chess, cmap="gray", vmin=0, vmax=1)

    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="black", linewidth=1)

    ax.set_xticks([])
    ax.set_yticks([])

    for r, c in enumerate(board):
        if c != -1:
            ax.text(c, r, "♕", ha="center", va="center",
                    fontsize=28, color="red")

    return fig


# User Input
n = st.number_input("Enter value of N:", min_value=4, max_value=10, value=4)

if st.button("Start Visualization"):
    board = [-1] * n
    steps = []

    solve_n_queens(board, 0, n, steps)

    placeholder = st.empty()

    for step in steps:
        fig = draw_board(step, n)
        placeholder.pyplot(fig)
        time.sleep(0.6)
