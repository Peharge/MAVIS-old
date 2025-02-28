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

import sys
import getpass
import os
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

# Den Benutzernamen abrufen
user_name = getpass.getuser()

# Farbcodes definieren
blue = "\033[94m"
reset = "\033[0m"

print(f"""
{blue}      ██╗     █╗      {reset}
{blue}     ████╗   ███╗     {reset}   ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
{blue}    ██████╗  ████╗    {reset}   ████╗ ████║██╔══██╗██║   ██║██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
{blue}   ████████╗  ████╗   {reset}   ██╔████╔██║███████║██║   ██║██║███████╗       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
{blue}  ████╔█████╗  ████╗  {reset}   ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
{blue} ████╔╝╚█████╗  ████╗ {reset}   ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
{blue} ╚═══╝  ╚███╔╝  ╚═══╝ {reset}   ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
{blue}         ╚█╔╝         {reset}
{blue}          ╚╝          {reset}    
""")

print(f"""A warm welcome, {blue}{user_name}{reset}, to MAVIS (MAth Visual Intelligent System) - the most powerful calculator in the world!
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️""")

print(f"""
{blue}MAVIS Version{reset}: 3
{blue}MAVIS Installer Version{reset}: 3
{blue}MAVIS Terminal Version{reset}: 3
{blue}MAVIS License{reset}: MIT
""")

def set_python_path():
    """Set the PYTHON_PATH environment variable."""
    python_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe"
    os.environ["PYTHON_PATH"] = python_path
    print(f"PYTHON_PATH set to {python_path}")

def run_command(command, shell=False):
    """Run a given command using subprocess and print the full output."""
    try:
        print(f"Running command: {command}")  # Debug-Ausgabe
        result = subprocess.run(command, shell=shell, check=True, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        if result.stdout:
            print("Output:", result.stdout, end='')
        if result.stderr:
            print("Error:", result.stderr, end='', file=sys.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error while executing the command: {e.stderr}", end='', file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", end='', file=sys.stderr)

def run_mavis_command(script_path, is_bat=False):
    """Run a MAVIS command."""
    try:
        print(f"Running MAVIS command: {script_path}")

        if is_bat:
            run_command([script_path], shell=True)
        else:
            run_command(["python", script_path], shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Script execution error: {e.stderr}", end='', file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred during MAVIS command execution: {str(e)}", end='', file=sys.stderr)

def handle_special_commands(user_input):
    """Handle special MAVIS commands."""
    commands = {
        "mavis-env-install": "mavis-terminal-3\\install-info-mavis-3.py",
        "mavis-env-update": "mavis-terminal-3\\install-info-mavis-3.py",
        "update-mavis": "mavis-terminal-3\\update-repository-windows.py",
        "mavis-security": "mavis-terminal-3\\security_check.py",
        "mavis-info": "mavis-terminal-3\\info.py",
        "run-mavis": "run-mavis-3-all.bat"
    }

    if user_input in commands:
        script_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\{commands[user_input]}"
        if user_input == "run-mavis":
            run_mavis_command(script_path, is_bat=True)
        else:
            run_mavis_command(script_path)
        return True

    return False

def main():
    set_python_path()
    while True:
        try:
            user_input = input(">>> ").strip()  # User Input
            if user_input.lower() == "exit":
                break
            elif handle_special_commands(user_input):
                continue  # Skip rest of the code, since the special command was handled
            elif user_input.startswith("powershell "):
                run_command(user_input, shell=True)  # Run PowerShell command
            else:
                run_command(user_input.split())  # Execute general commands
            print()  # Print a new line after each command output
            print(">>> ", end='', flush=True)  # Print prompt immediately after each command execution
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred in the main loop: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()
