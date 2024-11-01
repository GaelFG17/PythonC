import numpy as np
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt

def plot_function(equation):
    x = np.linspace(-10, 10, 400)
    y = eval(equation)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of {equation}')
    plt.grid(True)
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    equation = simpledialog.askstring("Input", "Enter a function of x (e.g., np.sin(x), x**2, etc.):")
    if equation:
        plot_function(equation)

if __name__ == "__main__":
    main()