class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.my_arr = [None] * capacity
        self.capacity = capacity

        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.my_arr)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # hashed_string = self.djb2(key)
        idx = self.hash_index(key)

        new_hashTableEntry = HashTableEntry(key, value)
        existing_entry = self.my_arr[idx]

        if existing_entry:            
            while existing_entry:
                if existing_entry.key == key:
                    # updating value for this repeat key
                    existing_entry.value = value
                    return
                if existing_entry.next == None:
                    existing_entry.next = new_hashTableEntry
                    self.load = self.load + 1
                    if self.get_load_factor() > 0.7:
                        self.resize(self.capacity * 2)
                    return
                existing_entry = existing_entry.next
        else:
            self.my_arr[idx] = new_hashTableEntry
            self.load = self.load + 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # hashed_string = self.djb2(key)
        # idx = hashed_string % self.capacity
        idx = self.hash_index(key)

        existing_entry = self.my_arr[idx]

        if self.load == 0:
            print("there are no items in hash table")
            return

        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    self.load = self.load - 1
                    if last_entry:
                        last_entry.next = existing_entry.next
                        return
                    else:
                        self.my_arr[idx] = existing_entry.next
                        return
                last_entry = existing_entry
                existing_entry = existing_entry.next
        print("Key was not found") 



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # hashed_string = self.djb2(key)
        # idx = hashed_string % self.capacity
        idx = self.hash_index(key)

        existing_entry = self.my_arr[idx]

        if existing_entry:
            while existing_entry:
                if existing_entry.key == key:
                    return existing_entry.value
                existing_entry = existing_entry.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_arr = [None] * (new_capacity)
        self.capacity = new_capacity

        old_arr = self.my_arr

        self.my_arr = new_arr

        for index in range(len(old_arr)):
            entry = old_arr[index]
            if entry:
                while entry:
                    self.put(entry.key, entry.value)
                    entry = entry.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
