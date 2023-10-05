import time
from src.sorts.heap import heap_sort
from src.random.number.with10k.items import random_number_10k

print('Running "random - number - 10k - heap"')

start_time = time.perf_counter()

heap_sort(random_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
