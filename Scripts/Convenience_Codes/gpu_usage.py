import os
import subprocess
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# function to get GPU usage
def get_gpu_usage():
    """Function to get the current GPU usage as a percentage"""
    gpu_usage = subprocess.check_output(
        "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits", 
        shell=True
    )
    return float(gpu_usage)

# DataFrame to store all GPU usage data
gpu_usage_df = pd.DataFrame(columns=['timestamp', 'gpu_usage'])

def update_gpu_usage(i):
    """Function to update the GPU usage data"""
    global gpu_usage_df  # use the global DataFrame
    gpu_usage = get_gpu_usage()
    timestamp = time.time()  # get timestamp as a float
    # Append new data to the DataFrame
    gpu_usage_df = gpu_usage_df.append({'timestamp': timestamp, 'gpu_usage': gpu_usage}, ignore_index=True)

# Function to animate the plot
def animate(i, xs, ys):
    # append current relative time (subtract start time) and GPU usage to the lists
    xs.append(time.time() - start_time)
    ys.append(get_gpu_usage())

    # draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('GPU Usage over Time')
    plt.ylabel('GPU Usage (%)')
    plt.xlabel('Tims (S)')

def close_event():
    """handler for figure window close event"""
    print("Closing GPU monitor, writing data to Parquet file...")
    # Subtract start time from all timestamps to make them relative
    gpu_usage_df['timestamp'] -= start_time
    gpu_usage_df.to_parquet('gpu_usage.parquet')
    os._exit(0)  # close the entire script

# get the start time
start_time = time.time()

# create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []

# set up animation
ani = FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)

# on close event
fig.canvas.mpl_connect('close_event', close_event)

# show plot
plt.show()

