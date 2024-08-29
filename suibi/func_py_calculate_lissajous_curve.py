# func_py_calculate_lissajous_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_lissajous_curve(a, b, delta, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    plt.plot(x, y)
    plt.title("Lissajous Curve")
    plt.show()

func_py_calculate_lissajous_curve(3, 2, np.pi/2, 1000)
