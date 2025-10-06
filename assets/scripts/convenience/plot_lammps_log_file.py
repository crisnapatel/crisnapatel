
import pandas as pd
import matplotlib.pyplot as plt
import math
import os
import argparse

def plot_lammps_log_dynamic(file_path):
    header_found = False
    header_line = None
    skip_rows = 0  # Number of rows to skip when reading the DataFrame
    data_lines = []  # To store the lines containing numerical data
    
    # Open the file and read lines until we find the header
    with open(file_path, 'r') as f:
        for line in f:
            skip_rows += 1
            # A simple heuristic to identify a header line: it should contain 'Step' and not any numeric values
            if 'Step' in line and not any(char.isdigit() for char in line):
                header_line = line.strip()
                header_found = True
                break
    
    # If header is found, proceed to read and collect data lines
    if header_found:
        with open(file_path, 'r') as f:
            # Skip the lines before the header
            for _ in range(skip_rows):
                next(f)
            
            # Collect lines that contain numerical data
            for line in f:
                if all(char.isdigit() or char.isspace() or char == '.' or char == '-' for char in line.strip()):
                    data_lines.append(line.strip())
                else:
                    break
        
        # Convert the list of data lines into a DataFrame
        df = pd.DataFrame([line.split() for line in data_lines], columns=header_line.split(), dtype=float)
        
        # Calculate the number of subplots needed (ignoring 'Step' column)
        num_subplots = len(df.columns) - 1

        # Calculate the number of rows needed for subplots
        num_rows = math.ceil(num_subplots / 2.0)
        
        # Create a figure window with multiple subplots arranged in a grid
        fig, axes = plt.subplots(num_rows, 2, figsize=(15, 6 * num_rows))
        
        # If only one row, axes will be a 1D array, so make it 2D for uniformity
        if num_rows == 1:
            axes = axes.reshape(1, -1)
        
        axes = axes.flatten()  # Flatten the 2D array to 1D for easy indexing
        
        # Plot each column against 'Step' in its respective subplot
        for i, column in enumerate(df.columns):
            if column != 'Step':
                ax = axes[i - 1]  # Adjust index to exclude 'Step'
                ax.plot(df['Step'], df[column])
                ax.set_title(f"{column} vs Step")
                ax.set_xlabel('Step')
                ax.set_ylabel(column)
        
        # Remove any unused subplots
        for i in range(num_subplots, len(axes)):
            fig.delaxes(axes[i])
        
        # Add a title for the entire figure
        fig.suptitle(f"Plots for {os.path.basename(file_path)}", fontsize=16)
        
        # Show the figure
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
    else:
        print(f"Header not found in {file_path}. Skipping this file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot LAMMPS log file")
    parser.add_argument("file_path", help="Path to the LAMMPS log file")
    
    args = parser.parse_args()
    plot_lammps_log_dynamic(args.file_path)
