    marks.sort()
    num = len(marks)  # Number of students
    if num % 2 == 1:
        median = marks[num // 2]     # If the number of students is odd
    else:
        middle1 = marks[(num - 1) // 2]
        middle2 = marks[num // 2]
        median = (middle1 + middle2)/2 # If the number of students is even
    return median