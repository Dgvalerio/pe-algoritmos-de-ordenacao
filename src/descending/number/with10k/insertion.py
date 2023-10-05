import time
from src.sorts.insertion import insertion_sort
from src.descending.number.with10k.items import descending_number_10k

print('Running "descending - number - 10k - insertion"')

start_time = time.perf_counter()

insertion_sort(descending_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
