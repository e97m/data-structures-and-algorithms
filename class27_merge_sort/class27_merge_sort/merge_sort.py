def merge_sort(arr):
    if type(arr) is not list: return 'Please enten an array!'
    if len(arr) <= 0: return 'Empty array!'
    for i in arr:
        if type(i) is not int: return 'Please enter an integer array!'

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # print('arr', arr)
        # print('left', left)
        # print('right', right)

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    # print('merged',arr)
    return arr



if __name__ == "__main__":

    matrix = [
        [8,4,23,42,16,15],
        [20,18,12,8,5,-2],
        [5,12,7,5,5,7],
        [2,3,5,7,13,11],
        ]
    
    for i in matrix:
        print(merge_sort(i))