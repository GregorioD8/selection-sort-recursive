def recursive_selection_sort(arr, start=0):
     # Base case: if start index reaches the end of the array, it's sorted
    if start >= len(arr) - 1:
        return arr
    
    # Step 1: Find the minimum element in the unsorted portion
    min_index = start
    for j in range(start + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    
    # Step 2: Swap the minimum element with the current start element
    arr[start], arr[min_index] = arr[min_index], arr[start]
    
    # Step 3: Recur for the next index
    return recursive_selection_sort(arr, start + 1)

# Testing
print(recursive_selection_sort([3, -1, 5, 2]))  # Expected output: [-1, 2, 3, 5]
print(recursive_selection_sort([64, 25, 12, 22, 11]))  # Expected output: [11, 12, 22, 25, 64]
print(recursive_selection_sort([1, 2, 3, 4]))  # Expected output: [1, 2, 3, 4]
print(recursive_selection_sort([-3, -5, -2, -8]))  # Expected output: [-8, -5, -3, -2]