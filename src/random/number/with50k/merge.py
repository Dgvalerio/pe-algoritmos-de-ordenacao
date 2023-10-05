import time
from src.sorts.merge import merge_sort
from src.random.number.with50k.items import random_number_50k

start_time = time.perf_counter()

merge_sort(random_number_50k)

end_time = time.perf_counter()

result = end_time - start_time
