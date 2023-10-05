import time
from src.sorts.heap import heap_sort
from src.ascending.number.with100k.items import ascending_number_100k

print('Running "ascending - number - 100k - heap"')

start_time = time.perf_counter()

heap_sort(ascending_number_100k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
