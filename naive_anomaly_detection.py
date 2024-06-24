import numpy as np 
import datetime as dt
import matplotlib.dates as md

def anomaly_detection(temperatures, timestamps, threshold):
    # Calculate the time differences (converted to seconds)
    time_deltas = np.diff(timestamps) * 24 * 3600

    # Calculate the differences in temperature
    temperature_deltas = np.diff(temperatures)
    # Calculate the derivatives (rate of temperature change)
    derivatives = temperature_deltas / time_deltas

    # Detect points where the absolute value of the derivative exceeds the threshold
    abnormal = np.abs(derivatives) > threshold
    # Filter out consecutive abnormal points, only keeping the first in a series
    abnormal_indices = []
    for i in range(len(abnormal)):
        if abnormal[i] and (i == 0 or not abnormal[i - 1]):
            abnormal_indices.append(i)

    # Return the timestamps for points of abnormal temperature rise
    abnormal_times = [timestamps[i+1] for i in abnormal_indices]  # i+1 because the derivative is calculated between points

    # Convert back the abnormal timestamps from Matplotlib date numbers to datetime objects
    dates = [md.num2date(num) for num in abnormal_times]

    return dates

# every 10 minutes check how many anomalies are there, 
# according to the number of anomalies, classify the warning level
def classify_anomalies(anomalies, window=dt.timedelta(minutes = 10)):
    #Classify anomalies based on frequency within a time window.
    warnings = []
    if not anomalies:  # Check if the anomalies list is empty
        return warnings
    
    start = anomalies[0]
    count = 1
    
    for i in range(1, len(anomalies)):
        # If the time difference between two anomalies is less than the window, increment the count
        if anomalies[i] - start <= window:
            count += 1
        else:
            if count >= 3:
                warnings.append((start, 'High'))
            elif count == 2:
                warnings.append((start, 'Medium'))
            else:
                warnings.append((start, 'Low'))
            start = anomalies[i]
            count = 1
    
    # Check last segment
    if count >= 3:
        warnings.append((start, 'High'))
    elif count ==2:
        warnings.append((start, 'Medium'))
    else:
        warnings.append((start, 'Low'))
    
    return warnings