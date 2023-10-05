import pandas as pd

from src.random.number.with10k import merge as random_10k_merge, heap as random_10k_heap, insertion as random_10k_insertion, bubble as random_10k_bubble
from src.random.number.with50k import merge as random_50k_merge, heap as random_50k_heap, insertion as random_50k_insertion, bubble as random_50k_bubble
from src.random.number.with100k import merge as random_100k_merge, heap as random_100k_heap, insertion as random_100k_insertion, bubble as random_100k_bubble

from src.descending.number.with10k import merge as descending_10k_merge, heap as descending_10k_heap, insertion as descending_10k_insertion, bubble as descending_10k_bubble
from src.descending.number.with50k import merge as descending_50k_merge, heap as descending_50k_heap, insertion as descending_50k_insertion, bubble as descending_50k_bubble
from src.descending.number.with100k import merge as descending_100k_merge, heap as descending_100k_heap, insertion as descending_100k_insertion, bubble as descending_100k_bubble

from src.ascending.number.with10k import merge as ascending_10k_merge, heap as ascending_10k_heap, insertion as ascending_10k_insertion, bubble as ascending_10k_bubble
from src.ascending.number.with50k import merge as ascending_50k_merge, heap as ascending_50k_heap, insertion as ascending_50k_insertion, bubble as ascending_50k_bubble
from src.ascending.number.with100k import merge as ascending_100k_merge, heap as ascending_100k_heap, insertion as ascending_100k_insertion, bubble as ascending_100k_bubble

items = [
    # Random
    {"Type": 'random', "Quantity": '10k', "Bubble": random_10k_bubble.result, "Heap": random_10k_heap.result, "Insertion": random_10k_insertion.result, "Merge": random_10k_merge.result},
    {"Type": 'random', "Quantity": '50k', "Bubble": random_50k_bubble.result, "Heap": random_50k_heap.result, "Insertion": random_50k_insertion.result, "Merge": random_50k_merge.result},
    {"Type": 'random', "Quantity": '100k', "Bubble": random_100k_bubble.result, "Heap": random_100k_heap.result, "Insertion": random_100k_insertion.result, "Merge": random_100k_merge.result},
    # Descending
    {"Type": 'descending', "Quantity": '10k', "Bubble": descending_10k_bubble.result, "Heap": descending_10k_heap.result, "Insertion": descending_10k_insertion.result, "Merge": descending_10k_merge.result},
    {"Type": 'descending', "Quantity": '50k', "Bubble": descending_50k_bubble.result, "Heap": descending_50k_heap.result, "Insertion": descending_50k_insertion.result, "Merge": descending_50k_merge.result},
    {"Type": 'descending', "Quantity": '100k', "Bubble": descending_100k_bubble.result, "Heap": descending_100k_heap.result, "Insertion": descending_100k_insertion.result, "Merge": descending_100k_merge.result},
    # Descending
    {"Type": 'ascending', "Quantity": '10k', "Bubble": ascending_10k_bubble.result, "Heap": ascending_10k_heap.result, "Insertion": ascending_10k_insertion.result, "Merge": ascending_10k_merge.result},
    {"Type": 'ascending', "Quantity": '50k', "Bubble": ascending_50k_bubble.result, "Heap": ascending_50k_heap.result, "Insertion": ascending_50k_insertion.result, "Merge": ascending_50k_merge.result},
    {"Type": 'ascending', "Quantity": '100k', "Bubble": ascending_100k_bubble.result, "Heap": ascending_100k_heap.result, "Insertion": ascending_100k_insertion.result, "Merge": ascending_100k_merge.result},
]

table = pd.DataFrame(items)
print(table)
