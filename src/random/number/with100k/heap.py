import time
from src.sorts.heap import heap_sort
from src.random.number.with100k.items import random_number_100k

print('Running "random - number - 100k - heap"')

start_time = time.perf_counter()

heap_sort(random_number_100k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
