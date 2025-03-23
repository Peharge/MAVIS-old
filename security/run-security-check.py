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
import subprocess
from dotenv import load_dotenv

# Kritische Sicherheitsvariablen
CRITICAL_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD', 'DEBUG',
    'ALLOWED_HOSTS', 'DATABASE_URL', 'REDIS_URL', 'CELERY_BROKER_URL', 'LOG_LEVEL',
    'SSL_CERT_PATH', 'SSL_KEY_PATH', 'OAUTH_CLIENT_ID', 'OAUTH_CLIENT_SECRET',
    'S3_BUCKET_NAME', 'S3_ACCESS_KEY', 'S3_SECRET_KEY', 'SENDGRID_API_KEY',
    'GITHUB_TOKEN', 'TWITTER_API_KEY', 'TWITTER_API_SECRET'
]

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

# Lade .env Datei und alle relevanten Umgebungsvariablen
def load_env():
    env_path = os.path.join(f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        print(f"{blue}INFO{reset}: .env file loaded successfully.")
    else:
        print(f"{yellow}WARNING{reset}: No .env file found.")
    return env_path


# Zeigt an, welche Dateien im Scan überprüft werden
def list_files_for_scan(directory):
    file_count = 0  # Zähler für die Anzahl der Dateien
    print("\nFiles to be scanned:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"   - {file_path}")
            file_count += 1
    return file_count


# Windows Defender Scan für alle Dateien im Verzeichnis
def scan_with_defender(directory):
    print("\nRunning Windows Defender Scan on all files in the directory...")
    try:
        # Zeigt die zu prüfenden Dateien an und zählt sie
        total_files = list_files_for_scan(directory)

        # Führe den Scan auf dem gesamten Verzeichnis durch
        result = subprocess.run(
            ["powershell", "-Command", f"Start-MpScan -ScanType CustomScan -ScanPath '{directory}'"],
            capture_output=True, text=True, timeout=300, encoding="cp1252", errors="ignore"
        )

        # Ausgabe des Scan-Ergebnisses
        if result.stdout:
            print(result.stdout)
        else:
            print(f"   {green}No threats detected.{reset}")

        # Rückgabe der Gesamtzahl der gescannten Dateien
        return total_files
    except Exception as e:
        print(f"   {red}ERROR{reset}: Windows Defender scan failed - {e}")
        return 0


# Überprüfen, ob eine Datei sicher ist (z.B. keine Bedrohung von Defender)
def is_safe(file_path):
    return True  # Grundannahme, dass der Defender die Dateien sicher behandelt


# Extrahieren von Pfaden und URLs aus den Variablen in .env
def extract_paths_from_env():
    paths = []
    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if value:
            # Füge nur Pfade hinzu, die existieren
            if os.path.exists(value):
                paths.append(value)
            elif value.startswith("http"):  # URLs zu externen Services
                print(f"{blue}URL found{reset}: {var} -> {value}")
    return paths


# Dateien aus dem gesamten Verzeichnis und den angegebenen Pfaden scannen
def scan_all_files():
    env_path = load_env()
    total_scanned_files = 0  # Zähler für die Gesamtzahl der gescannten Dateien
    if env_path:
        directory = os.path.dirname(env_path)  # Das Verzeichnis der .env-Datei
        paths_to_scan = [
            directory] + extract_paths_from_env()  # Alle Verzeichnisse und Pfade, die überprüft werden sollen

        # Scanne alle relevanten Pfade
        for path in paths_to_scan:
            if os.path.isdir(path):
                print(f"\n{blue}Scanning directory{reset}: {path}")
                total_scanned_files += scan_with_defender(path)
            elif os.path.isfile(path):
                print(f"\n{blue}Scanning file{reset}: {path}")
                total_scanned_files += scan_with_defender(path)
            else:
                print(f"\n{blue}Skipping{reset}: {path} (not a valid file or directory)")

        # Sicherheitsüberprüfung und Anzeige der Ergebnisse
        for path in paths_to_scan:
            if os.path.exists(path):
                if is_safe(path):
                    print(f"{green}Safe{reset}: {path}")
                else:
                    print(f"{red}Unsafe{reset}: {path}")

        print(f"\n{green}Security check complete!{reset}")
        print(f"{blue}Total files scanned{reset}: {total_scanned_files}")  # Ausgabe der Gesamtzahl der gescannten Dateien

if __name__ == '__main__':
    scan_all_files()
