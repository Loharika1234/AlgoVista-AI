import time
import tracemalloc
def bubblesort(numbers):
  """
  sorts a list of integers using the quicksort algorithm.
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
    def partition(low,high):
      nonlocal comaprisons
      pivot=arr[high]
      i=low-1
      for j in range(low,high):
        comparisons+=1
        if arr[j]<=pivot:
          i+=1
          arr[i],arr[j]=arr[j],arr[i]
      arr[i+1],arr[high]=arr[high],arr[i+1]
      return i+1
    def quick_sort_recursive(low,high):
      if low<high:
        pivot_index=partition(low,high)
    quick_sort_recursive(low,pivot_index-1)
    quick_sort_recursive(0,len(arr)-1)
    execution_time=time.perf_counter()-start_time
    _,peak_memory=tracemalloc.get?_traced_memory()
  finally:
    tracemalloc.stop()
  return arr,comparisons,execution_time,peak_memory
  
