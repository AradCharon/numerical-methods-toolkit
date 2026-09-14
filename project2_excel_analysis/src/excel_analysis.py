import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Plot settings
plt.rcParams["font.size"] = 10
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.3


# Directory paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

FILE_PATH = os.path.join(DATA_DIR, "project3.xlsx")


def read_and_process_data(file_path):
    """Read and clean the Excel dataset."""
    try:
        df = pd.read_excel(file_path, header=0)
        df.columns = df.columns.str.strip()

        for column in df.columns:
            if column != "Run time for different data size":
                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )

        print("Data loaded successfully:")
        print(df)

        return df

    except Exception as error:
        print(f"Error reading file: {error}")
        return None


def save_plot(fig, filename):
    """Save a figure as both PNG and PDF."""
    png_path = os.path.join(OUTPUT_DIR, filename)
    pdf_path = os.path.join(
        OUTPUT_DIR,
        filename.replace(".png", ".pdf")
    )

    fig.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight"
    )

    fig.savefig(
        pdf_path,
        format="pdf",
        bbox_inches="tight"
    )

    print(f"PNG saved to {png_path}")
    print(f"PDF saved to {pdf_path}")

    plt.close(fig)


def plot_bar_chart(df, filename="bar_chart.png"):
    """Create a grouped bar chart of algorithm run times."""
    fig, ax = plt.subplots(figsize=(12, 6))

    data_sizes = df["Run time for different data size"].astype(str)
    x = np.arange(len(data_sizes))
    width = 0.25

    bars1 = ax.bar(
        x - width,
        df["Alg.1"],
        width,
        label="Algorithm 1"
    )

    bars2 = ax.bar(
        x,
        df["Alg.2"],
        width,
        label="Algorithm 2"
    )

    bars3 = ax.bar(
        x + width,
        df["Alg.3"],
        width,
        label="Algorithm 3"
    )

    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()

            ax.annotate(
                f"{height:.0f}",
                xy=(
                    bar.get_x() + bar.get_width() / 2,
                    height
                ),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9
            )

    ax.set_xlabel("Data Size (KB)", fontsize=12)
    ax.set_ylabel("Run Time (seconds)", fontsize=12)
    ax.set_title(
        "Comparison of Algorithm Run Times",
        fontsize=14
    )

    ax.set_xticks(x)
    ax.set_xticklabels(data_sizes)
    ax.legend(loc="upper left")

    fig.tight_layout()
    save_plot(fig, filename)


def plot_line_chart(df, filename="line_chart.png"):
    """Create a line chart showing run-time trends."""
    fig, ax = plt.subplots(figsize=(12, 6))

    data_sizes = df["Run time for different data size"]

    ax.plot(
        data_sizes,
        df["Alg.1"],
        "o-",
        label="Algorithm 1",
        linewidth=2,
        markersize=8
    )

    ax.plot(
        data_sizes,
        df["Alg.2"],
        "s-",
        label="Algorithm 2",
        linewidth=2,
        markersize=8
    )

    ax.plot(
        data_sizes,
        df["Alg.3"],
        "^-",
        label="Algorithm 3",
        linewidth=2,
        markersize=8
    )

    ax.set_xlabel("Data Size (KB)", fontsize=12)
    ax.set_ylabel("Run Time (seconds)", fontsize=12)
    ax.set_title(
        "Run Time Trends by Data Size",
        fontsize=14
    )

    ax.legend(loc="upper left")

    fig.tight_layout()
    save_plot(fig, filename)


def plot_box_plot(df, filename="box_plot.png"):
    """Create a box plot comparing algorithm run-time distributions."""
    fig, ax = plt.subplots(figsize=(10, 6))

    data = [
        df["Alg.1"].dropna().values,
        df["Alg.2"].dropna().values,
        df["Alg.3"].dropna().values
    ]

    labels = [
        "Algorithm 1",
        "Algorithm 2",
        "Algorithm 3"
    ]

    box = ax.boxplot(
        data,
        labels=labels,
        patch_artist=True,
        medianprops={
            "color": "black",
            "linewidth": 2
        }
    )

    for patch in box["boxes"]:
        patch.set_alpha(0.7)

    ax.set_ylabel("Run Time (seconds)", fontsize=12)
    ax.set_title(
        "Distribution of Algorithm Run Times",
        fontsize=14
    )

    fig.tight_layout()
    save_plot(fig, filename)


def add_new_data(file_path):
    """Add the required 700 KB data point to the Excel file."""
    new_data = {
        "Run time for different data size": [700],
        "Alg.1": [80],
        "Alg.2": [320],
        "Alg.3": [700]
    }

    df = pd.read_excel(file_path, header=0)
    df.columns = df.columns.str.strip()

    new_df = pd.DataFrame(new_data)

    updated_df = pd.concat(
        [df, new_df],
        ignore_index=True
    )

    updated_df.to_excel(
        file_path,
        index=False
    )

    print("\nNew data added successfully:")
    print(updated_df)

    return updated_df


def main():
    print("=" * 60)
    print("Project 2: Excel File Analysis and Visualization")
    print("=" * 60)

    # Check whether the Excel file exists
    if not os.path.exists(FILE_PATH):
        print(f"File not found: {FILE_PATH}")
        print(
            "Please place 'project3.xlsx' "
            "in the 'data' folder."
        )
        return

    # Read and process data
    df = read_and_process_data(FILE_PATH)

    if df is None:
        return

    # Create initial charts
    plot_bar_chart(df)
    plot_line_chart(df)
    plot_box_plot(df)

    # Calculate Algorithm 2 mean
    alg2_mean = df["Alg.2"].mean()

    print(
        f"\nMean runtime for Algorithm 2: "
        f"{alg2_mean:.2f} seconds"
    )

    # Add the new 700 KB data point
    print("\n" + "=" * 60)
    print("Adding new data to Excel file...")
    
    updated_df = add_new_data(FILE_PATH)

    # Re-create charts using updated data
    print("\nRe-plotting charts with updated data...")

    plot_bar_chart(
        updated_df,
        "bar_chart_updated.png"
    )

    plot_line_chart(
        updated_df,
        "line_chart_updated.png"
    )

    plot_box_plot(
        updated_df,
        "box_plot_updated.png"
    )

    # Save statistical results
    stats_path = os.path.join(
        OUTPUT_DIR,
        "analysis_stats.txt"
    )

    with open(
        stats_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("Data Analysis Results\n")
        file.write("=" * 50 + "\n")
        file.write(
            f"\nMean runtime for Algorithm 2: "
            f"{alg2_mean:.2f} seconds\n"
        )

    print(
        f"\nAnalysis completed! "
        f"Results saved to {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()