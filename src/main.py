from src.random.number.with10k import merge as merge_10k, heap as heap_10k, insertion as insertion_10k, \
    bubble as bubble_10k

print(f"O Bubble sort organizou os itens em {bubble_10k.result} segundos")
print(f"O Heap sort organizou os itens em {heap_10k.result} segundos")
print(f"O Insertion sort organizou os itens em {insertion_10k.result} segundos")
print(f"O Merge sort organizou os itens em {merge_10k.result} segundos")
