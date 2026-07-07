import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, lagrange
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
os.makedirs(output_dir, exist_ok=True)

x_points = np.array([1, 2, 3, 4, 5, 6])
y_points = np.array([1, 3, 5, 8, 5, 2])

def lagrange_poly(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * L_i
    return result

def main():
    print("=" * 60)
    print("Project 1: Interpolation using Lagrange and Spline Methods")
    print("=" * 60)
    
    poly_lagrange = lagrange(x_points, y_points)
    print("\nLagrange Polynomial:")
    print(f"P(x) = {poly_lagrange}")
    
    cs = CubicSpline(x_points, y_points, bc_type='natural')
    print("\nNatural Cubic Spline:")
    for i in range(len(x_points)-1):
        a = cs.c[3, i]
        b = cs.c[2, i]
        c = cs.c[1, i]
        d = cs.c[0, i]
        print(f"Interval [{x_points[i]}, {x_points[i+1]}]: ")
        print(f"S(x) = {a:.4f}(x-{x_points[i]})^3 + {b:.4f}(x-{x_points[i]})^2 + {c:.4f}(x-{x_points[i]}) + {d:.4f}")
    
    x_smooth = np.linspace(1, 6, 500)
    y_lagrange = [lagrange_poly(x_points, y_points, x) for x in x_smooth]
    y_spline = cs(x_smooth)
    
    plt.figure(figsize=(12, 7))
    plt.scatter(x_points, y_points, color='red', s=150, label='Data Points', zorder=5)
    plt.plot(x_smooth, y_lagrange, 'b-', linewidth=2, label='Lagrange Interpolation')
    plt.plot(x_smooth, y_spline, 'g--', linewidth=2, label='Natural Cubic Spline')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Comparison of Lagrange and Spline Interpolation Methods', fontsize=14)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    
    # Save as PDF
    pdf_path = os.path.join(output_dir, 'interpolation_plot.pdf')
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"\n[OK] PDF saved to {pdf_path}")
    
    # Save as PNG (keep both formats)
    png_path = os.path.join(output_dir, 'interpolation_plot.png')
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"[OK] PNG saved to {png_path}")
    
    plt.show()
    
    results_path = os.path.join(output_dir, 'interpolation_results.txt')
    with open(results_path, 'w', encoding='utf-8') as f:
        f.write("Interpolation Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"Data Points: {list(zip(x_points, y_points))}\n")
        f.write(f"\nLagrange Polynomial: {poly_lagrange}\n")
    
    print(f"[OK] Results saved to {results_path}")

if __name__ == "__main__":
    main()