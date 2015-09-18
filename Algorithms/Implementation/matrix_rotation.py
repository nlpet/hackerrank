"""
Matrix RotatioN: https://www.hackerrank.com/challenges/matrix-rotation-algo
 
"""

def unroll_matrix(matrix, M, N):
    rings = M // 2
    unrolled = [[] for _ in range(rings)]
    for ring in range(rings):
        top, left_strip, right_strip, bottom = [], [], [], []
        for y in range(ring, M - ring):
            for x in range(ring, N - ring):
                if y == ring:
                    top = matrix[y][ring: N - ring]
                    break
                elif y == (M - ring - 1):
                    bottom = matrix[y][ring: N - ring]
                    break
                else:
                    left_strip.append(matrix[y][x])
                    right_strip.append(matrix[y][N - ring - 1])
                    break
        unrolled[ring] = top + right_strip + bottom[::-1] + left_strip[::-1]
    return unrolled
                

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

    cycle = N * M - 4
    rotations = R % cycle

    unrolled = unroll_matrix(matrix, M, N)
