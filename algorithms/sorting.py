import time
import tracemalloc
def mergesort(arr):
    comparisons=0
    def divide(values):
        nonlocal comparisons 
        if len(values)<=1:
            return values
        mid=len(values)//2
        left=divide(values[:mid])
        right=divide(values[mid:])
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            comparisons+=1
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    tracemalloc.start()
    start_time=time.perf_counter()
    sorted_array=divide(arr.copy())
    end_time=time.perf_counter()
    current_memory,peak_memory=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time=end_time-start_time
    return {
        "sorted_array":sorted_array,
        "comparisons":comparisons,
        "execution_time":execution_time,
        "peak_memory":peak_memory
    }