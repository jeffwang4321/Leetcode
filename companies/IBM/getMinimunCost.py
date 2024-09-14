from typing import List


def getMinimumCost(pixelIntensity: List[List[int]]) -> int:
    """
    Calculates the minimum total increase required to ensure that
    each COLUMNS's pixel intensities are non-decreasing from top to bottom.

    Args:
        pixelIntensity (List[List[int]]): 2D list of pixel intensity values.

    Returns:
        int: The total increase needed to make all columns non-decreasing.
    """

    ROWS = len(pixelIntensity)
    COLS = len(pixelIntensity[0])

    total_difference = 0
    for col in range(COLS):
        for row in range(1, ROWS):
            if pixelIntensity[row][col] <= pixelIntensity[row - 1][col]:
                difference = pixelIntensity[row - 1][col] - pixelIntensity[row][col] + 1
                total_difference += difference
                pixelIntensity[row][col] += difference

    return total_difference


if __name__ == "__main__":
    pixelIntensity = [[2, 5], [7, 4], [3, 5]]  # -> [[2, 5], [7, 6], [8, 7]]
    print(getMinimumCost(pixelIntensity))  # 5 + 2 + 2 = 9

    pixelIntensity = [[5, 3, 4], [2, 6, 1], [1, 5, 2]]  # -> [[5, 3, 4], [6, 6, 5], [7, 7, 6]]
    print(getMinimumCost(pixelIntensity))  # 4 + 6 + 2 + 4 + 4 = 20

    pixelIntensity = [[5, 3], [5, 6]]  # -> [[5, 3]], [6, 6]]
    print(getMinimumCost(pixelIntensity))  # 1
