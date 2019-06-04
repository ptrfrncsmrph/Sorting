from functools import reduce


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


def bubble_sort(arr):
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps = True
    return arr


def count_sort(arr):
    if arr == []:
        return arr
    offset = min(0, *arr)
    counts = [0] * (max(arr) - offset + 1)
    for elem in arr:
        counts[elem - offset] += 1
    acc = 0
    for i in range(0, len(counts)):
        for j in range(acc, acc + counts[i]):
            arr[j] = i + offset
        acc += counts[i]
    return arr
