n = int(input())
A = []
B = []
for _ in range(n):
    row = list(map(int, input().split(',')))
    A.append(row)
for _ in range(n):
    row = list(map(int, input().split(',')))
    B.append(row)

    
for i in range(n):
    for j in range(n):
        sum_mat = 0
        for k in range(n):
            sum_mat = sum_mat + A[i][k] * B[k][j]
        if j == n-1:
            print(sum_mat, end = "")
        else:
            print(sum_mat, end = ",")
    if(i,j) != (n-1, n-1):
        print()