import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(p0, p1, p2, p3, num_points=100):
    t = np.linspace(0, 1, num_points)
    x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
    return x, y

def main():
    # Define control points
    p0 = (0, 0)
    p1 = (50, 100)
    p2 = (100, 100)
    p3 = (150, 0)

    x, y = cubic_bezier(p0, p1, p2, p3)

    plt.plot(x, y, label='Cubic Bezier Curve', color='blue')
    plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], color='red', label='Control Points')
    plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], linestyle='--', color='gray')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cubic Bezier Curve, Bijay Sah Rauniyar')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
