
# mid point ellipse algorithm
import os
print(os.getcwd())
import matplotlib.pyplot as plt
rx=float(input("Enter the radius rx:  >>"))
ry=float(input("Enter the radius ry: >> "))
x_center=float(input("Enter the x_center co-ordinate: >> "))
y_center=float(input("Enter the y_center co-ordinate: >> "))
# function for plotting points
def plotPoints(x,y,x_center,y_center):
    plt.plot(x+x_center,y+y_center,marker=".",color='blue')
    plt.plot(-x+x_center,y+y_center,marker=".",color='blue')
    plt.plot(x+x_center,-y+y_center,marker=".",color='blue')
    plt.plot(-x+x_center,-y+y_center,marker=".",color='blue')
def display(k,p,x,y,x_center,y_center):
    x=round(x)
    y=round(y)
    print(f"{k}\t{p}\t{(x,y)}\t\t",end="")
    print(f"{(x+x_center,y+y_center)}\t",end="")
    print(f"{(-x+x_center,y+y_center)}\t",end="")
    print(f"{(x+x_center,-y+y_center)}\t",end="")
    print(f"{(-x+x_center,-y+y_center)}\t")
# initial decision parameter for region one
p1=(ry*ry)-(rx*rx*ry)+(rx*rx*0.25)
# assigning value of x and y
x,y,k=0,ry,0

print("k\tp1\t(x+1,y+1)\t(x,y)\t\t(-x,y)\t\t(x,-y)\t\t(-x,-y)")
plotPoints(x,y,x_center,y_center)
display(k,p1,x,y,x_center,y_center)
while ((2*ry*ry*x)<(2*rx*rx*y)):
    k+=1
    x+=1
    if p1<0:
        p1=p1+(2*ry*ry*x)+(ry*ry)
    else:
        y-=1
        p1=p1+(2*ry*ry*x)-(2*rx*rx*y)+(ry*ry)
    plotPoints(x,y,x_center,y_center)
    display(k,p1,x,y,x_center,y_center)
# initial decision parameter for region two
p2=(ry*ry*(x+0.5)*(x+0.5))+(rx*rx*(y-1)*(y-1))-(rx*rx*ry*ry)
print("\n_____________________________________________________________________________________________________________\n")
print("k\tp2\t(x+1,y+1)\t(x,y)\t\t(-x,y)\t\t(x,-y)\t\t(-x,-y)")
k=0
while (y>0):
    y-=1
    if p2>0:
        p2=p2-(2*rx*rx*(y))+(rx*rx)
    else:
        x+=1
        p2=p2+(2*ry*ry*(x))-(2*rx*rx*(y))+(rx*rx)
    plotPoints(x,y,x_center,y_center)
    display(k,p2,x,y,x_center,y_center)
    k+=1
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Mid-point Ellipse Darwing Algorithm")
plt.plot(x_center,y_center,marker="o")
plt.show()
print("Bijay Sah Rauniyar")









