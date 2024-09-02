# func_py_calculate_lemniscate_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_lemniscate_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.sqrt(2) * np.cos(t) / (1 + np.sin(t)**2)
    y = a * np.sqrt(2) * np.sin(t) * np.cos(t) / (1 + np.sin(t)**2)
    plt.plot(x, y)
    plt.title("Lemniscate Curve")
    plt.show()

func_py_calculate_lemniscate_curve(5, 1000)
