import time
import random
import pandas as pd
from datetime import datetime
import json


class Sort:
    def heapify(self, arr, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < N and arr[largest] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < N and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, N, largest)

    def heap(self, arr):
        # This code is contributed by Mohit Kumra

        N = len(arr)

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            self.heapify(arr, N, i)

        # One by one extract elements
        for i in range(N - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

    def bubble(self, arr):
        # This code is modified by Suraj krushna Yadav
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):
            swapped = False

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

    def insertion(self, arr):
        # This code is contributed by Mohit Kumra
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(self, arr):
        # This code is contributed by Mayank Khanna

        if len(arr) > 1:
            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the array elements
            L = arr[:mid]

            # Into 2 halves
            R = arr[mid:]

            # Sorting the first half
            self.merge(L)

            # Sorting the second half
            self.merge(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


class Utils:
    def count_time(self, title, function, items):
        print(title)

        start_time = time.perf_counter()

        function(items.copy())

        end_time = time.perf_counter()

        result = end_time - start_time

        print(f' = = = = = Finished in {result} segundos"')

        return result

    def generate_numbers(self, count):
        items = []

        for i in range(0, count):
            items.append(i)

        random.shuffle(items)

        return items


sort = Sort()
util = Utils()

random_number_10k = util.generate_numbers(10000)
random_number_50k = util.generate_numbers(50000)
random_number_100k = util.generate_numbers(100000)

random_10k_bubble = util.count_time('Running "random - number - 10k - bubble"', sort.bubble, random_number_10k)
random_10k_heap = util.count_time('Running "random - number - 10k - heap"', sort.heap, random_number_10k)
random_10k_insertion = util.count_time('Running "random - number - 10k - insertion"', sort.insertion, random_number_10k)
random_10k_merge = util.count_time('Running "random - number - 10k - merge"', sort.merge, random_number_10k)

random_50k_bubble = util.count_time('Running "random - number - 50k - bubble"', sort.bubble, random_number_50k)
random_50k_heap = util.count_time('Running "random - number - 50k - heap"', sort.heap, random_number_50k)
random_50k_insertion = util.count_time('Running "random - number - 50k - insertion"', sort.insertion, random_number_50k)
random_50k_merge = util.count_time('Running "random - number - 50k - merge"', sort.merge, random_number_50k)

random_100k_bubble = util.count_time('Running "random - number - 100k - bubble"', sort.bubble, random_number_100k)
random_100k_heap = util.count_time('Running "random - number - 100k - heap"', sort.heap, random_number_100k)
random_100k_insertion = util.count_time('Running "random - number - 100k - insertion"', sort.insertion, random_number_100k)
random_100k_merge = util.count_time('Running "random - number - 100k - merge"', sort.merge, random_number_100k)

items = [
    # Random
    {"type": 'number', "order": 'random', "quantity": '10k', "bubble": random_10k_bubble,
     "heap": random_10k_heap, "insertion": random_10k_insertion, "merge": random_10k_merge},
    {"type": 'number', "order": 'random', "quantity": '50k', "bubble": random_50k_bubble,
     "heap": random_50k_heap, "insertion": random_50k_insertion, "merge": random_50k_merge},
    {"type": 'number', "order": 'random', "quantity": '100k', "bubble": random_100k_bubble,
     "heap": random_100k_heap, "insertion": random_100k_insertion, "merge": random_100k_merge},
    # Descending
    # {"type": 'number', "order": 'descending', "quantity": '10k', "bubble": descending_10k_bubble.result, "heap": descending_10k_heap.result, "insertion": descending_10k_insertion.result, "merge": descending_10k_merge.result},
    # {"type": 'number', "order": 'descending', "quantity": '50k', "bubble": descending_50k_bubble.result, "heap": descending_50k_heap.result, "insertion": descending_50k_insertion.result, "merge": descending_50k_merge.result},
    # {"type": 'number', "order": 'descending', "quantity": '100k', "bubble": descending_100k_bubble.result, "heap": descending_100k_heap.result, "insertion": descending_100k_insertion.result, "merge": descending_100k_merge.result},
    # Descending
    # {"type": 'number', "order": 'ascending', "quantity": '10k', "bubble": ascending_10k_bubble.result, "heap": ascending_10k_heap.result, "insertion": ascending_10k_insertion.result, "merge": ascending_10k_merge.result},
    # {"type": 'number', "order": 'ascending', "quantity": '50k', "bubble": ascending_50k_bubble.result, "heap": ascending_50k_heap.result, "insertion": ascending_50k_insertion.result, "merge": ascending_50k_merge.result},
    # {"type": 'number', "order": 'ascending', "quantity": '100k', "bubble": ascending_100k_bubble.result, "heap": ascending_100k_heap.result, "insertion": ascending_100k_insertion.result, "merge": ascending_100k_merge.result},
]

now = datetime.now()
iso = now.isoformat()

to_write = {"data": items}

with open(f"data/{iso.replace(':', '-')}.json", 'w') as file:
    json.dump(to_write, file)

table = pd.DataFrame(items)
print(table)
