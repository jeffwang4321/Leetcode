"""
We'd like for you to write a function that outputs a 10 by 10 multiplication table with the following requirements:

The table should print out
The table should include headers, with an X in the top left corner  
The table outputs in a square shape

Consider creating a code that you will be comfortable to put in production, even if you do it with pseudo code.

Desired Output:

 X   1   2   3   4   5   6   7   8   9  10
 1   1   2   3   4   5   6   7   8   9  10
 2   2   4   6   8  10  12  14  16  18  20
 3   3   6   9  12  15  18  21  24  27  30
 4   4   8  12  16  20  24  28  32  36  40
 5   5  10  15  20  25  30  35  40  45  50
 6   6  12  18  24  30  36  42  48  54  60
 7   7  14  21  28  35  42  49  56  63  70
 8   8  16  24  32  40  48  56  64  72  80
 9   9  18  27  36  45  54  63  72  81  90
10  10  20  30  40  50  60  70  80  90 100 

"""


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
