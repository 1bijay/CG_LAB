import matplotlib.pyplot as plt

# Predefined vertex data (modify as needed)
vertices = ["A", "B", "C", "D"]

# Predefined edge data (modify as needed)
# Each sub-list represents an edge (start vertex, end vertex)
edges = [["A", "B"], ["B", "C"], ["C", "D"], ["A", "C"]]

# Create column labels
col_labels = ["Start Vertex", "End Vertex"]

# Create the table data
data = [[edge[0], edge[1]] for edge in edges]

# Create a figure and hide axis elements
fig, ax = plt.subplots()
ax.axis('off')

# Create the table
table = ax.table(cellText=data, colLabels=col_labels, loc='center')

# Customize table appearance (optional)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Display the plot
plt.show()
