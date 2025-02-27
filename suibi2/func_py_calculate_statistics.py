# func_py_calculate_statistics.py
import numpy as np

def calculate_statistics(data):
    """
    Calculate basic statistics (mean, median, std dev) from a list of numbers.
    """
    if not data:
        raise ValueError("Input data cannot be empty.")
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    
    return {
        "mean": mean,
        "median": median,
        "std_dev": std_dev
    }

# Example usage
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    stats = calculate_statistics(data)
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std_dev']}")
