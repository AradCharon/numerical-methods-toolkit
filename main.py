import os
import subprocess
import sys


def run_project(project_name, script_name):
    print(f"\n{'=' * 60}")
    print(f"Running {project_name}")
    print("=" * 60)

    project_path = os.path.join(
        project_name,
        "src",
        script_name
    )

    if not os.path.exists(project_path):
        print(f"File not found: {project_path}")
        return False

    result = subprocess.run(
        [sys.executable, project_path],
        text=True
    )

    if result.returncode != 0:
        print(
            f"\n{project_name} failed "
            f"with exit code {result.returncode}."
        )
        return False

    return True


def main():
    print("Starting Numerical Methods Projects")
    print("=" * 60)

    projects = [
        (
            "project1_interpolation",
            "interpolation.py"
        ),
        (
            "project2_excel_analysis",
            "excel_analysis.py"
        ),
        (
            "project3_numerical_integration",
            "integral_calculation.py"
        )
    ]

    all_successful = True

    for project_name, script_name in projects:
        success = run_project(
            project_name,
            script_name
        )

        if not success:
            all_successful = False

    print("\n" + "=" * 60)

    if all_successful:
        print("All projects completed successfully!")
    else:
        print("Some projects failed.")


if __name__ == "__main__":
    main()