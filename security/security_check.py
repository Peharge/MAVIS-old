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

import os
import re
import sys
import time
from dotenv import load_dotenv
import subprocess

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

# Kritische Sicherheitsvariablen
CRITICAL_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD'
]

# Schwache Muster
WEAK_PATTERNS = [
    r'1234', r'password', r'test', r'admin', r'secret', r'abc123'
]

def load_env():
    if os.path.exists('.env'):
        load_dotenv()
        print(f"{green}INFO{reset}: .env file loaded successfully.")
    else:
        print(f"{red}WARNING{reset}: No .env file found.")

def loading_bar(duration=3, bar_length=30, message="Running Security Check"):
    try:
        print(f"{blue}{message}{reset}:", end='')

        for _ in range(bar_length):
            sys.stdout.write("█")
            sys.stdout.flush()
            time.sleep(duration / bar_length)

        print("\nDone.\n")
    except KeyboardInterrupt:
        print("\nLoading interrupted.\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")

def check_env_security():
    issues_found = False
    print(f"\n{blue}.env SECURITY CHECK{reset}:")

    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if not value:
            print(f"   {red}ERROR{reset}: {var} is not set!")
            issues_found = True
        elif any(re.search(pattern, value, re.IGNORECASE) for pattern in WEAK_PATTERNS):
            print(f"   {orange}WARNING{reset}: {var} uses a weak pattern: {value}")
            issues_found = True
        elif len(value) < 16:
            print(f"   {yellow}WARNING{reset}: {var} is very short. At least 16 characters recommended.")
            issues_found = True
        elif not all(re.search(p, value) for p in [r'[A-Z]', r'[a-z]', r'[0-9]', r'[!@#$%^&*(),.?":{}|<>]']):
            print(f"   {yellow}WARNING{reset}: {var} should contain uppercase, lowercase, numbers, and special characters.")
            issues_found = True

    if not issues_found:
        print(f"   {green}SECURE{reset}: No obvious issues found.")

def check_outdated_packages():
    print(f"\n{blue}OUTDATED PACKAGES CHECK{reset}")
    try:
        result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True, timeout=60)
        outdated = result.stdout.strip()

        if outdated:
            print(f"   {orange}WARNING{reset}: Outdated packages found:")
            for line in outdated.splitlines()[2:]:
                package_info = line.split()
                package_name = package_info[0]
                current_version = package_info[1]
                latest_version = package_info[2]
                print(
                    f"      {blue}{package_name}{reset}: Current version: {current_version}, Latest version: {latest_version}")
        else:
            print(f"      {green}SECURE{reset}: All packages are up to date.")
    except subprocess.TimeoutExpired:
        print(f"      {red}ERROR{reset}: Package check timed out.")
    except Exception as e:
        print(f"   {red}ERROR{reset}: Error checking packages: {e}")

def get_user_confirmation():
    while True:
        user_input = input(f"Do you want to perform a security check? (y/n):").strip().lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print(f"{red}ERROR{reset}: Invalid input. Please enter y or n.")

def main():
    if get_user_confirmation():
        loading_bar()
        load_env()
        check_env_security()
        check_outdated_packages()
    else:
        print(f"{yellow}INFO{reset}: Security check skipped.")


if __name__ == '__main__':
    main()
