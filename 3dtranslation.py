#3D translation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from copy import deepcopy
def translate_3d(tx,ty,tz,ax,vertices):
    # for x axis rotation
    for i in range(len(vertices)):
        vertices[i][0]+=tx
        vertices[i][1]+=ty
        vertices[i][2]+=tz
    plot_object(vertices,ax,'green',"After Translation")

# Function to plot a cube
def plot_object(vertices,ax,color,title):
    # Define the six faces of the cube using the vertices
    cube_size=12
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='k', alpha=.35,label=title))  
    # Set axis labels
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    ax.set_xlim([-cube_size, cube_size])
    ax.set_ylim([-2, cube_size])
    ax.set_zlim([-2, cube_size])
    ax.legend()

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1, projection='3d')





# Define the eight vertices of the rectangle
# if you want to change the value [x,y,z] the first four and last four has same z 
# ie 6,4 and first four x,y coordinates are same as last four x,y coordinates 
vertices = [
        [-1, 4, 4],
        [5, 4, 4],
        [5, 0, 4],
        [-1, 0, 4],
        [-1, 4, 2],
        [5, 4, 2],
        [5, 0, 2], 
        [-1, 0, 2]
    ]
tx=int(input("Enter the translating factor tx :"))
ty=int(input("Enter the translating factor  ty and  :"))
tz=int(input("Enter the translating factor tz :"))
# Plot the cube
plot_object(vertices,ax,'blue',"Before Scaling")
t_list=deepcopy(vertices)
translate_3d(tx,ty,tz,ax,t_list)
print("Before translation\tAfter Translation")
for i in range(len(vertices)):
    print(vertices[i],"\t\t",t_list[i])
plt.suptitle("3D Translation")
print("Bijay Sah Rauniyar")
plt.show()
