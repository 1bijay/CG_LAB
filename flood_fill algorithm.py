#flood fill algorithm
import numpy as np
import matplotlib.pyplot as plt
import webcolors
import os
print(os.getcwd())
white_image = np.full((40, 40,3), 255, dtype=np.uint8)
def floodfill_Algo(x,y,old_color,new_color):
    global white_image
    value=webcolors.rgb_to_name(white_image[y,x])
    if(value==old_color):
        white_image[y,x]=webcolors.name_to_rgb(new_color)
        floodfill_Algo(x-1,y,old_color,new_color)
        floodfill_Algo(x+1,y,old_color,new_color)
        floodfill_Algo(x,y-1,old_color,new_color)
        floodfill_Algo(x,y+1,old_color,new_color)

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

x=int(input("Enter the Seed coordinate for x :"))
y=int(input("Enter the Seed coordinate for y :"))
fill_color=str(input("Enter fill color :"))
original_color=str(input("Enter  background color :"))
plt.subplot(121)
plt.imshow(white_image,cmap='binary')
plt.title('Original Image')

floodfill_Algo(x,y,fill_color,original_color)
plt.subplot(122)
plt.imshow(white_image,cmap='binary')
plt.title('Filled Image')
plt.suptitle("Floodfill Algorithm")
plt.show()

