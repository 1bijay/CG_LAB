#2D reflection
import matplotlib.pyplot as plt
from copy import deepcopy
def reflection_x(object):
    for i in range(len(object)):
        object[i][1]*=(-1)
    x, y = zip(*object)
    plt.plot(x + (x[0],), y + (y[0],), color='black')
    plt.fill(x,y,color='green',label="Reflection along x-axis")
def reflection_y(shape):
    for i in range(len(shape)):
        shape[i][0]*=(-1)
    x, y = zip(*shape)
    plt.plot(x + (x[0],), y + (y[0],), color='black')
    plt.fill(x,y,color='red',label="Reflection along y-axis")
def reflection_origin(shape):
    for i in range(len(shape)):
        shape[i][0]*=(-1)
        shape[i][1]*=(-1)
    x, y = zip(*shape)
    plt.plot(x + (x[0],), y + (y[0],), color='black')
    plt.fill(x,y,color='black',label="Reflection along Origin")
polygon=[[1,2],[3,2],[3,4]]
copy_tempx=deepcopy(polygon)
copy_tempy=deepcopy(polygon)
copy_origin=deepcopy(polygon)
x, y = zip(*polygon)
plt.plot(x + (x[0],), y + (y[0],), color='black')
plt.fill(x,y,color='blue',label="Original Polygon")
reflection_x(copy_tempx)
reflection_y(copy_tempy)
reflection_origin(copy_origin)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend()
plt.title("Reflection Bijay Sah Rauniyar")
plt.show()
'''

'''
#Boundary Fill algorithm
import numpy as np
import matplotlib.pyplot as plt
import webcolors
import os
print(os.getcwd())
white_image = np.full((40, 40, 3), 255, dtype=np.uint8) 
def boundary_fill(x,y,fill,boundary):
    global white_image
    value=webcolors.rgb_to_name(white_image[y,x])
    if(value!=fill and value != boundary):
        white_image[y,x]=webcolors.name_to_rgb(fill)
        boundary_fill(x-1,y,fill,boundary)
        boundary_fill(x+1,y,fill,boundary)
        boundary_fill(x,y-1,fill,boundary)
        boundary_fill(x,y+1,fill,boundary)

pixel_x, pixel_y = 10, 10

# Define line segments and offsets for each segment
segments = [
    ((1, 0), (-1, 0)),  # Right, then left
    ((0, -1), (0, 1)),  # Down, then up
    ((-1, 0), (1, 0)),  # Left, then right
    ((0, 1), (0, -1)),  # Up, then down
]

# Loop through each segment and modify pixels
for dx, dy in segments:
    for _ in range(15):
        white_image[pixel_y, pixel_x] = [0, 0, 0]
        pixel_x += dx[0]  
        pixel_y += dy[1] 

x,y=map(int,input("Enter the Seed coordinate:").split())
fill_color,boundary_color=map(str,input("Enter fill color and boundary color respectively :").split())
color_name = webcolors.rgb_to_name(white_image[10,10])
plt.subplot(121)
plt.imshow(white_image,cmap='binary')
plt.title('Original Image')

boundary_fill(x,y,fill_color,boundary_color)
plt.subplot(122)
plt.imshow(white_image,cmap='binary')
plt.title('Filled Image')
plt.suptitle("Boundary Fill Algorithm")
plt.show()
