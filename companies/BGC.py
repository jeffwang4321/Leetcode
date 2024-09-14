def convertMiletoMeters(mileInput, tunnelStart, tunnelEnd):
    # if mileInput > 4.75:
    #   return -1

    # if mileInput < 2.75:
    #   return -1

    # return (4.75 - mileInput) * 1600

    if tunnelEnd >= mileInput >= tunnelStart:
        return (tunnelEnd - mileInput) * 1600

    return -1


# python3 'BGC.py'
if __name__ == "__main__":
    # Test Cases
    # t2 = convertMiletoMeters(2.75)
    # t3 = convertMiletoMeters(3.75)
    # t4 = convertMiletoMeters(3)

    t0 = convertMiletoMeters(5, 2.75, 4.75)  # Out of upper bounds
    t1 = convertMiletoMeters(4.75, 2.75, 4.75)  # Start -  0m
    t2 = convertMiletoMeters(3.75, 2.75, 4.75)  # Half way - 1600m
    t3 = convertMiletoMeters(2.75, 2.75, 4.75)  # End  - 3200m
    t4 = convertMiletoMeters(2, 2.75, 4.75)  # Out of lowerbounds

    # Output
    print(t0)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
