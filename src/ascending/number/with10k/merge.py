import time
from src.sorts.merge import merge_sort
from src.ascending.number.with10k.items import ascending_number_10k

print('Running "ascending - number - 10k - merge"')

start_time = time.perf_counter()

merge_sort(ascending_number_10k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
