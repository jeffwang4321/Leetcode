from typing import List

"""
Problem: Simulate Falling Objects

Given a 2D matrix matrix representing a field with an object and obstacles, simulate the falling 
the object until they either reach the bottom of the matrix or stop due to hitting obstacles.
F is a fixed shape falling object

Matrix Representation:

'-': An empty cell.
'F': A cell containing the falling object.
'#': A cell containing an obstacle.

"""


def simulate_fall(matrix: List[List[str]]) -> List[List[str]]:
    # matrix = [row[:] for row in matrix]  # Create a copy of the matrix
    while True:
        shape = get_shape(matrix)
        if not shape:  # If shape is empty,
            break
        if can_fall(matrix, shape):
            move_shape(matrix, shape)
        else:
            break
    return matrix


def can_fall(matrix, shape):
    rows = len(matrix)
    for row, col in shape:
        if row + 1 >= rows or matrix[row + 1][col] == "#":
            return False
    return True


def move_shape(matrix, shape):  # Move shape down by 1 unit
    # Clear current shape positions
    for row, col in shape:
        matrix[row][col] = "-"
    # Place shape in the new position
    for row, col in shape:
        matrix[row + 1][col] = "F"


def get_shape(matrix):  # Get the index positions of the falling shape
    return [(row, col) for row in range(len(matrix)) for col in range(len(matrix[0])) if matrix[row][col] == "F"]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()


def simulate_fall2(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    while True:
        shape = [(row, col) for row in range(ROWS) for col in range(COLS) if matrix[row][col] == "F"]
        if not shape:  # If shape is empty,
            break

        can_fall = True
        for row, col in shape:
            if row + 1 >= ROWS or matrix[row + 1][col] == "#":
                can_fall = False

        if can_fall:
            for row, col in shape:
                matrix[row][col] = "-"
            for row, col in shape:
                matrix[row + 1][col] = "F"
        else:
            break

    return matrix


# Example input with obstacles
input_matrix = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "F", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "F", "F", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "F", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "F", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "#", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]

# Run simulation
print("Input:")
print_matrix(input_matrix)
output = simulate_fall(input_matrix)
print("Output:")
print_matrix(output)
