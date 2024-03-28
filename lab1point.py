
#LAB 01
# WAP that prompts the user to enter the co ordinates for points and then display them

import matplotlib.pyplot as plt
x1=int(input("Enter the x1 coordinates"))
y1=int(input("Enter the y1coordinates"))
x2=int(input("Enter the x2 coordinates"))
y2=int(input("Enter the y2 coordinates"))
print(f"Point 1 coordinates is :({x1},{y1})")
print(f"Point 1 coordinates is :({x2},{y2})")
plt.plot([x1,x2],[y1,y2],'-bo')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Asmita Pokhrel")
plt.grid(True)
plt.show()
