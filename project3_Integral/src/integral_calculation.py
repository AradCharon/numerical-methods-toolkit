import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
os.makedirs(output_dir, exist_ok=True)

def func(x):
    return np.exp(x**2)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h * (y[0] + y[-1] + 2 * sum(y[1:-1])) / 2
    return integral

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h/3 * (y[0] + y[-1] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-1:2]))
    return integral

def gaussian_quadrature(f, a, b, n):
    x_nodes, weights = roots_legendre(n)
    t = 0.5 * (b - a) * x_nodes + 0.5 * (a + b)
    integral = 0.5 * (b - a) * np.sum(weights * f(t))
    return integral

def main():
    print("=" * 60)
    print("Project 3: Numerical Integration Methods")
    print("=" * 60)
    
    a, b = 0, 1
    
    n_values = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    trapezoidal_results = []
    simpson_results = []
    
    print("\nCalculating integral using Trapezoidal and Simpson rules:")
    print("-" * 60)
    print(f"{'n':<8} {'Trapezoidal':<15} {'Simpson':<15} {'Difference':<15}")
    print("-" * 60)
    
    for n in n_values:
        trap = trapezoidal_rule(func, a, b, n)
        simp = simpson_rule(func, a, b, n)
        trapezoidal_results.append(trap)
        simpson_results.append(simp)
        print(f"{n:<8} {trap:<15.10f} {simp:<15.10f} {abs(trap-simp):<15.10e}")
    
    exact_integral, error_est = quad(func, a, b)
    print(f"\nExact integral value: {exact_integral:.15f}")
    
    print("\n" + "=" * 60)
    print("Calculating integral using Gaussian Quadrature:")
    print("-" * 60)
    print(f"{'Points':<12} {'Result':<20} {'Error':<20}")
    print("-" * 60)
    
    n_gauss_values = [2, 3, 4, 5, 6, 8, 10]
    gaussian_results = []
    
    for n in n_gauss_values:
        gauss = gaussian_quadrature(func, a, b, n)
        error = abs(gauss - exact_integral)
        gaussian_results.append(gauss)
        print(f"{n:<12} {gauss:<20.15f} {error:<20.15e}")
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.semilogy(n_values, [abs(t - exact_integral) for t in trapezoidal_results], 
                 'o-', label='Trapezoidal', linewidth=2)
    plt.semilogy(n_values, [abs(s - exact_integral) for s in simpson_results], 
                 's-', label='Simpson', linewidth=2)
    plt.xlabel('Number of subintervals (n)')
    plt.ylabel('Absolute Error')
    plt.title('Convergence of Trapezoidal and Simpson Methods')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(n_gauss_values, [abs(g - exact_integral) for g in gaussian_results], 
             'd-', label='Gaussian', color='red', linewidth=2)
    plt.xlabel('Number of Gaussian Points')
    plt.ylabel('Absolute Error')
    plt.title('Convergence of Gaussian Quadrature')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save as PDF
    pdf_path = os.path.join(output_dir, 'integral_comparison.pdf')
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"\n[OK] PDF saved to {pdf_path}")
    
    # Save as PNG
    png_path = os.path.join(output_dir, 'integral_comparison.png')
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"[OK] PNG saved to {png_path}")
    
    plt.show()
    
    results_path = os.path.join(output_dir, 'integral_results.txt')
    with open(results_path, 'w', encoding='utf-8') as f:
        f.write("Integral Results for ∫₀¹ e^(x²) dx\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Exact value: {exact_integral:.15f}\n\n")
        f.write(f"Trapezoidal Rule (n=1024): {trapezoidal_results[-1]:.15f}\n")
        f.write(f"Error: {abs(trapezoidal_results[-1] - exact_integral):.15e}\n\n")
        f.write(f"Simpson Rule (n=1024): {simpson_results[-1]:.15f}\n")
        f.write(f"Error: {abs(simpson_results[-1] - exact_integral):.15e}\n\n")
        f.write(f"Gaussian Quadrature (n=10): {gaussian_results[-1]:.15f}\n")
        f.write(f"Error: {abs(gaussian_results[-1] - exact_integral):.15e}\n")
    
    print(f"[OK] Results saved to {results_path}")

if __name__ == "__main__":
    main()