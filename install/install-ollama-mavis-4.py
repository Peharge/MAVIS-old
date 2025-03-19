import os
import platform
import subprocess
import time
import json

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

def check_ollama_update():
    """
    Prüft, ob eine neue Version von Ollama verfügbar ist, und bietet ein Update an.
    """
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            local_version = result.stdout.strip()
            remote_version = subprocess.run(["curl", "-s", "https://api.ollama.ai/version"],
                                            stdout=subprocess.PIPE, text=True).stdout.strip()

            if local_version != remote_version:
                print(f"{yellow}New Ollama version available: {remote_version} (Current: {local_version}){reset}")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"{green}Ollama updated successfully! Please restart the script.{reset}")
                        exit()
                    elif user_input in ["n", "no"]:
                        print("Skipping update.")
                        break
                    else:
                        print(f"{red}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")

def find_ollama_path():
    """
    Findet den Installationspfad von Ollama basierend auf dem Betriebssystem.
    """
    try:
        if platform.system() == "Windows":
            base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
            return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
        elif platform.system() == "Darwin":  # macOS
            return "/Applications/Ollama.app/Contents/MacOS/Ollama"
        else:
            raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"Error finding Ollama path: {e}")

def start_ollama():
    """
    Startet Ollama, falls es noch nicht läuft.
    """
    try:
        # Überprüfen, ob Ollama bereits läuft
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")

def check_command_installed(command):
    """
    Überprüft, ob ein Befehlszeilentool installiert ist (z. B. ollama).
    :param command: Zu prüfender Befehlsname.
    :return: True, wenn installiert, andernfalls False.
    """
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}: {e}{reset}")
        return False

def check_model_with_ollama(model_name):
    """
    Überprüft, ob ein bestimmtes Modell in ollama verfügbar ist.
    :param model_name: Der Name des zu prüfenden Modells.
    :return: True, wenn verfügbar, andernfalls False.
    """
    try:
        result = subprocess.run(
            ["ollama", "show", model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",  # Sicherstellen, dass UTF-8 für die Ausgabe verwendet wird
            errors="replace"  # Ersetzt ungültige Zeichen, anstatt eine Exception auszulösen
        )

        if result.returncode == 0:
            print(f"Model information for {blue}{model_name}{reset}:\n"
                  f"--------------------------------------\n{result.stdout}\n")
            return True
        else:
            print(f"{yellow}Model {model_name} is not available{reset}:\n"
                  f"-----------------------------------\n{result.stderr}\n")
            return False

    except Exception as e:
        print(f"{red}Error checking model {model_name} with ollama{reset}:\n"
              f"-----------------------------------\n{e}\n")
        return False

def install_model_with_ollama(model_name):
    """
    Installiert ein Modell mit ollama, sofern verfügbar.
    :param model_name: Der Name des zu installierenden Modells.
    """
    try:
        print(f"{blue}Attempting to install model {model_name} with ollama...{reset}")
        result = subprocess.run(["ollama", "run", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"{green}Model {model_name} installed successfully.{reset}")
        else:
            print(f"{red}Failed to install model {model_name}{reset}:\n-----------------------------------\n{result.stderr}\n")
    except Exception as e:
        print(f"{red}Error installing model {model_name}{reset}:\n-----------------------------------\n{e}\n")

def prompt_user_for_installation(model_name):
    """
    Fragt den Benutzer, ob das Modell installiert werden soll.
    :param model_name: Der Name des Modells.
    :return: True, wenn der Benutzer zustimmt, False ansonsten.
    """
    while True:
        user_input = input(f"Do you want to install the model {model_name}? [y/n]:").strip().lower()
        if user_input in ["y", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print(f"{yellow}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

def save_model_selection(models):
    """
    Speichert die ausgewählten Modelle in einer JSON-Datei.
    :param models: Ein Dictionary mit den ausgewählten Modellen.
    """
    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "model-mavis-4.json")
    mavis_data = {
        "mavis-4": models
    }

    try:
        with open(file_path, 'w') as f:
            json.dump(mavis_data, f, indent=4)
        print(f"{green}Model selection saved to {file_path}{reset}")
    except Exception as e:
        print(f"{red}Error saving model selection: {e}{reset}")

if __name__ == "__main__":
    print("\nOllama Information:")
    print("-------------------")

    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print(f"{green}Ollama is installed.{reset}")
    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")

    start_ollama()
    check_ollama_update()

    # Benutzer fragt nach den Modellnamen
    models = {}
    for i in range(1, 5):
        model_name = input(f"Please select model {i} (e.g. gemma3:12b, llama3.2-vision:11b, qwen2.5:1.5b, granite3.2-vision): ").strip()
        models[f"model{i}"] = model_name

    # Speichern der Auswahl
    save_model_selection(models)

    models_to_check = [models["model1"], models["model2"], models["model3"], models["model4"]]

    for model in models_to_check:
        model_installed = check_model_with_ollama(model)
        if model_installed:
            print(f"{green}{model} is installed.{reset}\n")
        else:
            print(f"{yellow}{model} is not installed.{reset}\n")
            if ollama_installed and prompt_user_for_installation(model):
                install_model_with_ollama(model)
            else:
                print(f"{yellow}Skipping installation of {model}.{reset}\n")
