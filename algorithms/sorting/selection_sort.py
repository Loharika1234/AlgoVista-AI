import time
import tracemalloc
def selectionsort(numbers):
  """
  sorts a list of numbers using the slection sort algorithm.
  returns:
    sorted_array: Sorted list
    comaprisons: number of comparisons performed 
    execution_time: Time taekn to sort
    peak_memory: Peaqk memory used in bytes
  """
  if not isinstance(numbers,list):
    raise TypeError("Input must be a list.")
  if any(type(num) is not int for num in numbers):
    raise ValueError("All elements must be integers.")
  arr=numbers.copy()
  n=len(arr)
  comparisons=0
  tracemalloc.start()
  start_time=time.perf_counter()
  try:
    for i in range(n-1):
      min_index=i
      for j in range(i+1,n):
        comparisons+=1
        if arr[j]<arr[min_index]:
          min_index=j
      if min_index!=i:
        arr[i],arr[min_index]=arr[min_index],arr[i]
    execution_time=time.perf_counter()-start_time
    _,peak_memory=tracemalloc.get_traced_memory()
  finally:
    tracemalloc.stop()
  return arr,comparisons,execution_time,peak_memory
