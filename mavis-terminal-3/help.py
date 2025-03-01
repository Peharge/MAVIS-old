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
        "env install": "Installs the Mavis environment.",
        "mavis env install": "Alias to install the Mavis environment.",
        "env update": "Updates the Mavis environment to the latest version.",
        "mavis env update": "Alias to update the Mavis environment.",
        "update": "Updates the repository for the current Mavis environment.",
        "update mavis": "Alias to update the Mavis repository.",
        "security": "Executes a security check on the system.",
        "mavis security": "Alias to run a Mavis security check.",
        "securitycheck": "Alias to initiate a security check.",
        "info": "Displays general system information.",
        "mavis info": "Alias to show Mavis-specific system information.",
        "neofetch": "Displays system information in a visually appealing format (Neofetch).",
        "jupyter": "Launches the Jupyter Notebook environment.",
        "run jupyter": "Alias to run the Jupyter Notebook environment.",
        "run mavis-1-5-main": "Launches Mavis 1.5 main version.",
        "run mavis-1-5-math": "Launches Mavis 1.5 math version.",
        "run mavis-1-5-math-pro": "Launches Mavis 1.5 math professional version.",
        "run mavis-1-5-math-ultra": "Launches Mavis 1.5 ultra math version.",
        "run mavis-1-5-math-mini": "Launches Mavis 1.5 mini math version.",
        "run mavis-1-5-code": "Launches Mavis 1.5 code version.",
        "run mavis-1-5-code-pro": "Launches Mavis 1.5 code professional version.",
        "run mavis-1-5-3-math-mini-mini": "Launches Mavis 1.5 with mini math version (3).",
        "run mavis-3-main": "Launches Mavis 3 main version.",
        "run mavis-3-math": "Launches Mavis 3 math version.",
        "run mavis-3-code": "Launches Mavis 3 code version.",
        "install ollama mavis-1-5-main": "Installs Ollama with Mavis 1.5 main version.",
        "install ollama mavis-1-5-math": "Installs Ollama with Mavis 1.5 math version.",
        "grafana": "Launches the Grafana dashboard.",
        "install grafana": "Installs the Grafana dashboard.",
        "account": "Manages user account settings for Mavis.",
        "run deepseek-r1:1.5b": "Runs the DeepSeek R1 model with 1.5b parameters.",
        "run deepseek-r1:7b": "Runs the DeepSeek R1 model with 7b parameters.",
        "run llama3.1:8b": "Runs the Llama 3.1 model with 8b parameters.",
        "run qwen2.5:0.5b": "Runs the Qwen 2.5 model with 0.5b parameters.",
        "run qwen2.5-coder:0.5b": "Runs the Qwen 2.5 Coder model with 0.5b parameters.",
        "run mavis": "Installs or runs the Mavis installer."
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
