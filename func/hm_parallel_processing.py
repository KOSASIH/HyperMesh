import os
import time
import random
import dask
from dask.distributed import Client
from multiprocessing.pool import ThreadPool

def expensive_function(x):
    """An example of an expensive function that takes a long time to compute."""
    time.sleep(1)
    return x**2

def multi_threading():
    """Demonstrates multi-threading with the `concurrent.futures` library."""
    with ThreadPool(os.cpu_count()) as pool:
        results = pool.map(expensive_function, range(10))
    print("Multi-threading results:", results)

def distributed_computing():
    """Demonstrates distributed computing with the `dask` library."""
    client = Client()
    futures = client.map(expensive_function, range(10))
    results = client.gather(futures)
    print("Distributed computing results:", results)

if __name__ == "__main__":
    start_time = time.time()
    multi_threading()
    print("Multi-threading time:", time.time() - start_time)

    start_time = time.time()
    distributed_computing()
    print("Distributed computing time:", time.time() - start_time)
