from analysis.time_analyzer import benchmarck_merge_sort
results=benchmarck_merge_sort()
print("\nMERGESORT PERFORMANCE REPORT")
print(results.to_string(index=False))
print("\n BenchMark Completed Successfully!")