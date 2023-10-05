import time
from src.sorts.insertion import insertion_sort
from src.random.number.with10k.items import random_number_10k

print('Running "random - number - 10k - insertion"')

start_time = time.perf_counter()

insertion_sort(random_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
