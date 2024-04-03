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

x=int(input("Enter the Seed coordinate for x:"))
y=int(input("Enter the Seed coordinate for y:"))
fill_color=str(input("Enter fill color  :"))
boundary_color=str(input("Enter  boundary color  :"))
color_name = webcolors.rgb_to_name(white_image[10,10])
plt.subplot(121)
plt.imshow(white_image,cmap='binary')
plt.title('Original Image')

boundary_fill(x,y,fill_color,boundary_color)
plt.subplot(122)
plt.imshow(white_image,cmap='binary')
plt.title('Filled Image')
plt.suptitle("Boundary Fill Algorithm, Bijay")
plt.show()