
# WAP to implement DDA algorithm

import matplotlib.pyplot as plt
x1=int(input("Enter the x1 coordinates"))
y1=int(input("Enter the y1coordinates"))
x2=int(input("Enter the x2 coordinates"))
y2=int(input("Enter the y2 coordinates"))
#x1, x2 = map(int, input(" Enter x coordinates of a line :").split())
#y1, y2 = map(int, input("Enter y coordinates of a line ").split())
print(f"The x coordinates are{x1,x2} and y coordinates are{y1,y2}")

dx = x2 - x1
dy = y2 - y1

x = x1
y = y1
M = (y2 - y1) / (x2 - x1)


if abs(dx) > abs(dy) or M < 1:
    steps = abs(dx)
else:
    steps = abs(dy)


X_incr = dx / float(steps)
Y_incr = dy / float(steps)
xs = [x]
ys = [y]
print("Step\tX\tY\tRounded X\tRounded Y")
print("-" * 50)
for i in range(steps):
    if i < steps:
        x += X_incr
        y += Y_incr
        xs.append(x)
        ys.append(y)
        
        round_x = round(x)
        round_y = round(y)

        print(f"{i + 1}\t{x:.2f}\t{y:.2f}\t{round_x}\t\t{round_y}")
print("Asmita pokhrel")
plt.plot(xs, ys,'bo-')
plt.title("Asmita Pokhrel")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
