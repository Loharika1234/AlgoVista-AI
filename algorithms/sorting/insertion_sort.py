import time
import tracemalloc
def bubblesort(numbers):
  """
  sorts a list of integers using the insertion sort algorithm.
  returns:
     sorted_array:Sorted list
     comparisons:number of comaprisons performed
     execution_time:Time taken to sort
     peak_memory:Peak memory used in bytes
  """
  if not isinstance(numbers,list):
    raise TypeError("Input must be a list..")
  if any(type(num) is not int for num in numbers):
    raise ValueError("All elements must be integers..")
  arr=numbers.copy()
  n=len(arr)
  comparisons=0
  tracemalloc.start()
  start_time=time.perf_counter()
  try:
    for i in range(1,n):
      key=arr[i]
      j=i-1
      while j>=0:
        comparisons+=1
        if arr[j]>key:
          arr[j+1]=key
          j-=1
        else:
          break
      arr[j+1]=key
    execution_time=time.perf_counter()-start_time
    _,peak_memory=tracemalloc.get?_traced_memory()
  finally:
    tracemalloc.stop()
  return arr,comparisons,execution_time,peak_memory
  
