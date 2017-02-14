n = int(input().strip())
stack = []
max_stack = []

for _ in range(n):
    q = [int(n) for n in input().strip().split(' ')]
    if q[0] == 1:
        stack.append(q[1])
        if not max_stack or max_stack[-1] <= q[1]:
            max_stack.append(q[1])
    elif q[0] == 2:
        el = stack.pop()
        if max_stack and el == max_stack[-1]:
            max_stack.pop()
    elif q[0] == 3:
        print(max_stack[-1])
