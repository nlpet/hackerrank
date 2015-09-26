"""
Matrix RotatioN: https://www.hackerrank.com/challenges/matrix-rotation-algo
"""


def unroll_matrix(matrix, M, N, rings):
    unrolled = [[] for _ in range(rings)]
    for r in range(rings):
        top, left_strip, right_strip, bottom = [], [], [], []
        # Iterate over columns
        for y in range(r, M - r):
            # Iterate over rows
            for x in range(r, N - r):
                if y == r:
                    top = matrix[y][r: N - r]
                    break
                elif y == (M - r - 1):
                    bottom = matrix[y][r: N - r]
                    break
                else:
                    left_strip.append(matrix[y][x])
                    right_strip.append(matrix[y][N - r - 1])
                    break
        unrolled[r] = top + right_strip + bottom[::-1] + left_strip[::-1]
    return unrolled


def rotate(unrolled, rotations):
    for i in range(len(unrolled)):
        unrolled[i] = unrolled[i][rotations:] + unrolled[i][:rotations]


def roll_matrix(unrolled, M, N, rings):
    matrix = [[None] * N for _ in range(M)]
    for r in range(rings):
        if len(matrix[r]) == 4:
            top = matrix[r][:2]
            left_strip = []
            bottom = matrix[r][2:]
            right_strip = []
        else:
            top = matrix[r][: (N - r)]
            left_strip = matrix[r][(N - r): (N - r) + (M - r) - 2]
            bottom = matrix[r][(N - r) + (M - r) - 2: 2 * (N - r) + (M - r) - 2]
            right_strip = matrix[r][2 * (N - r) + (M - r) - 2:]
        # Iterate over columns
        for y in range(r, M - r):
            # Iterate over rows
            for x in range(r, N - r):
                pass



if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    # Num rows
    M = 4

    # Num columns
    N = 4

    # Rotations
    R = 1

    # Rings
    rings = M // 2

    cycle = N * M - 4
    rotations = R % cycle

    unrolled = unroll_matrix(matrix, M, N, rings)
