def positive_sum(arr):
    s = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            s = s + arr[i]
    return s
