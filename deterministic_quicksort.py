
def deterministic_quicksort(arr):

    # Base case
    if len(arr) <= 1:
        return arr.copy()

    # Choose the first element as pivot
    pivot = arr[0]

    # Divide elements into three groups
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort and combine
    return (
        deterministic_quicksort(left)
        + middle
        + deterministic_quicksort(right)
    )


if __name__ == "__main__":

    print("Deterministic Quicksort Results")

    test_cases = {
        "Random Array": [8, 3, 1, 7, 5, 2],
        "Sorted Array": [1, 2, 3, 4, 5],
        "Reverse Sorted": [5, 4, 3, 2, 1],
        "Repeated Elements": [4, 2, 4, 1, 2, 4],
        "Empty Array": [],
        "Single Element": [10]
    }

    for name, arr in test_cases.items():

        result = deterministic_quicksort(arr)

        print(f"\n{name}")
        print("Original:", arr)
        print("Sorted:", result)

        assert result == sorted(arr)

    print("\nAll tests passed!")
