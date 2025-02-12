import subprocess
import sys
import os

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
        print("--------------------")
        user_input = input("Do you want to start Jupyter? [y/n]:").strip().lower()
        if user_input not in ['y', 'yes']:
            print(f"{green}Jupyter will not be started.{reset}")
            sys.exit(0)

        user_home = os.path.expanduser("~")
        venv_python = os.path.join(user_home, "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

        if not os.path.isfile(venv_python):
            print(f"{red}Error{reset}: The virtual environment {venv_python} does not exist.")
            sys.exit(1)

        try:
            subprocess.run([venv_python, "-m", "pip", "show", "jupyter"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(f"{red}Error: Jupyter is not installed in the virtual environment.{reset}")
            sys.exit(1)

        jupyter_directory = os.path.join(user_home, "PycharmProjects", "MAVIS", "jupyter")
        if not os.path.isdir(jupyter_directory):
            print(f"{red}Error: The specified directory '{jupyter_directory}' does not exist.{reset}")
            sys.exit(1)

        # Start Jupyter Notebook
        jupyter_command = [
            venv_python,
            "-m", "notebook",
            "--NotebookApp.ip=0.0.0.0",
            "--NotebookApp.port=8888",
            f"--NotebookApp.notebook_dir={jupyter_directory}",
            "--NotebookApp.disable_check_xsrf=True",
            "--NotebookApp.allow_origin='*'",
            "--NotebookApp.allow_root=True",
            "--NotebookApp.token=",  # Kein Token
            "--NotebookApp.password=",  # Kein Passwort
            "--no-browser",
            "--NotebookApp.tornado_settings={\"headers\": {\"Content-Security-Policy\": \"frame-ancestors *\"}}",
            "--NotebookApp.log_level=DEBUG"
        ]

        # Start Jupyter-Server
        process = subprocess.Popen(jupyter_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{green}Jupyter Notebook is running.{reset}")
        print(f"Access it via: {cyan}http://localhost:8888{reset}")

        # Warte auf den Prozess, um Fehler abzufangen
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"{yellow}Jupyter Notebook stopped with errors:{reset}\n{stderr.decode()}")
        else:
            print(f"{green}Jupyter Notebook closed successfully.{reset}")

    except subprocess.CalledProcessError as e:
        print(f"{red}Error starting Jupyter Notebook{reset}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"{red}Unexpected error{reset}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_jupyter()
    print("\nFlask Information:")
    print("------------------")
