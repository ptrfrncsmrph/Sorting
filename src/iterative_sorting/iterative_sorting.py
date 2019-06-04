def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    swaps = 0
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swaps += 1
    if swaps == 0:
        return arr
    else:
        return bubble_sort(arr)


def count_sort(arr, maximum=-1):
    if arr == []:
        return arr
    counts = {}
    for i in range(min(arr), max(arr) + 1):
        counts[i] = 0
    for elem in arr:
        counts[elem] += 1
    acc = 0
    for key, value in counts.items():
        for i in range(acc, acc + value):
            arr[i] = key
        acc += value
    return arr
