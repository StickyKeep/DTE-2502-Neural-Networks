import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file and reshape the grid to 48x48
file_path = '/Users/gwwf/Downloads/message_this.txt'
grid_df = pd.read_csv(file_path, header=None, delimiter='\t')
grid = grid_df.to_numpy()
grid_reshaped = np.reshape(grid, (48, 48))

# Initialize variables
initial_value = 333
goal = (47, 47)
start = (0, 0)
successful_path = []

# DFS function for path finding with early stopping
def dfs(position, value, grid, path):
    global successful_path

    row, col = position

    if value < 1:
        return False

    if position == goal:
        if value == 1:
            successful_path = path.copy()
            return True
        else:
            return False

    if col + 1 < grid.shape[1]:
        new_value = value + grid[row, col + 1]
        if dfs((row, col + 1), new_value, grid, path + [(row, col + 1)]):
            return True

    if row + 1 < grid.shape[0]:
        new_value = value + grid[row + 1, col]
        if dfs((row + 1, col), new_value, grid, path + [(row + 1, col)]):
            return True

    return False

# Run the DFS algorithm
dfs_result = dfs(start, initial_value + grid_reshaped[start], grid_reshaped, [start])

# Visualize the path if successful
if dfs_result:
    plt.figure(figsize=(12, 12))
    sns.heatmap(grid_reshaped, cmap="coolwarm", annot=False, cbar=True, square=True)

    rows, cols = zip(*successful_path)
    plt.scatter(cols, rows, c='green', marker='o', s=100, label='Path')
    plt.title("Grid with Successful Path")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    plt.legend()
    plt.show()

    path_values = [grid_reshaped[row, col] for row, col in successful_path]
    path_values_str = " + ".join(map(str, path_values))
    print(f"Path Values: {path_values_str}")
else:
    print("No successful path found.")
