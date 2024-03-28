import matplotlib.pyplot as plt

# Get user input for number of vertices
num_vertices = int(input("Enter the number of vertices: "))

# Initialize empty lists for data
vertices = []
col_labels = []

# Get user input for each vertex
for i in range(num_vertices):
  label = input("Enter vertex label (e.g., A, B, C): ")
  x_coord = float(input(f"Enter x-coordinate for vertex {label}: "))
  y_coord = float(input(f"Enter y-coordinate for vertex {label}: "))
  vertices.append([label, x_coord, y_coord])
  col_labels = ["Label", "X-coord", "Y-coord"]  # Set column labels

# Extract data for each row
data = [[vertex[1], vertex[2]] for vertex in vertices]

# Create a figure and hide axis elements
fig, ax = plt.subplots()
ax.axis('off')

# Create the table with custom cellText and colLabels
table = ax.table(cellText=data, colLabels=col_labels, loc='center')

# Customize table appearance (optional)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Display the plot
plt.title('vertex table')
plt.show()
