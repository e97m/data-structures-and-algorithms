
# time O(n^2), space O(1)
def insertion_sort(arr):
    if len(arr) == 0: return 'Empty array!'
    for i in arr:
        if type(i) is not int:
            return 'Please enter an integer array!'

    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = temp
    return arr


# Example for another algorithm
def select_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr


if __name__ == "__main__":
    matrix = [
        [8,4,23,42,16,15],
        [20,18,12,8,5,-2],
        [5,12,7,5,5,7],
        [2,3,5,7,13,11],
        ]

    for i in matrix:
        print('select_sort:',select_sort(i))
        print('insertion_sort:',insertion_sort(i))
