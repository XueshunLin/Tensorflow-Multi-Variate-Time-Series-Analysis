import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np

def log_vis(timestamps, labels, values_lists,label=None, ax= None):
    # xfmt = md.DateFormatter("%H:%M")
    if ax is None:
        fig, ax = plt.subplots()
    # ax.xaxis.set_major_formatter(xfmt)
    ax.locator_params(axis='x', nbins=10)  # Adjusted for better visibility
    
    if type(values_lists) is not list:
        shifted_values_lists = [values_lists]
    else:
        # Shift each values list by dividing by the first value (plot original value if the first value is 0)
        shifted_values_lists = [np.array(values) / values[0] if values[0] != 0 else np.array(values) + 1 for values in values_lists]
    
    if label is not None:
        ax.semilogy(timestamps, shifted_values_lists[0] + 1, label=label)
    else:
        # Plot each shifted values list with logarithmic y-axis
        for i, values in enumerate(shifted_values_lists):
            ax.semilogy(timestamps, values + 1, label=labels[i]) # Add 1 to avoid log(0)
    
    plt.grid()
    plt.ylabel("Shifted Value (log scale)")
    plt.xlabel("Time")
    plt.tight_layout()
    plt.legend()  # Use provided labels

def normal_vis(timestamps, values, label = None, ax = None):
    xfmt = md.DateFormatter("%H:%M")

    if ax is None:
        fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(xfmt)
    ax.locator_params(axis='x', nbins=10)  # Adjusted for better visibility
    
    ax.plot(timestamps, values, label = label)
    if label:
        ax.legend()
    
    plt.grid()
    plt.ylabel("Value")
    plt.xlabel("Time")
    plt.tight_layout()
