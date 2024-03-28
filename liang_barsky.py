import matplotlib.pyplot as plt

# Define region codes for Liang-Barsky algorithm
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Define window coordinates
x_min, y_min = 50, 50
x_max, y_max = 150, 150

# Function to clip the line segment using Liang-Barsky algorithm
def liang_barsky(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    u1, u2 = 0, 1

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return  # Line is parallel and outside the clipping window, discard it
        if p[i] != 0:
            r = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, r)
            else:
                u2 = min(u2, r)
    
    if u1 > u2:
        return  # Line is completely outside the clipping window, discard it
    
    x1_clip = x1 + u1 * dx
    y1_clip = y1 + u1 * dy
    x2_clip = x1 + u2 * dx
    y2_clip = y1 + u2 * dy

    plt.plot([x1_clip, x2_clip], [y1_clip, y2_clip], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Liang-Barsky Line Clipping, Bijay')
    plt.grid(True)
    plt.xlim(0, 200)
    plt.ylim(0, 200)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Define the line segment
def main():
    x1, y1 = 20, 120
    x2, y2 = 180, 50
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'r--')
    plt.plot([x1, x2], [y1, y2], 'g-')
    liang_barsky(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
