import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


# Input data
x_points = np.array([1, 2, 3, 4, 5, 6])
y_points = np.array([1, 3, 5, 8, 5, 2])

# Output directory
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "output"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def lagrange_interpolation(x_points, y_points, x):
    """
    Evaluate the Lagrange interpolation polynomial at x.
    """
    result = 0.0
    n = len(x_points)

    for i in range(n):
        basis = 1.0

        for j in range(n):
            if i != j:
                basis *= (
                    (x - x_points[j])
                    / (x_points[i] - x_points[j])
                )

        result += y_points[i] * basis

    return result


def main():
    print("=" * 60)
    print("Project 1: Interpolation using Lagrange and Spline Methods")
    print("=" * 60)

    # ---------------------------------------------------------
    # Lagrange interpolation
    # ---------------------------------------------------------
    print("\nLagrange Interpolation:")

    x_smooth = np.linspace(
        x_points.min(),
        x_points.max(),
        500
    )

    y_lagrange = np.array([
        lagrange_interpolation(x_points, y_points, x)
        for x in x_smooth
    ])

    # ---------------------------------------------------------
    # Cubic spline interpolation
    # ---------------------------------------------------------
    spline = CubicSpline(
        x_points,
        y_points,
        bc_type="natural"
    )

    y_spline = spline(x_smooth)

    print("\nNatural Cubic Spline:")

    for i in range(len(x_points) - 1):
        a = spline.c[3, i]
        b = spline.c[2, i]
        c = spline.c[1, i]
        d = spline.c[0, i]

        print(
            f"Interval [{x_points[i]}, {x_points[i + 1]}]:"
        )
        print(
            f"S(x) = {d:.4f}(x - {x_points[i]})^3 "
            f"+ {c:.4f}(x - {x_points[i]})^2 "
            f"+ {b:.4f}(x - {x_points[i]}) "
            f"+ {a:.4f}"
        )

    # ---------------------------------------------------------
    # Plot results
    # ---------------------------------------------------------
    plt.figure(figsize=(12, 7))

    plt.scatter(
        x_points,
        y_points,
        s=150,
        label="Data Points",
        zorder=5
    )

    plt.plot(
        x_smooth,
        y_lagrange,
        linewidth=2,
        label="Lagrange Interpolation"
    )

    plt.plot(
        x_smooth,
        y_spline,
        linestyle="--",
        linewidth=2,
        label="Natural Cubic Spline"
    )

    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.title(
        "Comparison of Lagrange and Spline Interpolation Methods",
        fontsize=14
    )

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # ---------------------------------------------------------
    # Save plot
    # ---------------------------------------------------------
    pdf_path = os.path.join(
        OUTPUT_DIR,
        "interpolation_plot.pdf"
    )

    png_path = os.path.join(
        OUTPUT_DIR,
        "interpolation_plot.png"
    )

    plt.savefig(
        pdf_path,
        format="pdf",
        bbox_inches="tight"
    )

    plt.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"\n[OK] PDF saved to {pdf_path}")
    print(f"[OK] PNG saved to {png_path}")

    # ---------------------------------------------------------
    # Save results
    # ---------------------------------------------------------
    results_path = os.path.join(
        OUTPUT_DIR,
        "interpolation_results.txt"
    )

    with open(results_path, "w", encoding="utf-8") as file:
        file.write("Interpolation Results\n")
        file.write("=" * 50 + "\n")

        file.write(
            f"Data Points: {list(zip(x_points, y_points))}\n"
        )

        file.write("\nNatural Cubic Spline:\n")

        for i in range(len(x_points) - 1):
            a = spline.c[3, i]
            b = spline.c[2, i]
            c = spline.c[1, i]
            d = spline.c[0, i]

            file.write(
                f"\nInterval [{x_points[i]}, {x_points[i + 1]}]:\n"
            )

            file.write(
                f"S(x) = {d:.6f}(x - {x_points[i]})^3 "
                f"+ {c:.6f}(x - {x_points[i]})^2 "
                f"+ {b:.6f}(x - {x_points[i]}) "
                f"+ {a:.6f}\n"
            )

    print(f"[OK] Results saved to {results_path}")


if __name__ == "__main__":
    main()