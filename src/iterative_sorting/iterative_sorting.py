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


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
