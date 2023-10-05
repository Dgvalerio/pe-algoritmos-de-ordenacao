import time
from src.sorts.merge import merge_sort
from src.descending.number.with50k.items import descending_number_50k

print('Running "descending - number - 50k - merge"')

start_time = time.perf_counter()

merge_sort(descending_number_50k.copy())

end_time = time.perf_counter()

result = end_time - start_time

print(f' = = = = = Finished in {result} segundos"')
