def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap = (arr, i, low)
    swap(arr, right, low + 1)
    return low + 1


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


if __name__ == "__main__":

    matrix = [
        [8, 4, 23, 42, 16, 15],
        [20, 18, 12, 8, 5, -2],
        [5, 12, 7, 5, 5, 7],
        [2, 3, 5, 7, 13, 11],
        ]

    for i in matrix:
        print(quick_sort(i, 0, len(i) - 1))
