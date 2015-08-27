n = int(input())
s = set(map(int, input().split()))
N = int(input())
commands = [input() for _ in range(N)]

key_command_dict = {
    'remove': s.remove,
    'discard': s.discard
}

for command in commands:
    command = command.split(' ')
    try:
        if len(command) == 1:
            s.pop()
        else:
            key_command_dict[command[0]](int(command[1]))
    except KeyError:
        pass

print(sum(s))
