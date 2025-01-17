import os
import subprocess

# Define color codes
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

def check_command_installed(command):
    """
    Checks if a command-line tool is installed (e.g., ollama).
    :param command: Command name to check.
    :return: True if installed, False otherwise.
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
    Checks if a specific model is available in ollama.
    :param model_name: The name of the model to check.
    :return: True if available, False otherwise.
    """
    try:
        result = subprocess.run(["ollama", "show", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"Model information for {model_name}:\n-----------------------------------\n{result.stdout}\n")
            return True
        else:
            print(f"{yellow}Model {model_name} is not available:\n-----------------------------------\n{result.stderr}{reset}\n")
            return False
    except Exception as e:
        print(f"{red}Error checking model {model_name} with ollama:\n-----------------------------------\n{e}{reset}\n")
        return False

def install_model_with_ollama(model_name):
    """
    Installs a model using ollama if available.
    :param model_name: The name of the model to install.
    """
    try:
        print(f"{cyan}Attempting to install model {model_name} with ollama...{reset}")
        result = subprocess.run(["ollama", "run", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"{green}Model {model_name} installed successfully.{reset}")
        else:
            print(f"{red}Failed to install model {model_name}:\n-----------------------------------\n{result.stderr}{reset}\n")
    except Exception as e:
        print(f"{red}Error installing model {model_name}:\n-----------------------------------\n{e}{reset}\n")

if __name__ == "__main__":
    # Check if ollama is installed
    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print(f"{green}Ollama is installed.{reset}\n")
    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}\n")

    # Check if llama3.2-vision is installed
    llama_installed = check_model_with_ollama("llama3.2-vision")
    if llama_installed:
        print(f"{green}llama3.2-vision is installed.{reset}\n")
    else:
        print(f"{yellow}llama3.2-vision is not installed.{reset}\n")
        if ollama_installed:
            install_model_with_ollama("llama3.2-vision")

    # Check if Smollm is installed
    smollm_installed = check_model_with_ollama("smollm:135m")
    if smollm_installed:
        print(f"{green}Smollm is installed.{reset}")
    else:
        print(f"{yellow}Smollm is not installed.{reset}")
        if ollama_installed:
            install_model_with_ollama("smollm:135m")
