# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

# Farbcodes definieren (kleingeschrieben)
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

def show_help():
    # Kopfzeile
    print("\nThis guide provides descriptions of the available terminal commands and usage instructions.\n")

    # Verfügbare Befehle und Beschreibungen
    print("Available Commands and Their Descriptions")
    print("-----------------------------------------")

    commands = {
        "env install": "Installs the Mavis environment, ensuring all dependencies are correctly set up.",
        "install env": "Installs the Mavis environment, equivalent to 'env install'.",
        "mavis env install": "Alternative command for installing the Mavis environment.",
        "install mavis env": "Alternative command for installing the Mavis environment.",
        "env update": "Updates the Mavis environment to the latest version.",
        "update env": "Updates the Mavis environment, equivalent to 'env update'.",
        "mavis env update": "Alternative command for updating the Mavis environment.",
        "update mavis env": "Alternative command for updating the Mavis environment.",
        "update": "Fetches and applies the latest updates for the Mavis repository.",
        "mavis update": "Alternative command for updating the Mavis repository.",
        "update mavis": "Alternative command for updating the Mavis repository.",
        "security": "Performs a security check to identify vulnerabilities in the system.",
        "mavis security": "Alternative command for performing a security check.",
        "securitycheck": "Alternative command for performing a security check.",
        "info": "Displays system and environment details related to Mavis.",
        "mavis info": "Alternative command for displaying system and environment details.",
        "info mavis": "Alternative command for displaying system and environment details.",
        "neofetch": "Retrieves system hardware and software information in a concise format.",
        "jupyter": "Launches a Jupyter Notebook instance for interactive computing.",
        "run jupyter": "Alternative command for launching Jupyter Notebook.",
        "run mavis-1-5-main": "Executes the primary Mavis 1.5 module.",
        "run mavis-1-5-math": "Runs the mathematics-focused Mavis 1.5 module.",
        "run mavis-1-5-math-pro": "Runs the advanced mathematics module for Mavis 1.5.",
        "run mavis-1-5-math-ultra": "Executes the ultra-performance mathematics module in Mavis 1.5.",
        "run mavis-1-5-math-mini": "Runs the lightweight Mavis 1.5 mathematics module.",
        "run mavis-1-5-math-mini-mini": "Runs the ultra-lightweight Mavis 1.5 mathematics module.",
        "run mavis-1-5-code": "Executes the coding-related Mavis 1.5 module.",
        "run mavis-1-5-code-pro": "Runs the professional version of the Mavis 1.5 coding module.",
        "run mavis-1-5-code-mini": "Runs the lightweight Mavis 1.5 coding module.",
        "run mavis-1-5-code-mini-mini": "Runs the ultra-lightweight Mavis 1.5 coding module.",
        "run mavis-1-5-3-math-mini-mini": "Executes the specialized mini mathematics module in Mavis 1.5.3.",
        "run mavis-3-main": "Launches the core Mavis 3 module.",
        "run mavis-3-math": "Executes the mathematics-focused module in Mavis 3.",
        "run mavis-3-code": "Runs the coding module in Mavis 3.",
        "install ollama mavis-1-5-main": "Installs the Ollama package required for Mavis 1.5 main module.",
        "install ollama mavis-1-5-math": "Installs Ollama for the mathematics-focused Mavis 1.5 module.",
        "install ollama mavis-1-5-math-pro": "Installs Ollama for the advanced Mavis 1.5 math module.",
        "install ollama mavis-1-5-math-ultra": "Installs Ollama for the ultra-performance math module in Mavis 1.5.",
        "install ollama mavis-1-5-math-mini": "Installs Ollama for the lightweight Mavis 1.5 mathematics module.",
        "install ollama mavis-1-5-math-mini-mini": "Installs Ollama for the ultra-lightweight Mavis 1.5 math module.",
        "install ollama mavis-1-5-code": "Installs Ollama for the coding-related Mavis 1.5 module.",
        "install ollama mavis-1-5-code-pro": "Installs Ollama for the professional Mavis 1.5 coding module.",
        "install ollama mavis-1-5-code-mini": "Installs Ollama for the lightweight Mavis 1.5 coding module.",
        "install ollama mavis-1-5-code-mini-mini": "Installs Ollama for the ultra-lightweight Mavis 1.5 coding module.",
        "install ollama mavis-1-5-3-math-mini-mini": "Installs Ollama for the specialized mini mathematics module in Mavis 1.5.3.",
        "install ollama mavis-3-main": "Installs Ollama for the core Mavis 3 module.",
        "install ollama mavis-3-math": "Installs Ollama for the Mavis 3 mathematics module.",
        "install ollama mavis-3-code": "Installs Ollama for the Mavis 3 coding module.",
        "grafana": "Starts the Grafana visualization and monitoring tool.",
        "run grafana": "Alternative command for starting Grafana.",
        "install grafana": "Installs and runs Grafana for visualization and monitoring.",
        "account": "Manages user account settings within the Mavis system.",
        "run deepseek-r1:1.5b": "Runs DeepSeek model version R1 with 1.5 billion parameters.",
        "run deepseek-r1:7b": "Runs DeepSeek model version R1 with 7 billion parameters.",
        "run deepseek-r1:8b": "Runs DeepSeek model version R1 with 8 billion parameters.",
        "run deepseek-r1:14b": "Runs DeepSeek model version R1 with 14 billion parameters.",
        "run deepseek-r1:32b": "Runs DeepSeek model version R1 with 32 billion parameters.",
        "run deepseek-r1:70b": "Runs DeepSeek model version R1 with 70 billion parameters.",
        "run deepseek-r1:671b": "Runs DeepSeek model version R1 with 671 billion parameters.",
        "run deepscaler": "Runs the DeepScaler model for AI-based scaling tasks.",
        "run llama3.1:8b": "Executes the LLaMA 3.1 model with 8 billion parameters.",
        "run llama3.1:70b": "Executes the LLaMA 3.1 model with 70 billion parameters.",
        "run llama3.1:405b": "Executes the LLaMA 3.1 model with 405 billion parameters.",
        "run llama3.2:1b": "Runs LLaMA 3.2 model with 1 billion parameters.",
        "run llama3.2:3b": "Runs LLaMA 3.2 model with 3 billion parameters.",
        "run llama3.3": "Runs LLaMA 3.3 model.",
        "run llama3:8b": "Executes the LLaMA 3 model with 8 billion parameters.",
        "run llama3:70b": "Executes the LLaMA 3 model with 70 billion parameters.",
        "run mistral": "Launches the Mistral AI model for natural language processing.",
        "run phi4": "Starts the Phi-4 AI model for computational tasks.",
        "run qwen2.5:0.5b": "Runs Qwen 2.5 model with 0.5 billion parameters.",
        "run qwen2.5:1.5b": "Runs Qwen 2.5 model with 1.5 billion parameters.",
        "run qwen2.5:3b": "Runs Qwen 2.5 model with 3 billion parameters.",
        "run qwen2.5:7b": "Runs Qwen 2.5 model with 7 billion parameters.",
        "run qwen2.5:14b": "Runs Qwen 2.5 model with 14 billion parameters.",
        "run qwen2.5:32b": "Runs Qwen 2.5 model with 32 billion parameters.",
        "run qwen2.5:72b": "Runs Qwen 2.5 model with 72 billion parameters.",
        "help": "Displays the list of available commands and their descriptions.",
        "run mavis": "Initializes the Mavis installer for system-wide setup."
    }

    # Drucken der Befehle in einem übersichtlichen, tabellenähnlichen Format
    for command, description in commands.items():
        print(f"{blue}{command}{reset}: {description}")

    # How to use pip and PowerShell
    print("\nHow to Use pip and PowerShell")
    print("-----------------------------")

    # pip instructions
    print("1. Using `pip` (Python Package Installer):")
    print(" - To install a Python package, execute the following command in your terminal or command prompt:")
    print("  pip install <package_name>")
    print("  Example: pip install numpy")
    print(" - To upgrade pip itself, run:")
    print("  python -m pip install --upgrade pip")
    print(" - Note: In some environments, you may need to use `pip3` instead of `pip`.\n")

    # PowerShell instructions
    print("2. Using PowerShell:")
    print(" - To run Python scripts in PowerShell, navigate to the script directory and execute the command:")
    print("  python <script_name>.py")
    print("  Example: python my_script.py")
    print(" - To install Python packages in PowerShell using pip, run:")
    print("  pip install <package_name>")
    print("  Example: pip install requests")
    print(" - If you're using PowerShell as an administrator and face any permission issues, try running it as Administrator.\n")

    print("For more information, refer to the official documentation or contact support.")


# Call the help function
show_help()
