import time
from src.sorts.insertion import insertion_sort
from src.random.number.with100k.items import random_number_100k

start_time = time.perf_counter()

insertion_sort(random_number_100k)

end_time = time.perf_counter()

result = end_time - start_time
