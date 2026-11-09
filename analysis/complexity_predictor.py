import numpy as np
def predict_complexity(results):
    n = results["Input Size"].to_numpy(dtype=float)
    t = results["Average Time"].to_numpy(dtype=float)
    if np.any(n <= 1) or np.any(t <= 0):
        raise ValueError(
            "Input sizes must exceed 1 and times must be positive."
        )
    models = {
        "O(log n)": np.log2(n),
        "O(n)": n,
        "O(n log n)": n * np.log2(n),
        "O(n²)": n ** 2
    }
    log_time = np.log(t)
    predictions = {}
    for name, growth in models.items():
        log_growth = np.log(growth)
        # Estimate only the constant multiplier
        intercept = np.mean(log_time - log_growth)
        predicted = log_growth + intercept
        ss_res = np.sum(
            (log_time - predicted) ** 2
        )
        ss_tot = np.sum(
            (log_time - np.mean(log_time)) ** 2
        )
        r_squared = (
            1 - ss_res / ss_tot
            if ss_tot > 0 else 0
        )
        predictions[name] = {
            "R2 Score": r_squared
        }
    best_model = max(
        predictions,
        key=lambda x: predictions[x]["R2 Score"]
    )
    return best_model, predictions