from src.random.number.with10k import merge as merge_10k, heap as heap_10k, insertion as insertion_10k, \
    bubble as bubble_10k
from src.random.number.with50k import merge as merge_50k, heap as heap_50k, insertion as insertion_50k, \
    bubble as bubble_50k
from src.random.number.with100k import merge as merge_100k, heap as heap_100k, insertion as insertion_100k, \
    bubble as bubble_100k

print(f"# 10K")
print(f"O Bubble sort organizou os itens em {bubble_10k.result} segundos")
print(f"O Heap sort organizou os itens em {heap_10k.result} segundos")
print(f"O Insertion sort organizou os itens em {insertion_10k.result} segundos")
print(f"O Merge sort organizou os itens em {merge_10k.result} segundos")

print(f"# 50K")
print(f"O Bubble sort organizou os itens em {bubble_50k.result} segundos")
print(f"O Heap sort organizou os itens em {heap_50k.result} segundos")
print(f"O Insertion sort organizou os itens em {insertion_50k.result} segundos")
print(f"O Merge sort organizou os itens em {merge_50k.result} segundos")

print(f"# 100K")
print(f"O Bubble sort organizou os itens em {bubble_100k.result} segundos")
print(f"O Heap sort organizou os itens em {heap_100k.result} segundos")
print(f"O Insertion sort organizou os itens em {insertion_100k.result} segundos")
print(f"O Merge sort organizou os itens em {merge_100k.result} segundos")
