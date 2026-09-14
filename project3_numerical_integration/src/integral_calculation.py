import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre


# Output directory
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "output"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def func(x):
    """Function to be integrated: f(x) = e^(x^2)."""
    return np.exp(x**2)


def trapezoidal_rule(f, a, b, n):
    """Approximate an integral using the trapezoidal rule."""
    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (
        h
        * (
            y[0]
            + y[-1]
            + 2 * np.sum(y[1:-1])
        )
        / 2
    )

    return integral


def simpson_rule(f, a, b, n):
    """Approximate an integral using Simpson's 1/3 rule."""
    if n % 2 != 0:
        n += 1

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (
        h
        / 3
        * (
            y[0]
            + y[-1]
            + 4 * np.sum(y[1:-1:2])
            + 2 * np.sum(y[2:-1:2])
        )
    )

    return integral


def gaussian_quadrature(f, a, b, n):
    """Approximate an integral using Gauss-Legendre quadrature."""
    nodes, weights = roots_legendre(n)

    # Transform nodes from [-1, 1] to [a, b]
    transformed_nodes = (
        0.5 * (b - a) * nodes
        + 0.5 * (a + b)
    )

    integral = (
        0.5
        * (b - a)
        * np.sum(
            weights * f(transformed_nodes)
        )
    )

    return integral


def save_plot(fig):
    """Save the figure as PNG and PDF."""
    pdf_path = os.path.join(
        OUTPUT_DIR,
        "integral_comparison.pdf"
    )

    png_path = os.path.join(
        OUTPUT_DIR,
        "integral_comparison.png"
    )

    fig.savefig(
        pdf_path,
        format="pdf",
        bbox_inches="tight"
    )

    fig.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"\n[OK] PDF saved to {pdf_path}")
    print(f"[OK] PNG saved to {png_path}")


def save_results(
    exact_integral,
    trapezoidal_results,
    simpson_results,
    gaussian_results
):
    """Save numerical integration results to a text file."""
    results_path = os.path.join(
        OUTPUT_DIR,
        "integral_results.txt"
    )

    trapezoidal_result = trapezoidal_results[-1]
    simpson_result = simpson_results[-1]
    gaussian_result = gaussian_results[-1]

    trapezoidal_error = abs(
        trapezoidal_result - exact_integral
    )

    simpson_error = abs(
        simpson_result - exact_integral
    )

    gaussian_error = abs(
        gaussian_result - exact_integral
    )

    with open(
        results_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Integral Results for ∫₀¹ e^(x²) dx\n"
        )
        file.write("=" * 60 + "\n\n")

        file.write(
            f"Reference value: "
            f"{exact_integral:.15f}\n\n"
        )

        file.write(
            "Trapezoidal Rule (n=1024)\n"
        )
        file.write(
            f"Result: {trapezoidal_result:.15f}\n"
        )
        file.write(
            f"Absolute Error: "
            f"{trapezoidal_error:.15e}\n\n"
        )

        file.write(
            "Simpson Rule (n=1024)\n"
        )
        file.write(
            f"Result: {simpson_result:.15f}\n"
        )
        file.write(
            f"Absolute Error: "
            f"{simpson_error:.15e}\n\n"
        )

        file.write(
            "Gaussian Quadrature (n=10)\n"
        )
        file.write(
            f"Result: {gaussian_result:.15f}\n"
        )
        file.write(
            f"Absolute Error: "
            f"{gaussian_error:.15e}\n"
        )

    print(f"[OK] Results saved to {results_path}")


def main():
    print("=" * 60)
    print("Project 3: Numerical Integration Methods")
    print("=" * 60)

    # Integration interval
    a, b = 0, 1

    # ---------------------------------------------------------
    # Trapezoidal and Simpson rules
    # ---------------------------------------------------------
    n_values = [
        2, 4, 8, 16, 32,
        64, 128, 256, 512, 1024
    ]

    trapezoidal_results = []
    simpson_results = []

    print(
        "\nCalculating integral using "
        "Trapezoidal and Simpson rules:"
    )

    print("-" * 60)
    print(
        f"{'n':<8}"
        f"{'Trapezoidal':<15}"
        f"{'Simpson':<15}"
        f"{'Difference':<15}"
    )
    print("-" * 60)

    for n in n_values:
        trapezoidal_result = trapezoidal_rule(
            func,
            a,
            b,
            n
        )

        simpson_result = simpson_rule(
            func,
            a,
            b,
            n
        )

        trapezoidal_results.append(
            trapezoidal_result
        )

        simpson_results.append(
            simpson_result
        )

        difference = abs(
            trapezoidal_result - simpson_result
        )

        print(
            f"{n:<8}"
            f"{trapezoidal_result:<15.10f}"
            f"{simpson_result:<15.10f}"
            f"{difference:<15.10e}"
        )

    # ---------------------------------------------------------
    # Reference value
    # ---------------------------------------------------------
    exact_integral, _ = quad(
        func,
        a,
        b
    )

    print(
        f"\nReference integral value: "
        f"{exact_integral:.15f}"
    )

    # ---------------------------------------------------------
    # Gaussian quadrature
    # ---------------------------------------------------------
    print("\n" + "=" * 60)
    print("Calculating integral using Gaussian Quadrature:")
    print("-" * 60)

    print(
        f"{'Points':<12}"
        f"{'Result':<20}"
        f"{'Error':<20}"
    )

    print("-" * 60)

    n_gauss_values = [
        2, 3, 4, 5, 6, 8, 10
    ]

    gaussian_results = []

    for n in n_gauss_values:
        gaussian_result = gaussian_quadrature(
            func,
            a,
            b,
            n
        )

        error = abs(
            gaussian_result - exact_integral
        )

        gaussian_results.append(
            gaussian_result
        )

        print(
            f"{n:<12}"
            f"{gaussian_result:<20.15f}"
            f"{error:<20.15e}"
        )

    # ---------------------------------------------------------
    # Calculate errors
    # ---------------------------------------------------------
    trapezoidal_errors = [
        abs(result - exact_integral)
        for result in trapezoidal_results
    ]

    simpson_errors = [
        abs(result - exact_integral)
        for result in simpson_results
    ]

    gaussian_errors = [
        abs(result - exact_integral)
        for result in gaussian_results
    ]

    # ---------------------------------------------------------
    # Plot convergence
    # ---------------------------------------------------------
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(12, 5)
    )

    # Trapezoidal and Simpson
    axes[0].semilogy(
        n_values,
        trapezoidal_errors,
        "o-",
        label="Trapezoidal",
        linewidth=2
    )

    axes[0].semilogy(
        n_values,
        simpson_errors,
        "s-",
        label="Simpson",
        linewidth=2
    )

    axes[0].set_xlabel(
        "Number of subintervals (n)"
    )

    axes[0].set_ylabel(
        "Absolute Error"
    )

    axes[0].set_title(
        "Convergence of Trapezoidal and Simpson Methods"
    )

    axes[0].legend()
    axes[0].grid(
        True,
        alpha=0.3
    )

    # Gaussian quadrature
    axes[1].semilogy(
        n_gauss_values,
        gaussian_errors,
        "d-",
        label="Gaussian",
        linewidth=2
    )

    axes[1].set_xlabel(
        "Number of Gaussian Points"
    )

    axes[1].set_ylabel(
        "Absolute Error"
    )

    axes[1].set_title(
        "Convergence of Gaussian Quadrature"
    )

    axes[1].legend()
    axes[1].grid(
        True,
        alpha=0.3
    )

    fig.tight_layout()

    save_plot(fig)

    # ---------------------------------------------------------
    # Save numerical results
    # ---------------------------------------------------------
    save_results(
        exact_integral,
        trapezoidal_results,
        simpson_results,
        gaussian_results
    )


if __name__ == "__main__":
    main()