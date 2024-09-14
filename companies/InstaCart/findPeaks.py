from typing import List


def find_peaks(target: List[int]) -> List[int]:
    """
    Returns a list of elements from the input list that are greater than their neighbors.
    Includes the first and last element by default.

    Args:
        target (List[int]): The input list of integers.

    Returns:
        List[int]: A list of elements that are greater than their neighbors.
    """

    # Edge case: If the list is empty or has 2 or less elements

    n = len(target)
    if n == 0:
        return []
    if n <= 2:
        return target

    # Initialize the result list with the first and last element
    result = [target[0]]

    # Iterate through the array, starting from the second element and ending at the second last element
    for i in range(1, n - 1):
        if target[i] > target[i - 1] and target[i] > target[i + 1]:
            result.append(target[i])

    result.append(target[-1])
    return result


# Example usage
print(find_peaks([1, 3, 2, 5, 7, 6, 8, 10, 9]))  # Output: [1, 3, 7, 10, 9]
print(find_peaks([1, 2, 3, 4, 5]))  # Output: [1, 5]
print(find_peaks([5, 1, 2, 3, 4]))  # Output: [5, 4]
print(find_peaks([1, 1]))  # Output: [1, 1]
print(find_peaks([0]))  # Output: [1, 1]
