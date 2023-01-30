import os; import psutil; import timeit
from datasets import load_dataset

mem_before = psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
wiki = load_dataset("wikipedia", "20220301.en", split="train")
mem_after = psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)

print(f"RAM memory used: {(mem_after - mem_before)} MB")

s = """batch_size = 1000
for batch in wiki.iter(batch_size):
    ...
"""

time = timeit.timeit(stmt=s, number=1, globals=globals())
print(f"Time to iterate over the {wiki.dataset_size >> 30} GB dataset: {time:.1f} sec, "
      f"ie. {float(wiki.dataset_size >> 27)/time:.1f} Gb/s")