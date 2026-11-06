
import random
import time
import csv
import sys

from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

# Allow larger recursive calls for the experiment
sys.setrecursionlimit(10000)

sizes = [100, 500, 1000, 2000]
trials = 5


def generate_data(size, data_type):
    if data_type == "Random":
        return random.sample(range(size * 10), size)

    elif data_type == "Sorted":
        return list(range(size))

    elif data_type == "Reverse Sorted":
        return list(range(size, 0, -1))

    elif data_type == "Repeated":
        return [random.randint(1, 10) for _ in range(size)]


def measure_time(algorithm, arr):
    start = time.perf_counter()
    result = algorithm(arr.copy())
    end = time.perf_counter()

    assert result == sorted(arr)

    return end - start


results = []

print("Quicksort Performance Comparison\n")

for size in sizes:
    for data_type in [
        "Random",
        "Sorted",
        "Reverse Sorted",
        "Repeated"
    ]:

        randomized_times = []
        deterministic_times = []

        for _ in range(trials):
            arr = generate_data(size, data_type)

            randomized_times.append(
                measure_time(randomized_quicksort, arr)
            )

            deterministic_times.append(
                measure_time(deterministic_quicksort, arr)
            )

        randomized_time = sum(randomized_times) / trials
        deterministic_time = sum(deterministic_times) / trials

        print(
            f"Size: {size}, Type: {data_type}, "
            f"Randomized: {randomized_time:.6f}s, "
            f"Deterministic: {deterministic_time:.6f}s"
        )

        results.append([
            size,
            data_type,
            round(randomized_time, 6),
            round(deterministic_time, 6)
        ])


with open(
    "performance_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Array Size",
        "Data Type",
        "Randomized Quicksort (s)",
        "Deterministic Quicksort (s)"
    ])

    writer.writerows(results)


print("\nPerformance results saved to performance_results.csv")
