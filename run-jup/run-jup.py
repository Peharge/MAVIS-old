import subprocess
import sys
import os
import shutil

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

def start_jupyter():
    try:
        print("\nJupyter Information:")
        print("------------------")
        # Ask for confirmation before execution
        user_input = input(f"Do you want to start Jupyter? (y/n): ").strip().lower()
        if user_input != 'y':
            print(f"{green}Jupyter will not be started.{reset}")
            sys.exit(0)

        # Dynamically determine the username and create the path to the virtual environment
        user_home = os.path.expanduser("~")  # User's home directory
        venv_python = os.path.join(user_home, "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

        # Check if the virtual environment Python exists
        if not os.path.isfile(venv_python):
            print(f"{red}Error: The virtual environment {venv_python} does not exist.{reset}")
            sys.exit(1)

        # Check if Jupyter is installed in the virtual environment using pip
        try:
            subprocess.run([venv_python, "-m", "pip", "show", "jupyter"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(f"{red}Error: Jupyter is not installed in the virtual environment.{reset}")
            sys.exit(1)

        # Target folder for Jupyter Notebooks
        jupyter_directory = os.path.join(user_home, "PycharmProjects", "MAVIS", "jupyter")
        if not os.path.isdir(jupyter_directory):
            print(f"{red}Error: The specified directory '{jupyter_directory}' does not exist.{reset}")
            sys.exit(1)

        # Start Jupyter with the Python interpreter from the virtual environment
        subprocess.run([
            venv_python,
            '-m', 'notebook',
            '--NotebookApp.ip=0.0.0.0',
            '--NotebookApp.port=8888',
            f'--NotebookApp.notebook_dir={jupyter_directory}'
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f"{red}Error starting Jupyter Notebook: {e}{reset}")
        sys.exit(1)
    except Exception as e:
        print(f"{red}Unexpected error: {e}{reset}")
        sys.exit(1)


if __name__ == "__main__":
    start_jupyter()
    print(f"\nFlask Information:")
    print(f"------------------")
