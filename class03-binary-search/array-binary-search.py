
def binary_search(arr, item):

    if type(item) != int:
        return 'Please  enter an integer!'
    if type(arr) != list:
        return 'Please enter a list!'
    if arr == []:
        return 'Please enter an array have values!'

    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    
    return "This value is not exist in the arr"

print(binary_search([], 8))