# import matplotlib.pyplot as plt
# import numpy as np
# a=float(input("Enter first co-ordinate"))
# b=float(input("Emter second cordinate "))
# print(a,b)
# plt.plot(a, b,marker="o")
# plt.show() 

#lab2

# import matplotlib.pyplot as plt
# import numpy as np
# x1=int(input("Enter x1 co-ordinate: "))
# y1=int(input("Enter x1 co-ordinate: "))
# x2=int(input("Enter x2 co-ordinate: "))
# y2=int(input("Enter y2 co-ordinate: "))
# dx=x2-x1
# dy=y2-y1
# x=x1
# y=y1

# if abs(dx)>abs(dy):
#     steps=abs(dx)
# else:
#     steps=abs(dy)          

# xincr=dx/float(steps)
# yincr=dy/float(steps)

# x_s = []
# y_s = []
# print("Iteration\txk\tyk\t")
# for i in range(steps):
#     x1
#     y1
#     x=xincr+x
#     x_s.append(x)
#     y=yincr+y
#     y_s.append(y)
    
#     print(x1,y1)

# print("Bijay Sah Rauniyar")

# plt.plot(x_s, y_s)
# #print(x_s, y_s)
# plt.show()


#lab 3

import matplotlib.pyplot as plt
import numpy as np
x1=int(input("enter x1  coordinate"))
y1=int(input("enter 11  coordinate"))
x2=int(input("enter x2  coordinate"))
y2=int(input("enter y2  coordinate"))
x_cordinate=[x1]
y_cordinate=[y1]
dx=abs(x2-x1)
dy=abs(y2-y1)
pk=2+dy-dx
print("i    | pk   |pk+1 | xk+1|yk+1  |plot")
print("     |      |     | %d  |  %d  | (%d,%d)"%(x1,y1,x1,y1))
for i in range(dx):
    if pk<0:
        pkn=pk+(2*dy)
        x1+=1
        print(" %d  |  %d  | %d  | %d  |  %d  | (%d,%d)"%(i,pk,pkn,x1,y1,x1,y1))
        pk=pkn
    else:
        pkn=pk+(2+dy+2*dx)
        x1+=1
        y1+=1
        print("%d   |  %d  | %d  | %d  |  %d  | (%d,%d)"%(i,pk,pkn,x1,y1,x1,y1))
        pk=pkn
    x_cordinate.append(x1)
    y_cordinate.append(y1)
    #To plot a straight line on a graph
    x=(x_cordinate[0],x_cordinate[-1])
    y=(y_cordinate[0],y_cordinate[-1])
plt.title("Bresenham Line Algorithm")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.plot(x,y)
plt.scatter(x_cordinate,y_cordinate,color="BLACK",s=25)
plt.show()


#import matplotlib.pyplot as plt
