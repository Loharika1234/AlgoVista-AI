from algorithms.sorting import mergesort
nums=[45,12,89,3,25,7,61]
result=mergesort(nums)
print("Original Array:",nums)
print("Sorted Array:",result["sorted_array"])
print("Comparisons:",result["comparisons"])
print("Executiobn Time:",result["execution_time"],"seconds")
print("Peak Memory",result["peak_memory"],"bytes")