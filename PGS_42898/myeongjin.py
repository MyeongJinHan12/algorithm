def solution(m, n, puddles):
    cases = [[0] * m for _ in range(n)] # m 열 / n 행
    cases[0][0] = 1

    for x, y in puddles: # 열 행
        cases[y-1][x-1] = -1

    for i in range(n):
        for j in range(m):

            if cases[i][j] != -1:
                if i > 0 and cases[i-1][j] != -1:
                    cases[i][j] += cases[i - 1][j]
                if j > 0 and cases[i][j-1] != -1:
                    cases[i][j] += cases[i][j - 1]

    answer = cases[n - 1][m - 1] % 1000000007

    return answer


solution(4, 3, [[2, 2]])