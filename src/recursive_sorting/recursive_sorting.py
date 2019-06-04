def merge(arrA, arrB):
    merged_arr = []
    while True:
        if arrA == [] or arrB == []:
            merged_arr.extend(arrA)
            merged_arr.extend(arrB)
            return merged_arr
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        l = len(arr)
        n = l // 2
        return merge(merge_sort(arr[0:n]), merge_sort(arr[n:]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
