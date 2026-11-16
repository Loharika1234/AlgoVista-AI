import time
import tracemalloc
def bubblesort(numbers):
  """
  sorts a list of integers using the heapsort algorithm.
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
    def heapify(size,root):
      nonlocal comparisons
      largest= root
      left=2*root+1
      right=2*root+2
      if left < size:
        comparisons+=1
        if arr[left]>arr[largest]:
          largest=left
      if right<size:
        comparisons+=1
        if arr[right]>arr[largest]
          largest=right
      if largest!=root:
        arr[root],arr[largest]=arr[largest],arr[root]
        heapify(size,largest)
    #build a max heap
    for i in range(n//2 - 1 ,-1 ,-1):
      heapify(n,i)
    #extract elements from the heap
    for i in range(n-1,0,-1):
      arr[0],arr[i]=arr[i],arr[0]

    execution_time=time.perf_counter()-start_time
    _,peak_memory=tracemalloc.get?_traced_memory()
  finally:
    tracemalloc.stop()
  return arr,comparisons,execution_time,peak_memory
  
