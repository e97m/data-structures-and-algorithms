
def bubble_sort(arr):
    '''
    Sort an array of integers using bubble sort
    Input: arr - array of integers
    Output: arr - sorted array of integers
    '''
    if len(arr) <= 0:
        raise ValueError('Array is empty')
    for element in arr:
        if not isinstance(element, int):
            raise ValueError('Array contains non-integer elements')
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    print(bubble_sort([1, 3, 2, 5, 4]))