def max_length_subarray(arr):
    max_length = 0
    cur_length = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            cur_length += 1
        else:
            max_length = max(max_length, cur_length)
            cur_length = 1
    return max(max_length, cur_length)

arr = [1,2,3,4]
print("Max length subarray:", max_length_subarray(arr)
