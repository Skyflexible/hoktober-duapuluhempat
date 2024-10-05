import time
import random

def generate_random_array(size, lower_bound=0, upper_bound=1000):
    """Generate a random array of given size."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def log_message(message):
    """Log messages for debugging and tracking."""
    print(f"[LOG] {message}")

def insertion_sort(arr):
    """
    Perform Insertion Sort on the array.
    
    Parameters:
    arr (list): The list to be sorted.
    """
    n = len(arr)
    log_message(f"Starting Insertion Sort on array of size {n}")

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        log_message(f"Inserted {key} at position {j + 1}, array state: {arr}")
    
    log_message("Insertion Sort completed")
    return arr

def measure_sort_time(sort_function, arr):
    """Measure the time taken to sort the array."""
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def is_sorted(arr):
    """Check if the array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def test_insertion_sort():
    """Test the Insertion Sort implementation."""
    sizes = [10, 100, 1000, 5000, 10000]
    for size in sizes:
        arr = generate_random_array(size)
        log_message(f"Testing Insertion Sort on array of size {size}...")
        duration = measure_sort_time(insertion_sort, arr.copy())
        
        if is_sorted(arr):
            log_message(f"Array sorted successfully in {duration:.6f} seconds.")
        else:
            log_message("Sorting failed!")

def main():
    """Main function to execute the Insertion Sort tests."""
    log_message("Starting Insertion Sort Tests...")
    test_insertion_sort()
    log_message("All tests completed.")

if __name__ == "__main__":
    main()
