from scipy.signal import butter, filtfilt
import numpy as np
 
def moving_average(values,timestamps, window_size = 10):
    # Apply moving average filter with a window size
    smoothed_values = np.convolve(values, np.ones(window_size)/window_size, mode='valid')

    # Adjust timestamps after applying the moving average filter
    # because the result is shorter than the original signal
    smoothed_timestamps = timestamps[:len(smoothed_values)]

    return smoothed_values,smoothed_timestamps

def low_pass(values,cutoff = 0.001):
     # Desired cutoff frequency of the filter, Hz (must be less than fs/2)
    # Sampling frequency and cutoff frequency
    fs = 1 / (1 * 60)  # Sample rate, Hz (e.g., one data point every 5 minutes)
    

    # Calculate Nyquist frequency
    nyquist = 0.5 * fs

    # Order of the filter
    order = 6
    
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    values = filtfilt(b, a, values)
    return values