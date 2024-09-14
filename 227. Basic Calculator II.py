class Solution:
    def calculate(self, s: str) -> int:
        # base case
        if len(s) == 0:
            return 0

        # Initialize
        stack = []
        current_number = 0
        operation = "+"

        # Iterate through each character in the string
        for i, char in enumerate(s):
            # If the character is a digit, build the current number
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            # If the character is an operator or it's the last character in the string
            if char in "+-*/" or i == len(s) - 1:
                # Process the current number based on the last operation
                if operation == "+":
                    stack.append(current_number)
                elif operation == "-":
                    stack.append(-current_number)
                elif operation == "*":
                    stack.append(stack.pop() * current_number)
                elif operation == "/":
                    # Integer division truncating towards zero
                    top = stack.pop()
                    stack.append(int(top / current_number))
                    # if top < 0:
                    #     stack.append(-(-top // current_number))
                    # else:
                    #     stack.append(top // current_number)

                # Reset the current number and update the operation
                current_number = 0
                operation = char

        return sum(stack)


# python3 '.\297. Serialize and Deserialize Binary Tree.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.calculate("3+2*2")
    t2 = s.calculate(" 3/2 ")
    t3 = s.calculate(" 3+5 / 2 ")

    # Output
    print(t1)
    print(t2)
    print(t3)
