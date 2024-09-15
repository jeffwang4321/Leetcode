from itertools import product

"""
Problem Restatement:
Given a number, determine if you can insert plus (+) or minus (-) signs between the digits to form 
an expression that evaluates to zero. If possible, return the sequence of signs, preferring the 
solution with the most minus (-) signs. If no such combination exists, return "not possible."
"""


def MathChallenge(num):
    """
    This function takes a integer num as input and returns a string representing the sequence of plus (+) and minus (-)
    signs that can be inserted between the digits of the number to form an expression that evaluates to zero.
    If no such combination exists, the function returns "not possible".
    """
    # Convert the number to a string to handle each digit individually
    digits = list(str(num))
    best_result = None
    most_minuses = -1

    # Generate all possible combinations of + and - for the digits
    # Without using product() we would have to write nested loops for each digit or use recursion/ backtracking
    for signs in product("+-", repeat=len(digits) - 1):
        # Build the expression
        expression = digits[0]
        for i in range(len(signs)):
            expression += signs[i] + digits[i + 1]

        # Evaluate the expression
        if eval(expression) == 0:
            # Count the number of minus signs
            minus_count = signs.count("-")

            # If this solution has more minus signs, take it as the best result
            if minus_count > most_minuses:
                most_minuses = minus_count
                best_result = "".join(signs)

    # Return the best result or 'not possible'
    return best_result if best_result else "not possible"


# Example usage:
print(MathChallenge(199))  # Output: "not possible"
print(MathChallenge(26712))  # Output: "-+--"
