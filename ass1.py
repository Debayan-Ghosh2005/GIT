def does_something(matrix):
    r = len(matrix)
    if r == 0 or r != len(matrix[0]):
        return False
    expected = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != expected:
            return False
    for j in range(r):
        if sum(matrix[i][j] for i in range(r)) != expected:
            return False
    if sum(matrix[i][r -1 - i] for i in range(r)) != expected:
        return False
    
    return True