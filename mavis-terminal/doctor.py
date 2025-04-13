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

"""
Doctor script for MAVIS project.
Checks the integrity of the .env file, verifies essential tool installations,
and recursively scans the project directory.
"""

import os
import subprocess
import sys
import getpass

issues = []

sys.stdout.reconfigure(encoding='utf-8')

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

def check_file_integrity(file_path):
    """Verify that the specified file exists and is readable."""
    if not os.path.exists(file_path):
        msg = f"File not found: {file_path}"
        print(msg)
        issues.append(msg)
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except Exception as e:
        msg = f"Error reading '{file_path}': {e}"
        print(msg)
        issues.append(msg)
        return False


def get_command_version(command, args, version_parser=lambda out: out.strip()):
    """Execute a command and return its parsed version output, if any."""
    try:
        proc = subprocess.run(
            [command] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = proc.stdout or proc.stderr
        return version_parser(output)
    except Exception as e:
        issues.append(f"{command} failed to run: {e}")
        return None


def check_installation(name, command, args, version_parser=lambda out: out.strip()):
    """Check if a tool is installed by running its version command."""
    print(f"Checking {name}...")
    version = get_command_version(command, args, version_parser)
    if version:
        print(f"  {name} found: {version}")
    else:
        msg = f"{name} NOT found or version check failed."
        print(f"  {msg}")
        issues.append(msg)


def scan_directory(root_path):
    """Recursively print directory structure from the given path."""
    print(f"Scanning directory: {root_path}")
    for dirpath, dirnames, filenames in os.walk(root_path):
        print(f"\nDirectory: {dirpath}")
        for filename in filenames:
            print(f"  File: {filename}")


def powershell_version_parser(output):
    """Extract PSVersion from PowerShell output."""
    for line in output.splitlines():
        if "PSVersion" in line:
            return line.strip()
    return output.strip()


def get_project_path():
    """Get default project path or fallback to current working directory."""
    username = getpass.getuser()
    default_path = os.path.join("C:\\Users", username, "PycharmProjects", "MAVIS")
    return default_path if os.path.exists(default_path) else os.getcwd()


def main():
    print("Doctor Script Started\n")

    base_path = get_project_path()
    env_file = os.path.join(base_path, ".env")

    # 1. Check .env file
    print("Checking the .env file:")
    if check_file_integrity(env_file):
        print("  .env file is present and readable.\n")
    else:
        print("  Problem with the .env file.\n")

    # 2. Check essential tools
    print("Checking system installations:\n")

    check_installation("Python", "python", ["--version"])
    check_installation("Git", "git", ["--version"])
    check_installation("Ollama", "ollama", ["--version"])
    check_installation("FFmpeg", "ffmpeg", ["-version"], lambda o: o.split('\n')[0])
    check_installation("Visual Studio C++ (CL)", "cl", [], lambda o: o.split('\n')[0] if o else "Unknown version")
    check_installation("Rust (rustc)", "rustc", ["--version"])
    check_installation("WSL", "wsl", ["--version"])
    check_installation("PowerShell", "powershell", ["-Command", "$PSVersionTable.PSVersion"], powershell_version_parser)

    # 3. Directory scan
    print("\nScanning the project directory:")
    scan_directory(base_path)

    # 4. Final report
    print("\nDoctor Script Finished")
    if issues:
        print(f"\n{red}Issues Detected{reset}")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
        print("\nPlease resolve the issues above before proceeding.")
    else:
        print(f"\n{green}All checks passed successfully. No issues found.{reset}")


if __name__ == "__main__":
    main()
