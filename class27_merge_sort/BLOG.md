# Merge Sort

Merge sort is a simple array sorting algorithm. It works by dividing the array into two parts and sorting them recursively. The array is divided into two parts until it is of size 1. Then the two parts are merged. The merge step is done by comparing the first element of each part and inserting the smaller element into the sorted array. The merge step is repeated until the array is sorted.

## Pseudocode:

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace:

Sample Array:  

    [8, 4, 23, 42, 16, 15]

### step 1:

Split the array into two halves.

    arr [8, 4, 23, 42, 16, 15]
    left [8, 4, 23]
    right [42, 16, 15]

### step 2:

Split the left into two halves.

    arr [8, 4, 23]
    left [8]
    right [4, 23]

### step 3:

The resultunt left is one element, so, split the right into two halves.

    arr [4, 23]
    left [4]
    right [23]

### step 4:

Now, all elements in the originila left are single elements. Merge the last two halves by copying elements decindly.

    merged [4, 23]

### step 5:

Merge in a sorted order the recently merged with the singl element in their level.

    merged [4, 8, 23]


### step 6:

Now, the original left is sorted and merged. Split the original right into two halves.

    arr [42, 16, 15]
    left [42]
    right [16, 15]

### step 7:

The resultunt left is one element, so, split the right into two halves.

    arr [16, 15]
    left [16]
    right [15]

### step 8:

Now, all elements in the originila righ are single elements. Merge the last two halves by copying elements decindly.

    merged [15, 16]

### step 9:

Merge in a sorted order the recently merged with the singl element in their level.

    merged [15, 16, 42]

### step 10:

Now, both original right and original righ are sorted and merged. Merge in a sorted order the original left and original right.

    merged [4, 8, 15, 16, 23, 42]

</br>

### Result

    [4, 8, 15, 16, 23, 42]

## Efficency:

Time Complexity: O(n * log n): It has recursion.

Space Complexity: O(n): copying process needs space