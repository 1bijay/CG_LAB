#3d reflection 
import os
print(os.getcwd())
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from copy import deepcopy
def rotate(index,vertices,ax,color,title):
    for i in range(len(vertices)):
        vertices[i][index]*=(-1)
    plot_object(vertices,ax,color,title)
    return vertices
def plot_object(vertices,ax,color,title):
    # Define the six faces of the cube using the vertices
    cube_size=10
    
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='k', alpha=.25,label=title))  
    # Set axis labels
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    ax.set_xlim([-cube_size, cube_size])
    ax.set_ylim([-cube_size, cube_size])
    ax.set_zlim([-cube_size, cube_size])
    ax.legend()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(2,2,1, projection='3d')
ax1=fig.add_subplot(2,2,2, projection='3d')
ax2=fig.add_subplot(2,2,3, projection='3d')
ax3=fig.add_subplot(2,2,4, projection='3d')
vertices = [
        [5, 6, 9],
        [5, 6, 9],
        [5, 6, 9],
        [5, 6, 9],
        [3, 8, 2],
        [7, 8, 2],
        [7, 4, 2], 
        [3, 4, 2]
    ]
plot_object(vertices,ax,'blue',"Before Rotation")
xyplane=rotate(index=2,vertices=deepcopy(vertices),ax=ax1,color='green',title="Reflection through xy plane")
yzplane=rotate(index=0,vertices=deepcopy(vertices),ax=ax2,color='red',title="Reflection through yz plane")
xzplane=rotate(index=1,vertices=deepcopy(vertices),ax=ax3,color='orange',title="Reflection through xz plane")
print("Points\t\txy-plane\tyz-plane\txz-plane")
for i in range(len(vertices)):
    print(f"{vertices[i]}\t{xyplane[i]}\t{yzplane[i]}\t{xzplane[i]}")
plt.suptitle("3D Reflection")
plt.show()

