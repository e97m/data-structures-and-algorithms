# Insertion Sort

Insertion sort is a simple array sorting algorithm. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part. The function will compare two elements, if the first element is bigger than the second element, then the function will swap them. in the end the first element will be the smallest element in the array. The process is repeated until the unsorted part is empty.

## Pseudocode:

```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace:

Sample Array:  

    [8, 4, 23, 42, 16, 15]

### step 1:

During this step, the function will compare the fisrt two elements. In this case, the first element is begger than the second element. So the function will swap them.

The nested loop wont be entered because j is smaller than 0.

    [4, 8, 23, 42, 16, 15]

### step 2:

During this step, the function will compare the secound element with the third one. In this case, the secound element is not begger than the third element. So the function will not swap them.

    [4, 8, 23, 42, 16, 15]

### step 3:

During this step, the function will compare the third element with the fourth one. In this case, the third element is not begger than the fourth element. So the function will not swap them.

    [4, 8, 23, 42, 16, 15]

### step 4:

During this step, the function will compare the fourth element with the fifth one. In this case, the fourth element is begger than the fifth element. So the function will swap them.

    [4, 8, 23, 16, 42, 15]

Then it will enter to the nested loop to be sure that the swaped element is smaller than the previous elements. In thes case, the fourth element is smaller than the third element. So the function will swap them.

    [4, 8, 16, 23, 42, 15]

The third element is not smaller than the secound element. So the function will not swap them.

    [4, 8, 16, 23, 42, 15]

### step 5:

During this step, the function will compare the fourth element with the sixth one. In this case, the fifth element is begger than the sixth element. So the function will swap them.

    [4, 8, 16, 23, 15, 42]

Then it will enter to the nested loop to be sure that the swaped element is smaller than the previous elements. In thes case, the fifth element is smaller than the fourth element. So the function will swap them.

    [4, 8, 16, 15, 23, 42]

The fourth element is smaller than the third element. So the function will swap them.

    [4, 8, 15, 16, 23, 42]

The third element is not smaller than the secound element. So the function will not swap them.

### Result

    [4, 8, 15, 16, 23, 42]

## Efficency:

Time Complexity: O(n^2): It has a nested loop.
Space Complexity: O(1): No additional space is being created. This array is being sorted in place.