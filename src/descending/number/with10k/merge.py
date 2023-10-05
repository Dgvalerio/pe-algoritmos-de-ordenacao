import time
from src.sorts.merge import merge_sort
from src.descending.number.with10k.items import descending_number_10k

print('Running "descending - number - 10k - merge"')

start_time = time.perf_counter()

merge_sort(descending_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
