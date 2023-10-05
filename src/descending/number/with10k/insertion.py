import time
from src.sorts.insertion import insertion_sort
from src.descending.number.with10k.items import descending_number_10k

start_time = time.perf_counter()

insertion_sort(descending_number_10k)

end_time = time.perf_counter()

result = end_time - start_time
