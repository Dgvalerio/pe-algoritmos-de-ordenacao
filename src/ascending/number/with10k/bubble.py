import time
from src.sorts.bubble import bubble_sort
from src.ascending.number.with10k.items import ascending_number_10k

start_time = time.perf_counter()

bubble_sort(ascending_number_10k)

end_time = time.perf_counter()

result = end_time - start_time
