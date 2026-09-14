import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ---------------------------------------------------------
# Plot settings
# ---------------------------------------------------------

plt.rcParams["font.size"] = 10
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.3


# ---------------------------------------------------------
# Directory and file paths
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

FILE_PATH = os.path.join(
    DATA_DIR,
    "algorithm_runtime_data.xlsx"
)

DATA_SIZE_COLUMN = "Run time for different data size"
ALGORITHM_COLUMNS = ["Alg.1", "Alg.2", "Alg.3"]


# ---------------------------------------------------------
# Data loading and validation
# ---------------------------------------------------------

def read_and_process_data(file_path):
    """Read, clean, and validate the Excel dataset."""

    try:
        df = pd.read_excel(file_path, header=0)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    except Exception as error:
        print(f"Error reading Excel file: {error}")
        return None

    # Clean column names
    df.columns = df.columns.astype(str).str.strip()

    # Check required columns
    required_columns = [
        DATA_SIZE_COLUMN,
        *ALGORITHM_COLUMNS
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print(
            "Missing required columns:"
            f" {missing_columns}"
        )
        return None

    # Clean data-size column
    df[DATA_SIZE_COLUMN] = (
        df[DATA_SIZE_COLUMN]
        .astype(str)
        .str.strip()
    )

    # Convert algorithm run times to numeric values
    for column in ALGORITHM_COLUMNS:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove completely invalid rows
    df = df.dropna(
        subset=ALGORITHM_COLUMNS
    ).reset_index(drop=True)

    print("\nData loaded successfully:")
    print(df.to_string(index=False))

    return df


# ---------------------------------------------------------
# Plot utilities
# ---------------------------------------------------------

def save_plot(fig, filename):
    """Save a figure as PNG and PDF."""

    png_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

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

    print(f"PNG saved to: {png_path}")
    print(f"PDF saved to: {pdf_path}")

    plt.close(fig)


# ---------------------------------------------------------
# Bar chart
# ---------------------------------------------------------

def plot_bar_chart(
    df,
    filename="bar_chart.png"
):
    """Create a grouped bar chart of algorithm run times."""

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    data_sizes = df[DATA_SIZE_COLUMN].astype(str)
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

    # Add values above bars
    for bars in (
        bars1,
        bars2,
        bars3
    ):
        for bar in bars:

            height = bar.get_height()

            ax.annotate(
                f"{height:.0f}",
                xy=(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height
                ),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9
            )

    ax.set_xlabel(
        "Data Size (KB)",
        fontsize=12
    )

    ax.set_ylabel(
        "Run Time (seconds)",
        fontsize=12
    )

    ax.set_title(
        "Comparison of Algorithm Run Times",
        fontsize=14
    )

    ax.set_xticks(x)
    ax.set_xticklabels(data_sizes)

    ax.legend(
        loc="upper left"
    )

    fig.tight_layout()

    save_plot(
        fig,
        filename
    )


# ---------------------------------------------------------
# Line chart
# ---------------------------------------------------------

def plot_line_chart(
    df,
    filename="line_chart.png"
):
    """Create a line chart showing run-time trends."""

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    data_sizes = df[DATA_SIZE_COLUMN].astype(str)

    ax.plot(
        data_sizes,
        df["Alg.1"],
        "o-",
        label="Algorithm 1",
        linewidth=2,
        markersize=7
    )

    ax.plot(
        data_sizes,
        df["Alg.2"],
        "s-",
        label="Algorithm 2",
        linewidth=2,
        markersize=7
    )

    ax.plot(
        data_sizes,
        df["Alg.3"],
        "^-",
        label="Algorithm 3",
        linewidth=2,
        markersize=7
    )

    ax.set_xlabel(
        "Data Size (KB)",
        fontsize=12
    )

    ax.set_ylabel(
        "Run Time (seconds)",
        fontsize=12
    )

    ax.set_title(
        "Run Time Trends by Data Size",
        fontsize=14
    )

    ax.legend(
        loc="upper left"
    )

    fig.tight_layout()

    save_plot(
        fig,
        filename
    )


# ---------------------------------------------------------
# Box plot
# ---------------------------------------------------------

def plot_box_plot(
    df,
    filename="box_plot.png"
):
    """Create a box plot comparing algorithm run-time distributions."""

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

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
        tick_labels=labels,
        patch_artist=True,
        medianprops={
            "color": "black",
            "linewidth": 2
        }
    )

    for patch in box["boxes"]:
        patch.set_alpha(0.7)

    ax.set_ylabel(
        "Run Time (seconds)",
        fontsize=12
    )

    ax.set_title(
        "Distribution of Algorithm Run Times",
        fontsize=14
    )

    fig.tight_layout()

    save_plot(
        fig,
        filename
    )


# ---------------------------------------------------------
# Add new data
# ---------------------------------------------------------

def add_new_data(file_path):
    """
    Add the required 700KB data point if it does not
    already exist in the Excel file.
    """

    df = pd.read_excel(
        file_path,
        header=0
    )

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Normalize data-size values
    df[DATA_SIZE_COLUMN] = (
        df[DATA_SIZE_COLUMN]
        .astype(str)
        .str.strip()
    )

    # Check whether 700KB already exists
    if "700KB" in df[DATA_SIZE_COLUMN].values:

        print(
            "\n700KB data already exists."
        )

        return df

    # Required assignment data
    new_data = pd.DataFrame({
        DATA_SIZE_COLUMN: ["700KB"],
        "Alg.1": [80],
        "Alg.2": [320],
        "Alg.3": [700]
    })

    updated_df = pd.concat(
        [
            df,
            new_data
        ],
        ignore_index=True
    )

    updated_df.to_excel(
        file_path,
        index=False
    )

    print(
        "\n700KB data added successfully:"
    )

    print(
        updated_df.to_string(
            index=False
        )
    )

    return updated_df


# ---------------------------------------------------------
# Algorithm 2 statistics
# ---------------------------------------------------------

def calculate_algorithm_2_mean(df):
    """
    Calculate the mean runtime of Algorithm 2
    for input sizes from 100KB to 600KB.
    """

    data_sizes = (
        df[DATA_SIZE_COLUMN]
        .astype(str)
        .str.extract(r"(\d+)")
        [0]
        .astype(float)
    )

    original_data = df[
        data_sizes.between(100, 600)
    ]

    if original_data.empty:
        print(
            "No data found for 100KB-600KB."
        )
        return np.nan

    return original_data["Alg.2"].mean()


# ---------------------------------------------------------
# Save statistical results
# ---------------------------------------------------------

def save_statistics(
    df,
    alg2_mean,
    filename="analysis_stats.txt"
):
    """Save basic statistical results to a text file."""

    stats_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(
        stats_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Algorithm Runtime Analysis\n"
        )

        file.write(
            "=" * 50 + "\n"
        )

        file.write(
            "\nDataset:\n"
        )

        file.write(
            df.to_string(index=False)
        )

        file.write(
            "\n\n"
        )

        file.write(
            "Algorithm 2 Mean Runtime "
            "(100KB-600KB): "
            f"{alg2_mean:.2f} seconds\n"
        )

        file.write(
            "\nSummary Statistics:\n"
        )

        file.write(
            df[ALGORITHM_COLUMNS]
            .describe()
            .to_string()
        )

    print(
        f"\nStatistics saved to: {stats_path}"
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 60)
    print(
        "Project 2: Excel File Analysis "
        "and Visualization"
    )
    print("=" * 60)

    # -----------------------------------------------------
    # Check Excel file
    # -----------------------------------------------------

    if not os.path.exists(FILE_PATH):

        print(
            f"\nFile not found: {FILE_PATH}"
        )

        print(
            "\nPlease place "
            "'algorithm_runtime_data.xlsx' "
            "in the 'data' folder."
        )

        return

    # -----------------------------------------------------
    # Read initial data
    # -----------------------------------------------------

    df = read_and_process_data(
        FILE_PATH
    )

    if df is None:
        return

    # -----------------------------------------------------
    # Create initial charts
    # -----------------------------------------------------

    print(
        "\nCreating charts for "
        "original dataset..."
    )

    plot_bar_chart(
        df,
        "bar_chart.png"
    )

    plot_line_chart(
        df,
        "line_chart.png"
    )

    plot_box_plot(
        df,
        "box_plot.png"
    )

    # -----------------------------------------------------
    # Calculate Algorithm 2 mean
    # -----------------------------------------------------

    alg2_mean = calculate_algorithm_2_mean(
        df
    )

    print(
        "\nMean runtime for Algorithm 2 "
        "(100KB-600KB): "
        f"{alg2_mean:.2f} seconds"
    )

    # -----------------------------------------------------
    # Add 700KB data
    # -----------------------------------------------------

    print(
        "\n" + "=" * 60
    )

    print(
        "Adding required 700KB data..."
    )

    updated_df = add_new_data(
        FILE_PATH
    )

    # -----------------------------------------------------
    # Create updated charts
    # -----------------------------------------------------

    print(
        "\nCreating charts for "
        "updated dataset..."
    )

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

    # -----------------------------------------------------
    # Save statistics
    # -----------------------------------------------------

    save_statistics(
        updated_df,
        alg2_mean
    )

    print(
        "\n" + "=" * 60
    )

    print(
        "Project 2 completed successfully."
    )


if __name__ == "__main__":
    main()