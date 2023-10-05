import time
from src.sorts.insertion import insertion_sort
from src.descending.number.with100k.items import descending_number_100k

start_time = time.perf_counter()

insertion_sort(descending_number_100k)

end_time = time.perf_counter()

result = end_time - start_time
