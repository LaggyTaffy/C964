# This file contains the implementation of the ChainingHashTable class as well as an insert, lookup and remove function

# Citation: C950 - Data Structures and Algorithms II Webinar-1, https://srm--c.vf.force.com/servlet/fileField?retURL=https%3A%2F%2Fsrm--c.vf.force.com%2Fapex%2Fcoursearticle%3FId%3DkA03x000000e1fpCAA&entityId=ka03x000000u1VWAAY&_CONFIRMATIONTOKEN=VmpFPSxNakF5TkMwd055MHhORlF4T0Rvek5Eb3lNUzQxTlRWYSxmSFBiSUF4eUZNMWk5TDQ0bjlmaUpQTHkxcUpZbDN3VDRhTnA4T1p5clI0PSxaREZrWVdOaQ%3D%3D&common.udd.actions.ActionsUtilORIG_URI=%2Fservlet%2FfileField&field=FileUpload__Body__s
# The ChainingHashTable class is a hash table that uses chaining to resolve collisions.
# Best case time complexity: O(1)
# Worst case time complexity: O(n)
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initialcapacity=10):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initialcapacity):
            self.table.append([])

    # Best case time complexity: O(1)
    # Worst case time complexity: O(n)
    # Inserts a new item into the hash table.
    def insert(self, key, packages):
        # Use the package ID as the key for hashing
        bucket = hash(key) % len(self.table)
        bucketlist = self.table[bucket]

        # Updates package if it exist
        for kv in bucketlist:
            if kv[0] == key:
                kv[1] = packages
                return True

        # If the package ID does not exist, add the new package
        bucketlist.append([key, packages])
        return True

    # Best case time complexity: O(1)
    # Worst case time complexity: O(n)
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def lookup(self, key):
        # Get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Best case time complexity: O(1)
    # Worst case time complexity: O(n)
    # Removes an item with matching key from the hash table.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucketlist = self.table[bucket]

        # If the key is found in the hash table, remove the item
        if key in bucketlist:
            bucketlist.remove(key)