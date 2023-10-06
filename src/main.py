from datetime import datetime
import json

from src.random.number.with10k import merge as random_10k_merge, heap as random_10k_heap, \
    insertion as random_10k_insertion, bubble as random_10k_bubble
from src.random.number.with50k import merge as random_50k_merge, heap as random_50k_heap, \
    insertion as random_50k_insertion, bubble as random_50k_bubble
from src.random.number.with100k import merge as random_100k_merge, heap as random_100k_heap, \
    insertion as random_100k_insertion, bubble as random_100k_bubble

from src.descending.number.with10k import merge as descending_10k_merge, heap as descending_10k_heap, \
    insertion as descending_10k_insertion, bubble as descending_10k_bubble
from src.descending.number.with50k import merge as descending_50k_merge, heap as descending_50k_heap, \
    insertion as descending_50k_insertion, bubble as descending_50k_bubble
from src.descending.number.with100k import merge as descending_100k_merge, heap as descending_100k_heap, \
    insertion as descending_100k_insertion, bubble as descending_100k_bubble

from src.ascending.number.with10k import merge as ascending_10k_merge, heap as ascending_10k_heap, \
    insertion as ascending_10k_insertion, bubble as ascending_10k_bubble
from src.ascending.number.with50k import merge as ascending_50k_merge, heap as ascending_50k_heap, \
    insertion as ascending_50k_insertion, bubble as ascending_50k_bubble
from src.ascending.number.with100k import merge as ascending_100k_merge, heap as ascending_100k_heap, \
    insertion as ascending_100k_insertion, bubble as ascending_100k_bubble

data = {
    "random": {
        "10k": { "bubble": random_10k_bubble.result, "heap": random_10k_heap.result, "insertion": random_10k_insertion.result, "merge": random_10k_merge.result },
        "50k": { "bubble": random_50k_bubble.result, "heap": random_50k_heap.result, "insertion": random_50k_insertion.result, "merge": random_50k_merge.result },
        "100k": { "bubble": random_100k_bubble.result, "heap": random_100k_heap.result, "insertion": random_100k_insertion.result, "merge": random_100k_merge.result },
    },
    "descending": {
        "10k": { "bubble": descending_10k_bubble.result, "heap": descending_10k_heap.result, "insertion": descending_10k_insertion.result, "merge": descending_10k_merge.result },
        "50k": { "bubble": descending_50k_bubble.result, "heap": descending_50k_heap.result, "insertion": descending_50k_insertion.result, "merge": descending_50k_merge.result },
        "100k": { "bubble": descending_100k_bubble.result, "heap": descending_100k_heap.result, "insertion": descending_100k_insertion.result, "merge": descending_100k_merge.result },
    },
    "ascending": {
        "10k": { "bubble": ascending_10k_bubble.result, "heap": ascending_10k_heap.result, "insertion": ascending_10k_insertion.result, "merge": ascending_10k_merge.result },
        "50k": { "bubble": ascending_50k_bubble.result, "heap": ascending_50k_heap.result, "insertion": ascending_50k_insertion.result, "merge": ascending_50k_merge.result },
        "100k": { "bubble": ascending_100k_bubble.result, "heap": ascending_100k_heap.result, "insertion": ascending_100k_insertion.result, "merge": ascending_100k_merge.result }
    }
}

now = datetime.now()
iso = now.isoformat()


with open(f"data/{iso.replace(':', '-')}.json", 'w') as file:
    json.dump(data, file)
