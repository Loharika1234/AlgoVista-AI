import numpy as np
import pandas as pd
import time 
from algorithms.sorting import mergesort
def benchmark_merge_sort():
    sizes=[100,500,1000,5000,10000]
    results=[]
    for size in sizes:
        arr=np.random.randint(1,100000,size).tolist()
        times=[]
        for run in range(5):
            start = time.perf_counter()
            mergesort(arr)
            end=time.perf_counter()
            times.append(end-start)
        avg_time=sum(times)/len(times)
        results.append({
            "Input Size":size,
            "Average Time":avg_time,
            "Median Time":np.median(times)
        })
    return pd.DataFrame(results)