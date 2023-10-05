import time
from src.sorts.heap import heap_sort
from src.descending.number.with10k.items import descending_number_10k

print('Running "descending - number - 10k - heap"')

start_time = time.perf_counter()

heap_sort(descending_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
