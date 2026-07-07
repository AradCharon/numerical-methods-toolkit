import subprocess
import os
import sys

def run_project(project_name, script_name):
    print(f"\n{'='*60}")
    print(f"Running {project_name}")
    print('='*60)
    
    project_path = os.path.join(project_name, "src", script_name)
    if os.path.exists(project_path):
        result = subprocess.run([sys.executable, project_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    else:
        print(f"❌ File {project_path} not found!")

if __name__ == "__main__":
    print("🚀 Starting Numerical Methods Projects")
    print("=" * 60)
    
    run_project("project1_Interpolation", "interpolation.py")
    run_project("project2_ExcelAnalysis", "excel_analysis.py")
    run_project("project3_Integral", "integral_calculation.py")
    
    print("\n✅ All projects completed successfully!")