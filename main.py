def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a big gap, then reduce the gap

    # Start with the largest gap and reduce the gap until it becomes 0
    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        
        gap //= 2  # Reduce the gap

    return arr

# Example usage
if __name__ == "__main__":
    data = [12, 34, 54, 2, 3]
    print("Original array:", data)
    sorted_array = shell_sort(data)
    print("Sorted array:", sorted_array)
