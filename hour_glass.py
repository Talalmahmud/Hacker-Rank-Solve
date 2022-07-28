arr = []
r = 0
max_result = []
arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

for i in range(4):
    for j in range(4):
        a = arr[i][j]
        b = arr[i][j + 1]
        c = arr[i][j + 2]
        d = arr[i + 1][j + 1]
        e = arr[i + 2][j]
        f = arr[i + 2][j + 1]
        g = arr[i + 2][j + 2]
        r = a + b + c + d + e + f + g
        max_result.append(r)
print(max_result)
