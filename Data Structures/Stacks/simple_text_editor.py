

def reverse_op(op):
    if op[0] == '1':
        s = op[1]
        if stack[-1] == s:
            stack.pop()
        else:
            while not stack[-1].endswith(s):
                el = stack.pop()
                s = s[:-len(el)]
            stack[-1] = stack[-1].replace(s, '')
    elif op[0] == '2':
        stack.append(op[1])


def perform_op(op):
    if op[0] == '1':
        stack.append(op[1])
        ops_stack.append(op)
    elif op[0] == '2':
        d = int(op[1])
        del_s = ''

        while d > 0:
            if len(stack[-1]) == d:
                del_s = stack.pop() + del_s
                d = 0
            elif len(stack[-1]) > d:
                del_s = stack[-1][-d:] + del_s
                stack[-1] = stack[-1][:-d]
                d = 0
            else:
                el = stack.pop()
                del_s = el + del_s
                d -= len(el)
        ops_stack.append(('2', del_s))
    elif op[0] == '3':
        print(''.join(stack)[int(op[1]) - 1])
    else:
        rev_op = ops_stack.pop()
        reverse_op(rev_op)


if __name__ == '__main__':
    stack = []
    ops_stack = []

    # TO BE FIXED

    with open('input04.txt', 'r') as r:
        N = int(r.readline().strip())

        for i in range(N):
            op = tuple(s for s in r.readline().strip().split(' '))
            perform_op(op)
