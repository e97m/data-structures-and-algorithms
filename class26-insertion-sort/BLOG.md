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

During this step, the function will compare the fisrt two elements. In this case, the first element (8) is begger than the second element (4). So the function will swap them.

The nested loop wont be entered because j is smaller than 0.

    [4, 8, 23, 42, 16, 15]

### step 2:

During this step, the function will compare the secound element (8) with the third one (23). In this case, the secound element (8) is not begger than the third element (23). So the function will not swap them.

    [4, 8, 23, 42, 16, 15]

### step 3:

During this step, the function will compare the third element (23) with the fourth one (42). In this case, the third element (23) is not begger than the fourth element (42). So the function will not swap them.

    [4, 8, 23, 42, 16, 15]

### step 4:

During this step, the function will compare the fourth element (42) with the fifth one (16). In this case, the fourth element (42) is begger than the fifth element (16). So the function will swap them.

    [4, 8, 23, 16, 42, 15]

Then it will enter to the nested loop to be sure that the swaped element is smaller than the previous elements. In thes case, the fourth element (16) is smaller than the third element (23). So the function will swap them.

    [4, 8, 16, 23, 42, 15]

The third element (16) is not smaller than the secound element (8). So the function will not swap them.

    [4, 8, 16, 23, 42, 15]

### step 5:

During this step, the function will compare the fifth element (42) with the sixth one (15). In this case, the fifth element (42) is begger than the sixth element (15). So the function will swap them.

    [4, 8, 16, 23, 15, 42]

Then it will enter to the nested loop to be sure that the swaped element is smaller than the previous elements. In thes case, the fifth element (15) is smaller than the fourth element (23). So the function will swap them.

    [4, 8, 16, 15, 23, 42]

The fourth element (15) is smaller than the third element (16). So the function will swap them.

    [4, 8, 15, 16, 23, 42]

The third element (15) is not smaller than the secound element (8). So the function will not swap them.

    [4, 8, 15, 16, 23, 42]

</br>

### Result

    [4, 8, 15, 16, 23, 42]

## Efficency:

Time Complexity: O(n^2): It has a nested loop.

Space Complexity: O(1): No additional space is being created. This array is being sorted in place.