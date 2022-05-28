# Quick Sort

Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quick sort. Most of the implementations use the last element as pivot. The pivot can also be chosen as the first element, the middle element or any other. The partition process keeps the pivot at its correct position in the sorted array and places all smaller elements to its left and all greater elements to its right.

## Pseudocode:

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Trace:

Sample Array:  

    arr = [8, 4, 23, 42, 16, 15]


### step 1:

Choose the last value (15) as pivot, split the array into two parts one grater than the pivot and one less than the pivot.

    less than pivot: 8, 4
    grater than pivot: 23, 42, 16

### step 2:

Dealing with the less part:

    arr = 8, 4

Choose the last value (4) as pivot, split the array into two parts one grater than the pivot and one less than the pivot.

    less than pivot: None
    grater than pivot: 8
    

### step 3:

Dealing with the grater part:

    arr = [23,42,16]

Choose the last value (16) as pivot, split the array into two parts one grater than the pivot and one less than the pivot.

    less than pivot: None
    grater than pivot: 23, 42

### step 4:

Dealing with the grater part:

    arr = [23, 42]

Choose the last value (42) as pivot, split the array into two parts one grater than the pivot and one less than the pivot.

  less than pivot: 23


### Result

    arr = [4, 8, 15, 16, 23, 42]


## Efficency:

Time Complexity: O(n)

Space Complexity: O(1)