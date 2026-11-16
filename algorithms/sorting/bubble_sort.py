import time
import tracemalloc
def bubblesort(numbers):
  """
  sorts a list of integers using the bubblesort algorithm.
  returns:
     sorted_array:Sorted list
     comparisons:number of comaprisons performed
     execution_time:Time taken to sort
     peak_memory:Peak memory used in bytes
  """
  if not isinstance(numbers,list):
    raise ValueError("Input must be a list..")
  if any(type(num) is not int for num in numbers):
    raise ValueError("All elements must be integers..")
  arr=numbers.copy()
  n=len(arr)
  comparisons=0
  tracemalloc.start()
  start_time=time.perf_counter()
  try:
    for i in range(n-1):
      swapped = False
      for j in range(n-i-1):
        comparisons+=1
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]
          swapped=True
      if not swapped:
        break
    execution_time=time.perf_counter()-start_time
    _,peak_memory=tracemalloc.get?_traced_memory()
  finally:
    tracemalloc.stop()
  return arr,comparisons,execution_time,peak_memory
  
