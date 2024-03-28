import matplotlib.pyplot as plt
import numpy as np

def flood_fill(matrix, x, y, target_color, replacement_color):
    if matrix[x, y] == target_color and matrix[x, y] != replacement_color:
        matrix[x, y] = replacement_color
        if x > 0:
            flood_fill(matrix, x - 1, y, target_color, replacement_color)
        if x < matrix.shape[0] - 1:
            flood_fill(matrix, x + 1, y, target_color, replacement_color)
        if y > 0:
            flood_fill(matrix, x, y - 1, target_color, replacement_color)
        if y < matrix.shape[1] - 1:
            flood_fill(matrix, x, y + 1, target_color, replacement_color)

# Create a sample matrix
width, height = 10, 10
matrix = np.zeros((width, height))

# Set a region to be filled initially
matrix[2:5, 2:5] = 1

# Take user input for target and replacement colors
target_color = int(input("Enter target color code (0 or 1): "))
replacement_color = int(input("Enter replacement color code: "))

# Perform flood fill
flood_fill(matrix, 3, 3, target_color, replacement_color)

# Plot the result
plt.imshow(matrix, cmap='viridis', origin='upper')
plt.title("Flood Fill Algorithm")
plt.show()
