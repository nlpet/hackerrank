n, d = [int(x) for x in input().strip().split(' ')]
arr = [int(x) for x in input().strip().split(' ')]

new_0_indx = n - d
new_arr = arr[n - new_0_indx:] + arr[:n - new_0_indx]
print(' '.join([str(n) for n in new_arr]))
