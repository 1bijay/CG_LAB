# Mid point circle drawing algorithm
import os
print(os.getcwd())
import matplotlib.pyplot as plt
r=float(input("Enter the radius = "))
x_center=float(input("Enter the x_center of circle= "))
y_center=float(input("Enter the y_center of circle= "))
def symmetry(x,y,x_center,y_center):
    plt.plot(x+x_center,y+y_center,marker=".",color='blue')
    plt.plot(-x+x_center,y+y_center,marker=".",color='blue')
    plt.plot(x+x_center,-y+y_center,marker=".",color='blue')
    plt.plot(-x+x_center,-y+y_center,marker=".",color='blue')
    plt.plot(y+x_center,x+y_center,marker=".",color='blue')
    plt.plot(-y+x_center,x+y_center,marker=".",color='blue')
    plt.plot(y+x_center,-x+y_center,marker=".",color='blue')
    plt.plot(-y+x_center,-x+y_center,marker=".",color='blue')
def display(k,p,x,y,x_center,y_center):
    x=round(x)
    y=round(y)
    print(f"{k}\t{p}\t{(x,y)}\t\t",end="")
    print(f"{(x+x_center,y+y_center)}\t",end="")
    print(f"{(-x+x_center,y+y_center)}\t",end="")
    print(f"{(x+x_center,-y+y_center)}\t",end="")
    print(f"{(-x+x_center,-y+y_center)}\t",end="")
    print(f"{(y+x_center,x+y_center)}\t",end="")
    print(f"{(-y+x_center,x+y_center)}\t",end="")
    print(f"{(y+x_center,-x+y_center)}\t",end="")
    print(f"{(-y+x_center,-x+y_center)}\t")
x=0
y=r
p=5/4-r
k=0
print("k\tpk\t(x+1,y+1)\t(x,y)\t\t(-x,y)\t\t(x,-y)\t\t(-x,-y)\t\t(y,x)\t\t(-y,x)\t\t(y,-x)\t\t(-y,-x)")
symmetry(x,y,x_center,y_center)
display(k,p,x,y,x_center,y_center)
while x<y:
    x+=1
    k+=1
    if p<0:
        p=p+2*x+1
    else:
        p=p+2*(x-y)+1
        y-=1
    symmetry(x,y,x_center,y_center)
    display(k,p,x,y,x_center,y_center)
plt.title("Mid point circle drawing algorithm")
plt.plot(x_center,y_center,color='red',marker=".")
plt.text(x_center,y_center,"("+str(x_center)+" , "+str(y_center)+")",fontsize=8)
plt.show();
print("Bijay Sah Rauniyar")
