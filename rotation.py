


#b) rotation 

import matplotlib.pyplot as plt
import math
import numpy as np

def calculate_sin_cos(angle_in_degree):
    angle_in_radian = math.radians(angle_in_degree)
    sin = math.sin(angle_in_radian)
    cos = math.cos(angle_in_radian)
    return sin, cos

angle = float(input("Enter the angle in degrees: "))
sin, cos = calculate_sin_cos(angle)

start_x  = int(input("Enter the starting coordinates for x : "))
start_y = int(input("Enter the starting coordinates for y : "))
end_x = int(input("Enter the ending coordinates for x : "))
end_y = int(input("Enter the ending coordinates for y : "))

start_vector = np.array([start_x, start_y])
end_vector = np.array([end_x, end_y])

rotation_matrix = np.array([[cos, -sin],
                            [sin, cos]])

print("Matrix before rotation:")
print("Start Vector:\n", start_vector)
print("End Vector:\n", end_vector)

result = np.matmul(start_vector, rotation_matrix)

print("\nMatrix after rotation:")
print("Result Vector:\n", result)



print("Result after rotation:", result)

# Plotting vectors
vectors = [start_vector, end_vector, result]
colors = ['r', 'g', 'b']
labels = ['Start Vector', 'End Vector', 'Result']

for vector, color, label in zip(vectors, colors, labels):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)
print("Asmita pokhrel")
plt.title('Rotation')
plt.xlabel("X-label")
plt.ylabel("Y-label")
plt.legend()
plt.grid()
plt.show()