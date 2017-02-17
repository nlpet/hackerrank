def array_left_rotation(arr, n, k):
    new_0_indx = n - k
    new_arr = arr[n - new_0_indx:] + arr[:n - new_0_indx]
    return new_arr

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
