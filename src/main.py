import pandas as pd

from src.random.number.with10k import merge as random_10k_merge, heap as random_10k_heap, insertion as random_10k_insertion, bubble as random_10k_bubble
from src.random.number.with50k import merge as random_50k_merge, heap as random_50k_heap, insertion as random_50k_insertion, bubble as random_50k_bubble
from src.random.number.with100k import merge as random_100k_merge, heap as random_100k_heap, insertion as random_100k_insertion, bubble as random_100k_bubble

from src.descending.number.with10k import merge as descending_10k_merge, heap as descending_10k_heap, insertion as descending_10k_insertion, bubble as descending_10k_bubble
from src.descending.number.with50k import merge as descending_50k_merge, heap as descending_50k_heap, insertion as descending_50k_insertion, bubble as descending_50k_bubble
from src.descending.number.with100k import merge as descending_100k_merge, heap as descending_100k_heap, insertion as descending_100k_insertion, bubble as descending_100k_bubble

# print(f"# 10K")
# print(f"O Bubble sort organizou os itens em {bubble_10k.result} segundos")
# print(f"O Heap sort organizou os itens em {heap_10k.result} segundos")
# print(f"O Insertion sort organizou os itens em {insertion_10k.result} segundos")
# print(f"O Merge sort organizou os itens em {merge_10k.result} segundos")
#
# print(f"# 50K")
# print(f"O Bubble sort organizou os itens em {bubble_50k.result} segundos")
# print(f"O Heap sort organizou os itens em {heap_50k.result} segundos")
# print(f"O Insertion sort organizou os itens em {insertion_50k.result} segundos")
# print(f"O Merge sort organizou os itens em {merge_50k.result} segundos")
#
# print(f"# 100K")
# print(f"O Bubble sort organizou os itens em {bubble_100k.result} segundos")
# print(f"O Heap sort organizou os itens em {heap_100k.result} segundos")
# print(f"O Insertion sort organizou os itens em {insertion_100k.result} segundos")
# print(f"O Merge sort organizou os itens em {merge_100k.result} segundos")

items = [
    # Random
    {"Type": 'random', "Quantity": '10k', "Bubble": random_10k_bubble.result, "Heap": random_10k_heap.result, "Insertion": random_10k_insertion.result, "Merge": random_10k_merge.result},
    {"Type": 'random', "Quantity": '50k', "Bubble": random_50k_bubble.result, "Heap": random_50k_heap.result, "Insertion": random_50k_insertion.result, "Merge": random_50k_merge.result},
    {"Type": 'random', "Quantity": '100k', "Bubble": random_100k_bubble.result, "Heap": random_100k_heap.result, "Insertion": random_100k_insertion.result, "Merge": random_100k_merge.result},
    # Descending
    {"Type": 'descending', "Quantity": '10k', "Bubble": descending_10k_bubble.result, "Heap": descending_10k_heap.result, "Insertion": descending_10k_insertion.result, "Merge": descending_10k_merge.result},
    {"Type": 'descending', "Quantity": '50k', "Bubble": descending_50k_bubble.result, "Heap": descending_50k_heap.result, "Insertion": descending_50k_insertion.result, "Merge": descending_50k_merge.result},
    {"Type": 'descending', "Quantity": '100k', "Bubble": descending_100k_bubble.result, "Heap": descending_100k_heap.result, "Insertion": descending_100k_insertion.result, "Merge": descending_100k_merge.result},
]

table = pd.DataFrame(items)
print(table)
