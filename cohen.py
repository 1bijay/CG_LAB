import matplotlib.pyplot as plt

# Define region codes for Cohen-Sutherland algorithm
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Define window coordinates
x_min, y_min = 50, 50
x_max, y_max = 150, 150

# Function to compute region code for a point
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Function to clip the line segment using Cohen-Sutherland algorithm
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)
    
    if accept:
        plt.plot([x1, x2], [y1, y2], 'b-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Cohen-Sutherland Line Clipping')
        plt.grid(True)
        plt.xlim(0, 200)
        plt.ylim(0, 200)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
    else:
        print("Line is completely outside and rejected")

# Take user input for line segment coordinates
def get_user_input():
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))
    return x1, y1, x2, y2

# Test the algorithm with user input
def main():
    print("Enter coordinates for the line segment:")
    x1, y1, x2, y2 = get_user_input()
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'r--')
    plt.plot([x1, x2], [y1, y2], 'g-')
    cohen_sutherland(x1, y1, x2, y2)
    print("Bijay Sah Rauniyar")

if __name__ == "__main__":
    main()
