import time
from src.sorts.insertion import insertion_sort
from src.ascending.number.with100k.items import ascending_number_100k

print('Running "ascending - number - 100k - insertion"')

start_time = time.perf_counter()

insertion_sort(ascending_number_100k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
