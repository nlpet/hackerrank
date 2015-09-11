"""
Matrix RotatioN: https://www.hackerrank.com/challenges/matrix-rotation-algo

[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

6 rotations:
 (0,0) => (3,3)

27 rotations:
 (0,0) => (3,0) (26 % 12 = 3 rotations, x + 3)
 
first cycle: x -> [0, M - 1]
second cycle: x = M - 1
third cycle: x -> [M - 1, 0]
fourth cycle: x = 0

first cycle: y -> 0
second cycle: y -> +1
third cycle: y -> +1
fourth cycle: y -> +1

x,y = (0, 0)

flag = 1

for i in range(rotations):
       
    if flag == first
        x ++
    elif flag == second
        y ++
    elif flag = third
        x --
    else
        y --
        
    if x == M - 1 and y == 0: flag 2
    elif x == M - 1 and y == N - 1: flag 3
    elif x == 0 and y == N - 1: flag 4
    else: flag 1
        
 
"""

# Num rows
M = 4

# Num columns
N = 4

# Rotations
R = 1


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

cycle = N * M - 4
rotations = R % wrap

index = (0,0)
reverse = {'row' : 1, 'col': 1}


