# 🧮 Numerical Methods Toolkit

<p align="center">
  <a href="https://github.com/AradCharon/numerical-methods-toolkit">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  </a>
  <a href="https://matplotlib.org/">
    <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
  </a>
  <a href="https://scipy.org/">
    <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy">
  </a>
  <a href="https://openpyxl.readthedocs.io/">
    <img src="https://img.shields.io/badge/OpenPyXL-2F6B3F?style=for-the-badge&logo=python&logoColor=white" alt="OpenPyXL">
  </a>
</p>

A modular Python implementation of fundamental numerical methods covering interpolation, algorithm runtime analysis, and numerical integration.

This project was developed as the **final project for the Mathematical Software course during my 4th semester at Amirkabir University of Technology**.

The toolkit combines mathematical formulations with computational implementations, numerical analysis, data processing, visualization, and reproducible experimentation. Each project is implemented as an independent module with dedicated source code, input data, generated outputs, and numerical results.

---

# 📖 Overview

The **Numerical Methods Toolkit** consists of three computational projects covering different areas of numerical analysis and scientific computing.

The project includes:

* Polynomial and spline interpolation
* Excel-based algorithm runtime analysis
* Numerical integration
* Convergence analysis
* Error analysis
* Data visualization
* Scientific Python programming
* Automated numerical result generation

The implementations are designed to connect mathematical concepts with practical computational workflows while maintaining a modular project structure.

---

# ✨ Features

* 🧮 Lagrange polynomial interpolation
* 📈 Natural cubic spline interpolation
* 📊 Algorithm runtime analysis
* 📑 Excel data processing
* 📉 Statistical visualization
* ∫ Numerical integration
* 🔢 Composite Trapezoidal Rule
* 📐 Composite Simpson's Rule
* 🎯 Gaussian Quadrature
* 📊 Convergence and error analysis
* 🧩 Modular Python architecture
* 📁 Structured input and output directories
* 📝 Automatically generated numerical results
* 📄 LaTeX-based technical report
* 📚 Reproducible computational workflow

---

# 🧠 Numerical Methods

The project implements several classical numerical methods and computational techniques.

## Interpolation

The interpolation module implements two different approaches for constructing approximations through a given set of data points:

* **Lagrange Polynomial Interpolation**
* **Natural Cubic Spline Interpolation**

The Lagrange interpolating polynomial is defined as:

$$
P(x)=\sum_{i=0}^{n} y_i L_i(x)
$$

where:

$$
L_i(x)=\prod_{\substack{j=0\\j\neq i}}^{n}
\frac{x-x_j}{x_i-x_j}
$$

The project also constructs a Natural Cubic Spline using piecewise cubic polynomials with continuity conditions on the function and its first two derivatives, together with natural boundary conditions.

---

## Numerical Integration

The numerical integration module evaluates:

$$
\int_0^1 e^{x^2}\,dx
$$

using three numerical approaches:

* **Composite Trapezoidal Rule**
* **Composite Simpson's Rule**
* **Gaussian Quadrature**

The Composite Trapezoidal Rule is given by:

$$
T_n =
\frac{h}{2}
\left[
f(x_0)+2\sum_{i=1}^{n-1}f(x_i)+f(x_n)
\right]
$$

The Composite Simpson's Rule is given by:

$$
S_n =
\frac{h}{3}
\left[
f(x_0)
+4\sum_{\text{odd }i}f(x_i)
+2\sum_{\text{even }i}f(x_i)
+f(x_n)
\right]
$$

Gaussian Quadrature evaluates the integral using weighted function evaluations at selected quadrature points.

---

# 📊 Algorithm Runtime Analysis

The second project analyzes the runtime behavior of three algorithms using experimental data stored in an Excel spreadsheet.

The original dataset contains runtime measurements for input sizes ranging from **100 KB to 600 KB**.

The implementation automatically adds the following data point when it is not already present:

```text
700KB | 80 | 320 | 700
```

The analysis generates multiple visualizations and statistical outputs, including:

* Bar charts
* Line charts
* Box plots
* Descriptive statistics
* Updated visualizations after extending the dataset

For the original dataset, the mean runtime of **Algorithm 2** is:

```text
250.00 seconds
```

The project uses Pandas and OpenPyXL to process the Excel data and Matplotlib to generate the visualizations.

---

# 📂 Project Structure

```text
numerical-methods-toolkit/
│
├── project1_interpolation/
│   ├── output/
│   │   ├── interpolation_plot.pdf
│   │   ├── interpolation_plot.png
│   │   └── interpolation_results.txt
│   │
│   └── src/
│       └── interpolation.py
│
├── project2_excel_analysis/
│   ├── data/
│   │   └── algorithm_runtime_data.xlsx
│   │
│   ├── output/
│   │   ├── analysis_stats.txt
│   │   ├── bar_chart.pdf
│   │   ├── bar_chart.png
│   │   ├── bar_chart_updated.pdf
│   │   ├── bar_chart_updated.png
│   │   ├── box_plot.pdf
│   │   ├── box_plot.png
│   │   ├── box_plot_updated.pdf
│   │   ├── box_plot_updated.png
│   │   ├── line_chart.pdf
│   │   ├── line_chart.png
│   │   ├── line_chart_updated.pdf
│   │   └── line_chart_updated.png
│   │
│   └── src/
│       └── excel_analysis.py
│
├── project3_numerical_integration/
│   ├── output/
│   │   ├── integral_comparison.pdf
│   │   ├── integral_comparison.png
│   │   └── integral_results.txt
│   │
│   └── src/
│       └── integral_calculation.py
│
├── report/
│   ├── aut_logo.png
│   ├── references.bib
│   ├── report.pdf
│   └── report.tex
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

The project is divided into three independent computational modules.

Each module contains its own implementation and generated outputs, while the root-level `main.py` provides the main entry point for the complete toolkit.

---

## project1_interpolation

The interpolation module processes a predefined set of data points and constructs both a Lagrange polynomial and a Natural Cubic Spline.

### Responsibilities

* Define interpolation data points
* Construct the Lagrange polynomial
* Construct the Natural Cubic Spline
* Calculate spline coefficients
* Generate interpolation visualizations
* Save numerical results

The generated output includes the interpolation plot and a text file containing the numerical interpolation results and spline equations.

---

## project2_excel_analysis

The Excel analysis module processes algorithm runtime data stored in:

```text
project2_excel_analysis/data/algorithm_runtime_data.xlsx
```

### Responsibilities

* Load Excel data
* Validate and process the dataset
* Calculate descriptive statistics
* Add the required 700 KB data point
* Generate bar charts
* Generate line charts
* Generate box plots
* Save statistical results

The module generates both original and updated visualizations.

---

## project3_numerical_integration

The numerical integration module evaluates:

$$
\int_0^1 e^{x^2}\,dx
$$

using multiple numerical integration methods.

### Responsibilities

* Apply the Composite Trapezoidal Rule
* Apply the Composite Simpson's Rule
* Apply Gaussian Quadrature
* Evaluate convergence
* Calculate numerical errors
* Compare integration methods
* Generate comparison plots
* Save numerical results

---

# 📈 Results

## Interpolation

The interpolation module produces a comparison between the Lagrange polynomial and Natural Cubic Spline.

The resulting visualization demonstrates the difference between a single global polynomial approximation and a piecewise cubic interpolation.

---

## Algorithm Runtime Analysis

The runtime analysis module generates six main visualization categories:

* Original bar chart
* Updated bar chart
* Original line chart
* Updated line chart
* Original box plot
* Updated box plot

The analysis also stores descriptive statistics in:

```text
project2_excel_analysis/output/analysis_stats.txt
```

---

## Numerical Integration

The high-accuracy numerical reference used for the integration analysis is approximately:

```text
1.462651745907181
```

The numerical experiments show the convergence behavior of the Trapezoidal and Simpson rules as the number of subintervals increases.

Gaussian Quadrature achieves very high accuracy with a relatively small number of quadrature points.

The complete numerical results are stored in:

```text
project3_numerical_integration/output/integral_results.txt
```

---

# 📄 Technical Report

A detailed technical report accompanies the implementation.

The report documents:

* Mathematical formulations
* Numerical methods
* Algorithmic procedures
* Experimental results
* Convergence analysis
* Error analysis
* Data visualizations
* Implementation details
* Conclusions

<p align="center">
  <a href="report/report.pdf">
    <img src="https://img.shields.io/badge/📄%20Read%20Full%20Report-005571?style=for-the-badge" alt="Full Technical Report">
  </a>
</p>

---

# 🛠️ Technologies Used

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  </a>
  <a href="https://matplotlib.org/">
    <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
  </a>
  <a href="https://scipy.org/">
    <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy">
  </a>
  <a href="https://openpyxl.readthedocs.io/">
    <img src="https://img.shields.io/badge/OpenPyXL-2F6B3F?style=for-the-badge&logo=python&logoColor=white" alt="OpenPyXL">
  </a>
  <a href="https://www.latex-project.org/">
    <img src="https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX">
  </a>
</p>

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AradCharon/numerical-methods-toolkit.git
```

Move into the project directory:

```bash
cd numerical-methods-toolkit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

Run the main entry point:

```bash
python main.py
```

Individual modules can also be executed directly from their respective source directories.

For example:

```bash
python project1_interpolation/src/interpolation.py
```

```bash
python project2_excel_analysis/src/excel_analysis.py
```

```bash
python project3_numerical_integration/src/integral_calculation.py
```

Generated numerical results and visualizations are stored in each project's `output/` directory.

---

# 🔬 Reproducibility

The project is structured so that the computational experiments can be reproduced from the source code and provided input data.

Dependencies are specified in:

```text
requirements.txt
```

The generated numerical outputs and visualizations are stored alongside their corresponding projects.

The technical report provides the mathematical formulations and experimental analysis required to interpret the results.

---

# 🎯 Project Scope

The toolkit covers three complementary aspects of numerical and scientific computing:

* **Interpolation** — approximation of discrete data using polynomial and spline methods
* **Data Analysis** — processing and visualization of algorithm runtime measurements
* **Numerical Integration** — approximation, convergence, and error analysis of definite integrals

Together, these components provide a computational implementation of several fundamental numerical methods while maintaining a modular and reproducible software structure.

---

# 👨‍💻 Author

**Arad Shafiee**

Mathematics & Applications Student
Computer Science Minor
Amirkabir University of Technology

Interested in:

* Artificial Intelligence
* Data Analysis
* Machine Learning
* Data Mining
* Algorithms

<p align="center">
  <a href="https://github.com/AradCharon">
    <img src="https://img.shields.io/badge/GitHub-AradCharon-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

---

# ⭐ Repository

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
