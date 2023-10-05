import time
from src.sorts.bubble import bubble_sort
from src.descending.number.with50k.items import descending_number_50k

start_time = time.perf_counter()

bubble_sort(descending_number_50k)

end_time = time.perf_counter()

result = end_time - start_time
