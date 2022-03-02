def insert_shift_array(arr, new_item):
    length = 0

    if type(arr) != list:
        return ('The first argument must be an array!!')

    if type(new_item) == list:
        return ('You cant add more than one item atime!!')

    for element in arr:
        length += 1
    
    if length % 2 == 0:
        mid = int(length/2)
    else:
        mid = int(length//2) + 1

    arr = arr[:mid] + [new_item] + arr[mid:]

    return arr



print(insert_shift_array(1,'a'))