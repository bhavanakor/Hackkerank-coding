class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)
        i, j = 0, 0  # Pointers for array 'a' and 'b'
        count = 0    # Tracks the current element index in the combined array

        while i < n and j < m:
            # Pick the smaller element
            if a[i] < b[j]:
                current = a[i]
                i += 1
            else:
                current = b[j]
                j += 1

            count += 1
            if count == k:
                return current

        # If array 'b' is exhausted, pick from 'a'
        while i < n:
            current = a[i]
            i += 1
            count += 1
            if count == k:
                return current

        # If array 'a' is exhausted, pick from 'b'
        while j < m:
            current = b[j]
            j += 1
            count += 1
            if count == k:
                return current
