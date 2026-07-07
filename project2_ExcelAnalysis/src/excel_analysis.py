import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

base_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(base_dir, 'data')
output_dir = os.path.join(base_dir, 'output')

os.makedirs(data_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

FILE_PATH = os.path.join(data_dir, 'project3.xlsx')

def read_and_process_data(file_path):
    try:
        df = pd.read_excel(file_path, header=0)
        df.columns = df.columns.str.strip()
        
        for col in df.columns:
            if col != 'Run time for different data size':
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        print("Data loaded successfully:")
        print(df)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def plot_bar_chart(df, filename='bar_chart.png'):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    data_sizes = df['Run time for different data size'].astype(str)
    x = np.arange(len(data_sizes))
    width = 0.25
    
    bars1 = ax.bar(x - width, df['Alg.1'], width, label='Algorithm 1', color='#FF6B6B', alpha=0.8)
    bars2 = ax.bar(x, df['Alg.2'], width, label='Algorithm 2', color='#4ECDC4', alpha=0.8)
    bars3 = ax.bar(x + width, df['Alg.3'], width, label='Algorithm 3', color='#45B7D1', alpha=0.8)
    
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.0f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Data Size (KB)', fontsize=12)
    ax.set_ylabel('Run Time (seconds)', fontsize=12)
    ax.set_title('Comparison of Algorithm Run Times', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(data_sizes)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save as PDF
    pdf_path = os.path.join(output_dir, filename.replace('.png', '.pdf'))
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"Bar chart PDF saved to {pdf_path}")
    
    # Save as PNG
    png_path = os.path.join(output_dir, filename)
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"Bar chart PNG saved to {png_path}")
    
    plt.show()

def plot_line_chart(df, filename='line_chart.png'):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Run time for different data size'], df['Alg.1'], 
            'o-', label='Algorithm 1', color='#FF6B6B', linewidth=2, markersize=8)
    ax.plot(df['Run time for different data size'], df['Alg.2'], 
            's-', label='Algorithm 2', color='#4ECDC4', linewidth=2, markersize=8)
    ax.plot(df['Run time for different data size'], df['Alg.3'], 
            '^-', label='Algorithm 3', color='#45B7D1', linewidth=2, markersize=8)
    
    ax.set_xlabel('Data Size (KB)', fontsize=12)
    ax.set_ylabel('Run Time (seconds)', fontsize=12)
    ax.set_title('Run Time Trends by Data Size', fontsize=14)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save as PDF
    pdf_path = os.path.join(output_dir, filename.replace('.png', '.pdf'))
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"Line chart PDF saved to {pdf_path}")
    
    # Save as PNG
    png_path = os.path.join(output_dir, filename)
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"Line chart PNG saved to {png_path}")
    
    plt.show()

def plot_box_plot(df, filename='box_plot.png'):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    data = [df['Alg.1'].values, df['Alg.2'].values, df['Alg.3'].values]
    labels = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    box = ax.boxplot(data, labels=labels, patch_artist=True,
                     medianprops={'color': 'black', 'linewidth': 2})
    
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Run Time (seconds)', fontsize=12)
    ax.set_title('Distribution of Algorithm Run Times', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save as PDF
    pdf_path = os.path.join(output_dir, filename.replace('.png', '.pdf'))
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"Box plot PDF saved to {pdf_path}")
    
    # Save as PNG
    png_path = os.path.join(output_dir, filename)
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"Box plot PNG saved to {png_path}")
    
    plt.show()

def add_new_data(file_path):
    new_data = {
        'Run time for different data size': [700],
        'Alg.1': [700],
        'Alg.2': [320],
        'Alg.3': [80]
    }
    
    df = pd.read_excel(file_path, header=0)
    df.columns = df.columns.str.strip()
    
    new_df = pd.DataFrame(new_data)
    updated_df = pd.concat([df, new_df], ignore_index=True)
    updated_df.to_excel(file_path, index=False)
    
    print("\nNew data added successfully:")
    print(updated_df)
    return updated_df

def main():
    print("=" * 60)
    print("Project 2: Excel File Analysis and Visualization")
    print("=" * 60)
    
    if not os.path.exists(FILE_PATH):
        print(f"File {FILE_PATH} not found!")
        print("Please place 'project3.xlsx' in the 'data' folder.")
        return
    
    df = read_and_process_data(FILE_PATH)
    if df is None:
        return
    
    plot_bar_chart(df)
    plot_line_chart(df)
    plot_box_plot(df)
    
    alg2_mean = df['Alg.2'].mean()
    print(f"\nMean runtime for Algorithm 2: {alg2_mean:.2f} seconds")
    
    print("\n" + "=" * 60)
    print("Adding new data to Excel file...")
    updated_df = add_new_data(FILE_PATH)
    
    print("\nRe-plotting charts with updated data...")
    plot_bar_chart(updated_df, 'bar_chart_updated.png')
    plot_line_chart(updated_df, 'line_chart_updated.png')
    plot_box_plot(updated_df, 'box_plot_updated.png')

    stats_path = os.path.join(output_dir, 'analysis_stats.txt')
    with open(stats_path, 'w', encoding='utf-8') as f:
        f.write("Data Analysis Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"\nMean runtime for Algorithm 2: {alg2_mean:.2f} seconds\n")
    
    print(f"\nAnalysis completed! Results saved to {output_dir}")

if __name__ == "__main__":
    main()