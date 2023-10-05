import time
from src.sorts.merge import merge_sort
from src.random.number.with100k.items import random_number_100k

start_time = time.perf_counter()

merge_sort(random_number_100k)

end_time = time.perf_counter()

result = end_time - start_time
