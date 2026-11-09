from analysis.time_analyzer import benchmark_merge_sort
from analysis.complexity_predictor import predict_complexity
# Generate benchmark data
results = benchmark_merge_sort()
# Predict complexity
best, scores = predict_complexity(results)
print("\nCOMPLEXITY ANALYSIS REPORT")
for model, details in scores.items():
    print(
        model,
        "R2 Score:",
        round(details["R2 Score"], 4),
        # "Slope:",
        # round(details["Slope"], 4)
    )
print("\nBest fitting model:", best)