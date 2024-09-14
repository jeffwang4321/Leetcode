def largest_square(histogram):
    n = len(histogram)
    max_area = 0

    # Iterate over each possible left boundary of the square
    for left in range(n):
        min_height = histogram[left]

        # Iterate over each possible right boundary of the square
        for right in range(left, n):
            # Update the minimum height in the current segment
            min_height = min(min_height, histogram[right])

            # The width of the segment is (right - left + 1), 1 - 0 + 1 = 2 squares
            width = right - left + 1

            # The side length of the square is the minimum of height and width
            side_length = min(min_height, width)

            # Calculate the area of the square
            area = side_length * side_length

            # Update the maximum area found
            max_area = max(max_area, area)

    return max_area


# Example usage
histogram = [1, 2, 3, 2, 1]
print(largest_square(histogram))

histogram = [4, 3, 4]
print(largest_square(histogram))
