



#c) 2D scaling 

import matplotlib.pyplot as plt 

x1=int(input("Enter the first coordinate for x1:"))
y1=int(input("Enter the first coordinate for y1:"))
x2=int(input("Enter the second coordinate for x2:"))
y2=int(input("Enter the second coordinate for y2:"))
tx=int(input("Enter the scaling coordinate for tx : "))
ty=int(input("Enter the scaling coordinate for ty : "))

var1 = x1 * tx
var = y1 * ty

var2 = x2 * tx
var3 = y2 * ty

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot([x1, x2], [y1, y2], label='Original Line')
plt.plot([var1, var2], [var, var3], label='Translated Line')
plt.legend()
plt.title("Asmita Pokhrel")
plt.grid(True)
plt.show()
