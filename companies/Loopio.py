def print_multiplication_table(size):
    """
    Prints a multiplication table of a given size with headers and text aligned right.

    Args:
        size (int): The size of the multiplication table (default is 10).
    """

    # Print the header row
    header = "   X"  # Start with a space for alignment
    for i in range(1, size + 1):
        header += f"{i:4}"  # Add each column header with proper spacing
    print(header)

    # Print each row of the multiplication table
    for i in range(1, size + 1):
        row = f"{i:4}"  # Starting with the row number
        for j in range(1, size + 1):
            row += f"{i * j:4}"  # Add the product to the row
        print(row)


if __name__ == "__main__":
    print_multiplication_table(20)
