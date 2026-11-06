# Assignment 3: Understanding Algorithm Efficiency and Scalability

## Overview

This project explores the implementation and performance of Randomized Quicksort and Hashing with Chaining using Python. The goal is to understand algorithm efficiency, time complexity, and scalability through theoretical analysis and practical experiments.

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub

## Project Files

- `randomized_quicksort.py` – Randomized Quicksort implementation
- `deterministic_quicksort.py` – Deterministic Quicksort implementation
- `performance_comparison.py` – Sorting performance comparison
- `hash_table.py` – Hash table using chaining
- `performance_results.csv` – Experimental results
- `Assignment_3_Report.docx` – APA-style assignment report

## Part 1: Quicksort Analysis

Randomized Quicksort selects a pivot randomly, while Deterministic Quicksort selects the first element.

Both algorithms were tested using random, sorted, reverse-sorted, and repeated-element arrays of sizes 100, 500, 1000, and 2000.

### Key Findings

- Randomized Quicksort has an expected time complexity of O(n log n).
- Deterministic Quicksort can take O(n²) time on sorted inputs.
- Randomized Quicksort generally performed better on sorted and reverse-sorted arrays.
- Both algorithms handled repeated elements efficiently.

## Part 2: Hashing with Chaining

A hash table was implemented using chaining to handle collisions. It supports:

- Insert, search, and delete operations
- Updating existing values
- Load factor calculation
- Dynamic resizing

The table automatically resized from 7 to 15 buckets when its load factor exceeded 0.75.

Expected search and delete complexity is O(1 + α), where α is the load factor.

## How to Run

Open the project folder in VS Code and run:

```bash
python randomized_quicksort.py
python deterministic_quicksort.py
python performance_comparison.py
python hash_table.py
```

The performance comparison generates `performance_results.csv`.

No additional Python packages are required.
