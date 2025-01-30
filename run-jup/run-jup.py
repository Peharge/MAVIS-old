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
        # Vor der Ausführung um Bestätigung bitten
        user_input = input(f"Do you want to start Jupyter in Black Mode? (y/n): ").strip().lower()
        if user_input != 'y':
            print(f"{green}Jupyter will not be started.{reset}")
            sys.exit(0)

        # Benutzernamen dynamisch ermitteln und Pfad zur virtuellen Umgebung erstellen
        user_home = os.path.expanduser("~")  # User's home directory
        venv_python = os.path.join(user_home, "PycharmProjects", "MAVIS", ".env", "Scripts", "python.exe")

        # Überprüfen Sie, ob die virtuelle Umgebung Python vorhanden ist
        if not os.path.isfile(venv_python):
            print(f"{red}Error: The virtual environment {venv_python} does not exist.{reset}")
            sys.exit(1)

        # Überprüfen Sie mit pip, ob Jupyter in der virtuellen Umgebung installiert ist
        try:
            subprocess.run([venv_python, "-m", "pip", "show", "jupyter"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(f"{red}Error: Jupyter is not installed in the virtual environment.{reset}")
            sys.exit(1)

        # Zielordner für Jupyter Notebooks
        jupyter_directory = os.path.join(user_home, "PycharmProjects", "MAVIS", "jupyter")
        if not os.path.isdir(jupyter_directory):
            print(f"{red}Error: The specified directory '{jupyter_directory}' does not exist.{reset}")
            sys.exit(1)

        # Richten Sie Jupyter mithilfe einer Konfigurationsdatei so ein, dass es im Dunkelmodus startet.
        # Sie können dazu das Paket „jupyterthemes“ installieren und verwenden.
        # Wenn es nicht installiert ist, installieren Sie es über „pip install jupyterthemes“.

        # Optional: Wenden Sie das Dark Mode-Design mit jupyterthemes an
        try:
            subprocess.run([venv_python, "-m", "pip", "install", "jupyterthemes"], check=True)
            subprocess.run([venv_python, "-m", "jt", "-t", "monokai"], check=True)  # Das Monokai-Thema ist ein beliebtes dunkles Thema
        except subprocess.CalledProcessError:
            print(f"{yellow}Warning: Could not apply the Jupyter dark theme. Proceeding without it.{reset}")

        # Starten Sie Jupyter mit dem Python-Interpreter aus der virtuellen Umgebung
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
