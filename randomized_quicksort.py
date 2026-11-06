
import random


def randomized_quicksort(arr):
    # Stop if the array has zero or one element
    if len(arr) <= 1:
        return arr.copy()

    # Select a random pivot
    pivot = random.choice(arr)

    # Divide elements into three groups
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right groups
    return (
        randomized_quicksort(left)
        + middle
        + randomized_quicksort(right)
    )


# Test the algorithm
if __name__ == "__main__":

    print("Randomized Quicksort Results")

    test_cases = {
        "Random Array": [8, 3, 1, 7, 5, 2],
        "Sorted Array": [1, 2, 3, 4, 5],
        "Reverse Sorted": [5, 4, 3, 2, 1],
        "Repeated Elements": [4, 2, 4, 1, 2, 4],
        "Empty Array": [],
        "Single Element": [10]
    }

    for name, arr in test_cases.items():
        result = randomized_quicksort(arr)

        print(f"\n{name}")
        print("Original:", arr)
        print("Sorted:", result)

        assert result == sorted(arr)

    print("\nAll tests passed!")
