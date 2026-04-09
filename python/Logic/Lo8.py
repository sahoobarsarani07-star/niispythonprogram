for no in range(1, 1001):
    p = 0
    temp = no

    # Count number of digits
    while temp != 0:
        temp = temp // 10
        p = p + 1

    temp = no
    arm = 0

    # Calculate Armstrong sum
    while temp != 0:
        r = temp % 10
        arm = arm + (r ** p)
        temp = temp // 10

    # Check Armstrong condition
    if no == arm:
        print(no, "is Armstrong number")