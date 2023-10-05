import time
from src.sorts.heap import heap_sort
from src.ascending.number.with50k.items import ascending_number_50k

print('Running "ascending - number - 50k - heap"')

start_time = time.perf_counter()

heap_sort(ascending_number_50k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
