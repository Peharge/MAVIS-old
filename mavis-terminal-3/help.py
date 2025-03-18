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
        "env install": "Installs the required environment for Mavis.",
        "install env": "Installs the Mavis environment.",
        "mavis env install": "Installs the Mavis environment for the Mavis project.",
        "install mavis env": "Installs the specific Mavis environment for the project.",
        "env update": "Updates the Mavis environment to the latest version.",
        "update env": "Updates the environment to the latest version.",
        "mavis env update": "Updates the Mavis environment to the latest version.",
        "update mavis env": "Updates the specific Mavis environment to the latest version.",
        "update": "Performs a repository update.",
        "mavis update": "Performs an update for the Mavis project.",
        "update mavis": "Performs an update for the Mavis installation.",
        "security": "Checks the system’s security.",
        "mavis security": "Performs a security check for the Mavis project.",
        "securitycheck": "Initiates a security check for the system.",
        "info": "Displays general system information.",
        "mavis info": "Displays specific information about the Mavis project.",
        "info mavis": "Shows information about the Mavis installation.",
        "neofetch": "Displays system information in a visually appealing format.",
        "fastfetch": "Displays system information using Neofetch.",
        "jupyter": "Launches Jupyter Notebook environment.",
        "run jupyter": "Starts the Jupyter Notebook environment.",
        "run mavis-1-5-main": "Runs the main version of Mavis 1.5.",
        "run mavis-1-5-math": "Runs the mathematical version of Mavis 1.5.",
        "run mavis-1-5-math-pro": "Runs the professional math version of Mavis 1.5.",
        "run mavis-1-5-math-ultra": "Runs the ultra math version of Mavis 1.5.",
        "run mavis-1-5-math-mini": "Runs the mini math version of Mavis 1.5.",
        "run mavis-1-5-math-mini-mini": "Runs the ultra-mini math version of Mavis 1.5.",
        "run mavis-1-5-code": "Runs the coding version of Mavis 1.5.",
        "run mavis-1-5-code-pro": "Runs the professional coding version of Mavis 1.5.",
        "run mavis-1-5-code-mini": "Runs the mini coding version of Mavis 1.5.",
        "run mavis-1-5-code-mini-mini": "Runs the ultra-mini coding version of Mavis 1.5.",
        "run mavis-1-5-3-math-mini-mini": "Runs the 1.5.3 ultra-mini math version of Mavis.",
        "run mavis-3-main": "Runs the main version of Mavis 3.",
        "run mavis-3-math": "Runs the math version of Mavis 3.",
        "run mavis-3-code": "Runs the coding version of Mavis 3.",
        "run mavis-1-2-main": "Runs the main version of Mavis 1.2.",
        "run mavis-1-2-math": "Runs the math version of Mavis 1.2.",
        "run mavis-1-2-math pro": "Runs the professional math version of Mavis 1.2.",
        "run mavis-1-2-code": "Runs the coding version of Mavis 1.2.",
        "run mavis-1-2-code pro": "Runs the professional coding version of Mavis 1.2.",
        "run mavis-1-2-main-mini": "Runs the mini version of Mavis 1.2.",
        "run mavis-1-2-main-mini-mini": "Runs the ultra-mini version of Mavis 1.2.",
        "run mavis-1-2-3-main": "Runs the 1.2.3 main version of Mavis.",
        "run mavis-1-2-3-math": "Runs the 1.2.3 math version of Mavis.",
        "run mavis-1-2-3-math-pro": "Runs the 1.2.3 professional math version of Mavis.",
        "run mavis-1-2-3-math-ultra": "Runs the 1.2.3 ultra math version of Mavis.",
        "run mavis-1-3-main": "Runs the main version of Mavis 1.3.",
        "run mavis-1-3-math": "Runs the math version of Mavis 1.3.",
        "run mavis-1-3-math pro": "Runs the professional math version of Mavis 1.3.",
        "run mavis-1-3-code": "Runs the coding version of Mavis 1.3.",
        "run mavis-1-3-code pro": "Runs the professional coding version of Mavis 1.3.",
        "run mavis-1-4-math": "Runs the math version of Mavis 1.4.",
        "run ollama mavis-3-main": "Runs the Ollama Mavis 3 Main model.",
        "run ollama mavis-3-main-mini": "Runs the Ollama Mavis 3 Main Mini model.",
        "run ollama mavis-3-math": "Runs the Ollama Mavis 3 Math model.",
        "run ollama mavis-3-math-pro": "Runs the Ollama Mavis 3 Math Pro model.",
        "run ollama mavis-3-math-ultra": "Runs the Ollama Mavis 3 Math Ultra model.",
        "run ollama mavis-3-math-mini": "Runs the Ollama Mavis 3 Math Mini model.",
        "run ollama mavis-3-math-mini-mini": "Runs the Ollama Mavis 3 Math Mini Mini model.",
        "run ollama mavis-3-code": "Runs the Ollama Mavis 3 Code model.",
        "run ollama mavis-3-code-pro": "Runs the Ollama Mavis 3 Code Pro model.",
        "run ollama mavis-3-code-mini": "Runs the Ollama Mavis 3 Code Mini model.",
        "run ollama mavis-3-code-mini-mini": "Runs the Ollama Mavis 3 Code Mini Mini model.",
        "run ollama mavis-3-3-main": "Runs the Ollama Mavis 3.3 Main model.",
        "run ollama mavis-3-3-main-pro": "Runs the Ollama Mavis 3.3 Main Pro model.",
        "run ollama mavis-3-3-main-mini": "Runs the Ollama Mavis 3.3 Main Mini model.",
        "run ollama mavis-3-3-main-mini-mini": "Runs the Ollama Mavis 3.3 Main Mini Mini model.",
        "run ollama mavis-3-3-math": "Runs the Ollama Mavis 3.3 Math model.",
        "run ollama mavis-3-3-math-mini": "Runs the Ollama Mavis 3.3 Math Mini model.",
        "install ollama mavis-1-5-main": "Installs Ollama for the Mavis 1.5 main version.",
        "install ollama mavis-1-5-math": "Installs Ollama for the Mavis 1.5 math version.",
        "install ollama mavis-1-5-math-pro": "Installs Ollama for the Mavis 1.5 professional math version.",
        "install ollama mavis-1-5-math-ultra": "Installs Ollama for the Mavis 1.5 ultra math version.",
        "install ollama mavis-1-5-math-mini": "Installs Ollama for the Mavis 1.5 mini math version.",
        "install ollama mavis-1-5-math-mini-mini": "Installs Ollama for the Mavis 1.5 ultra-mini math version.",
        "install ollama mavis-1-5-code": "Installs Ollama for the Mavis 1.5 code version.",
        "install ollama mavis-1-5-code-pro": "Installs Ollama for the Mavis 1.5 professional code version.",
        "install ollama mavis-1-5-code-mini": "Installs Ollama for the Mavis 1.5 mini code version.",
        "install ollama mavis-1-5-code-mini-mini": "Installs Ollama for the Mavis 1.5 ultra-mini code version.",
        "install ollama mavis-1-5-3-math-mini-mini": "Installs Ollama for the Mavis 1.5.3 ultra-mini math version.",
        "install ollama mavis-3-main": "Installs the Ollama Mavis 3 Main model.",
        "install ollama mavis-3-main-mini": "Installs the Ollama Mavis 3 Main Mini model.",
        "install ollama mavis-3-math": "Installs the Ollama Mavis 3 Math model.",
        "install ollama mavis-3-math-pro": "Installs the Ollama Mavis 3 Math Pro model.",
        "install ollama mavis-3-math-ultra": "Installs the Ollama Mavis 3 Math Ultra model.",
        "install ollama mavis-3-math-mini": "Installs the Ollama Mavis 3 Math Mini model.",
        "install ollama mavis-3-math-mini-mini": "Installs the Ollama Mavis 3 Math Mini Mini model.",
        "install ollama mavis-3-code": "Installs the Ollama Mavis 3 Code model.",
        "install ollama mavis-3-code-pro": "Installs the Ollama Mavis 3 Code Pro model.",
        "install ollama mavis-3-code-mini": "Installs the Ollama Mavis 3 Code Mini model.",
        "install ollama mavis-3-code-mini-mini": "Installs the Ollama Mavis 3 Code Mini Mini model.",
        "install ollama mavis-3-3-main": "Installs the Ollama Mavis 3.3 Main model.",
        "install ollama mavis-3-3-main-pro": "Installs the Ollama Mavis 3.3 Main Pro model.",
        "install ollama mavis-3-3-main-mini": "Installs the Ollama Mavis 3.3 Main Mini model.",
        "install ollama mavis-3-3-main-mini-mini": "Installs the Ollama Mavis 3.3 Main Mini Mini model.",
        "install ollama mavis-3-3-math": "Installs the Ollama Mavis 3.3 Math model.",
        "install ollama mavis-3-3-math-mini": "Installs the Ollama Mavis 3.3 Math Mini model.",
        "grafana": "Runs the Grafana application.",
        "run grafana": "Starts the Grafana application.",
        "install grafana": "Installs the Grafana application.",
        "account": "Manages user account settings.",
        "run deepseek-r1:1.5b": "Runs the DeepSeek model version 1.5b.",
        "run deepseek-r1:7b": "Runs the DeepSeek model version 7b.",
        "run deepseek-r1:8b": "Runs the DeepSeek model version 8b.",
        "run deepseek-r1:14b": "Runs the DeepSeek model version 14b.",
        "run deepseek-r1:32b": "Runs the DeepSeek model version 32b.",
        "run deepseek-r1:70b": "Runs the DeepSeek model version 70b.",
        "run deepseek-r1:671b": "Runs the DeepSeek model version 671b.",
        "run deepscaler": "Runs the DeepScaler application.",
        "run llama3.1:8b": "Runs the Llama3 model version 3.1 8b.",
        "run llama3.1:70b": "Runs the Llama3 model version 3.1 70b.",
        "run llama3.1:405": "Runs the Llama3 model version 3.1 405b.",
        "run llama3.2:1b": "Runs the Llama3 model version 3.2 1b.",
        "run llama3.2:3b": "Runs the Llama3 model version 3.2 3b.",
        "run llama3.3": "Runs the Llama3 model version 3.3.",
        "run llama3:8b": "Runs the Llama3 model version 8b.",
        "run llama3:70b": "Runs the Llama3 model version 70b.",
        "run mistral": "Runs the Mistral model.",
        "run mistral-large": "Runs the Mistral Large model.",
        "run mistral-nemo": "Runs the Mistral Nemo model.",
        "run mistral-openorca": "Runs the Mistral OpenOrca model.",
        "run mistral-small:22b": "Runs the Mistral Small model version 22b.",
        "run mistral-small:24b": "Runs the Mistral Small model version 24b.",
        "run phi4": "Runs the Phi4 model.",
        "run qwen2.5:0.5b": "Runs the Qwen2.5 model version 0.5b.",
        "run qwen2.5:1.5b": "Runs the Qwen2.5 model version 1.5b.",
        "run qwen2.5:3b": "Runs the Qwen2.5 model version 3b.",
        "run qwen2.5:7b": "Runs the Qwen2.5 model version 7b.",
        "run qwen2.5:14b": "Runs the Qwen2.5 model version 14b.",
        "run qwen2.5:32b": "Runs the Qwen2.5 model version 32b.",
        "run qwen2.5:72b": "Runs the Qwen2.5 model version 72b.",
        "run qwen2.5-coder:0.5b": "Runs the Qwen2.5 Coder model version 0.5b.",
        "run qwen2.5-coder:1.5b": "Runs the Qwen2.5 Coder model version 1.5b.",
        "run qwen2.5-coder:3b": "Runs the Qwen2.5 Coder model version 3b.",
        "run qwen2.5-coder:7b": "Runs the Qwen2.5 Coder model version 7b.",
        "run qwen2.5-coder:14b": "Runs the Qwen2.5 Coder model version 14b.",
        "run qwen2.5-coder:32b": "Runs the Qwen2.5 Coder model version 32b.",
        "run gemma3:1b": "Runs the Gemma3 model version 1b.",
        "run gemma3:4b": "Runs the Gemma3 model version 4b.",
        "run gemma3:12b": "Runs the Gemma3 model version 12b.",
        "run gemma3:27b": "Runs the Gemma3 model version 27b.",
        "run qwq": "Runs the Qwq tool.",
        "run command-a": "Runs the Command-A tool.",
        "run phi4-mini": "Runs the Phi4-Mini tool.",
        "run granite3.2:8b": "Runs the Granite 3.2 model version 8b.",
        "run granite3.2:2b": "Runs the Granite 3.2 model version 2b.",
        "run granite3.2-vision:2b": "Runs the Granite 3.2 model version 2b with Vision.",
        "install deepseek-r1:1.5b": "Installs the DeepSeek model version 1.5b.",
        "install deepseek-r1:7b": "Installs the DeepSeek model version 7b.",
        "install deepseek-r1:8b": "Installs the DeepSeek model version 8b.",
        "install deepseek-r1:14b": "Installs the DeepSeek model version 14b.",
        "install deepseek-r1:32b": "Installs the DeepSeek model version 32b.",
        "install deepseek-r1:70b": "Installs the DeepSeek model version 70b.",
        "install deepseek-r1:671b": "Installs the DeepSeek model version 671b.",
        "install deepscaler": "Installs the DeepScaler application.",
        "install llama3.1:8b": "Installs the Llama3 model version 3.1 8b.",
        "install llama3.1:70b": "Installs the Llama3 model version 3.1 70b.",
        "install llama3.1:405": "Installs the Llama3 model version 3.1 405b.",
        "install llama3.2:1b": "Installs the Llama3 model version 3.2 1b.",
        "install llama3.2:3b": "Installs the Llama3 model version 3.2 3b.",
        "install llama3.3": "Installs the Llama3 model version 3.3.",
        "install llama3:8b": "Installs the Llama3 model version 8b.",
        "install llama3:70b": "Installs the Llama3 model version 70b.",
        "install mistral": "Installs the Mistral model.",
        "install mistral-large": "Installs the Mistral Large model.",
        "install mistral-nemo": "Installs the Mistral Nemo model.",
        "install mistral-openorca": "Installs the Mistral OpenOrca model.",
        "install mistral-small:22b": "Installs the Mistral Small model version 22b.",
        "install mistral-small:24b": "Installs the Mistral Small model version 24b.",
        "install phi4": "Installs the Phi4 model.",
        "install qwen2.5:0.5b": "Installs the Qwen2.5 model version 0.5b.",
        "install qwen2.5:1.5b": "Installs the Qwen2.5 model version 1.5b.",
        "install qwen2.5:3b": "Installs the Qwen2.5 model version 3b.",
        "install qwen2.5:7b": "Installs the Qwen2.5 model version 7b.",
        "install qwen2.5:14b": "Installs the Qwen2.5 model version 14b.",
        "install qwen2.5:32b": "Installs the Qwen2.5 model version 32b.",
        "install qwen2.5:72b": "Installs the Qwen2.5 model version 72b.",
        "install qwen2.5-coder:0.5b": "Installs the Qwen2.5 Coder model version 0.5b.",
        "install qwen2.5-coder:1.5b": "Installs the Qwen2.5 Coder model version 1.5b.",
        "install qwen2.5-coder:3b": "Installs the Qwen2.5 Coder model version 3b.",
        "install qwen2.5-coder:7b": "Installs the Qwen2.5 Coder model version 7b.",
        "install qwen2.5-coder:14b": "Installs the Qwen2.5 Coder model version 14b.",
        "install qwen2.5-coder:32b": "Installs the Qwen2.5 Coder model version 32b.",
        "install gemma3:1b": "Installs the Gemma3 model version 1b.",
        "install gemma3:4b": "Installs the Gemma3 model version 4b.",
        "install gemma3:12b": "Installs the Gemma3 model version 12b.",
        "install gemma3:27b": "Installs the Gemma3 model version 27b.",
        "install qwq": "Installs the Qwq tool.",
        "install command-a": "Installs the Command-A tool.",
        "install phi4-mini": "Installs the Phi4-Mini tool.",
        "install granite3.2:8b": "Installs the Granite 3.2 model version 8b.",
        "install granite3.2:2b": "Installs the Granite 3.2 model version 2b.",
        "install granite3.2-vision:2b": "Installs the Granite 3.2 model version 2b with Vision.",
        "m run all": "Runs all available scripts, in a graphic window!",
        "m htop": "Displays a system resource overview (htop), in a graphic window!",
        "m run gemma3": "Runs the Gemma3 script, in a graphic window!",
        "m run deepseek-r1": "Runs all Deepseek-R1 versions, in a graphic window!",
        "m run qwen2.5": "Runs all Qwen 2.5 versions, in a graphic window!",
        "m run qwen2.5-coder": "Runs the Qwen 2.5 Coder versions, in a graphic window!",
        "m python frameworks": "Runs the Python frameworks versions, in a graphic window!",
        "m pip list": "Lists all installed Python packages (pip list), in a graphic window!",
        "m pip ls": "Lists all installed Python packages (pip ls), in a graphic window!",
        "m git": "Lists all install Commits and not install Commits, in a graphic window!",
        "m ls": "Displays a filesystem overview from MAVIS folder (ls), in a graphic window!"
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
