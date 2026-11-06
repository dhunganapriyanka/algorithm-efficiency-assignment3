
import random


class HashTable:

    def __init__(self, capacity=7):
        # Initialize the hash table
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.count = 0

        # Universal hashing parameters
        self.prime = 1000003
        self.a = random.randint(1, self.prime - 1)
        self.b = random.randint(0, self.prime - 1)

    # Hash function
    def hash_function(self, key):
        return ((self.a * key + self.b) % self.prime) % self.capacity

    # Insert a key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        # Update value if the key already exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # Insert new key-value pair
        bucket.append([key, value])
        self.count += 1

        # Resize when load factor exceeds 0.75
        if self.load_factor() > 0.75:
            self.resize()

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    # Delete a key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.count -= 1
                return True

        return False

    # Calculate load factor
    def load_factor(self):
        return self.count / self.capacity

    # Resize the hash table
    def resize(self):
        old_table = self.table

        self.capacity = self.capacity * 2 + 1
        self.table = [[] for _ in range(self.capacity)]
        self.count = 0

        # Reinsert existing elements
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    # Display the hash table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Main program
if __name__ == "__main__":

    ht = HashTable()

    print("HASH TABLE WITH CHAINING")
    print("------------------------")

    # Test 1: Insert
    print("\n1. Inserting elements...")

    ht.insert(101, "Apple")
    ht.insert(102, "Banana")
    ht.insert(103, "Mango")
    ht.insert(104, "Orange")

    ht.display()

    # Test 2: Search
    print("\n2. Searching for key 102:")
    print("Result:", ht.search(102))

    # Test 3: Delete
    print("\n3. Deleting key 103:")
    print("Deleted:", ht.delete(103))

    # Test 4: Search after deletion
    print("\n4. Searching for deleted key 103:")
    print("Result:", ht.search(103))

    # Test 5: Update existing key
    print("\n5. Updating key 101:")

    ht.insert(101, "Green Apple")

    print("Updated value:", ht.search(101))

    # Test 6: Load factor
    print("\n6. Current load factor:")
    print(round(ht.load_factor(), 2))

    # Test 7: Dynamic resizing
    print("\n7. Testing dynamic resizing...")

    print("Capacity before:", ht.capacity)

    ht.insert(105, "Grape")
    ht.insert(106, "Peach")
    ht.insert(107, "Pineapple")

    print("Capacity after:", ht.capacity)
    print("Load factor:", round(ht.load_factor(), 2))

    # Display final table
    print("\nFinal Hash Table:")
    ht.display()

    # Test 8: Verify operations
    assert ht.search(101) == "Green Apple"
    assert ht.search(102) == "Banana"
    assert ht.search(103) is None
    assert ht.search(104) == "Orange"
    assert ht.search(105) == "Grape"
    assert ht.search(106) == "Peach"
    assert ht.search(107) == "Pineapple"

    assert ht.count == 6
    assert ht.capacity == 15

    print("\nAll hash table tests passed!")
