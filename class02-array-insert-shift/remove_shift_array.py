def remove_shift_array(arr):
    length = 0

    if type(arr) != list:
        return ('The argument must be an array!!')

    if arr==[]:
        return ('You cant delete from empty array!!')

    for element in arr:
        length += 1
    
    if length % 2 == 0:
        mid = int(length/2)
        arr = arr[:mid] + arr[mid+1:]
    else:
        mid = int(length//2) + 1
        arr = arr[:mid-1] + arr[mid:]

    return arr


print(remove_shift_array([]))