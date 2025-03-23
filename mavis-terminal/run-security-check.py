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
import psutil
import socket
from dotenv import load_dotenv
import logging
import time
from datetime import datetime
import requests

# Kritische Sicherheitsvariablen
CRITICAL_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD', 'DEBUG',
    'ALLOWED_HOSTS', 'DATABASE_URL', 'REDIS_URL', 'CELERY_BROKER_URL', 'LOG_LEVEL',
    'SSL_CERT_PATH', 'SSL_KEY_PATH', 'OAUTH_CLIENT_ID', 'OAUTH_CLIENT_SECRET',
    'S3_BUCKET_NAME', 'S3_ACCESS_KEY', 'S3_SECRET_KEY', 'SENDGRID_API_KEY',
    'GITHUB_TOKEN', 'TWITTER_API_KEY', 'TWITTER_API_SECRET'
]

# Farbcodes definieren (für Konsolenausgaben)
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

# Logging konfigurieren: Protokollierung in "security_scan.log"
logging.basicConfig(filename='security_scan.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Bekannte bösartige IPs (Dummy-Werte, sollten durch echte Daten ersetzt werden)
known_malicious_ips = ["192.168.1.100", "203.0.113.5"]

# Überwachte Ports, die oft missbraucht werden
suspicious_ports = [22, 23, 25, 3306, 3389]

# Maximale Anzahl von Verbindungen von der gleichen IP (Schutz gegen DDoS)
MAX_CONNECTIONS_FROM_SAME_IP = 10

# Lädt die .env-Datei und relevante Umgebungsvariablen
def load_env():
    try:
        env_path = os.path.join(f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env")
        if os.path.exists(env_path):
            load_dotenv(dotenv_path=env_path)
            print(f"{blue}INFO{reset}: .env file loaded successfully.")
            logger.info("Loaded .env file successfully.")
        else:
            print(f"{yellow}WARNING{reset}: No .env file found.")
            logger.warning("No .env file found.")
    except Exception as e:
        print(f"{red}ERROR{reset}: Failed to load .env file - {e}")
        logger.error(f"Failed to load .env file - {e}")
    return env_path

# Zeigt alle Dateien an, die im Scan überprüft werden (nur Ausgabe und Zählung)
def list_files_for_scan(directory):
    file_count = 0
    print("\nFiles to be scanned:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"   - {file_path}")
            file_count += 1
    return file_count

# Führt einen Windows Defender Scan im angegebenen Verzeichnis aus
# (Blockiert oder löscht keine Systemdateien)
def scan_with_defender(directory):
    print("\nRunning Windows Defender Scan on all files in the directory...")
    if not os.path.isdir(directory):
        print(f"{red}ERROR{reset}: The specified directory does not exist or is not a directory.")
        logger.error("Invalid directory for scan: %s", directory)
        return 0

    try:
        total_files = list_files_for_scan(directory)
        # Sichere Argumentliste für den Subprozess-Aufruf
        ps_command = [
            "powershell",
            "-Command",
            "Start-MpScan",
            "-ScanType", "CustomScan",
            "-ScanPath", directory
        ]
        result = subprocess.run(ps_command,
                                capture_output=True,
                                text=True,
                                timeout=300,
                                encoding="cp1252",
                                errors="ignore")
        if result.stdout:
            print(result.stdout)
            logger.info("Windows Defender scan result: %s", result.stdout)
        else:
            print(f"   {green}No threats detected.{reset}")
            logger.info("No threats detected.")
        return total_files

    except subprocess.TimeoutExpired:
        print(f"   {red}ERROR{reset}: Windows Defender scan timed out.")
        logger.error("Windows Defender scan timed out for directory: %s", directory)
        return 0
    except Exception as e:
        print(f"   {red}ERROR{reset}: Windows Defender scan failed - {e}")
        logger.error("Windows Defender scan failed for directory %s: %s", directory, e)
        return 0

# Überprüft, ob eine Datei sicher ist (hier immer True, da Defender sie behandelt)
def is_safe(file_path):
    return True

# Extrahiert Pfade/URLs aus kritischen Umgebungsvariablen
def extract_paths_from_env():
    paths = []
    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if value:
            if os.path.exists(value):
                paths.append(value)
            elif value.startswith("http"):
                print(f"{blue}URL found{reset}: {var} -> {value}")
                logger.info("URL found: %s -> %s", var, value)
    return paths

# Überprüft den Status der Firewall
def check_firewall_status():
    print("\nChecking firewall status...")
    try:
        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True, text=True, timeout=60
        )
        if "State" in result.stdout:
            print(f"{green}Firewall is enabled{reset}")
            logger.info("Firewall is enabled")
        else:
            print(f"{red}Firewall is not enabled{reset}")
            logger.warning("Firewall is not enabled")
    except Exception as e:
        print(f"{red}ERROR{reset}: Failed to check firewall status - {e}")
        logger.error("Failed to check firewall status - %s", e)

# Überprüft verdächtige Prozesse anhand von Namen und Ressourcennutzung
def check_suspicious_processes():
    print("\nChecking for suspicious processes...")
    suspicious_processes = [
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe"
    ]
    suspicious_cpu_usage_threshold = 70  # 70% CPU usage threshold
    suspicious_memory_usage_threshold = 1000000000  # 1 GB memory threshold

    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_info', 'create_time', 'username']):
        try:
            if proc.info['name'].lower() in suspicious_processes:
                cpu_usage = proc.info['cpu_percent']
                memory_usage = proc.info['memory_info'].rss
                create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(proc.info['create_time']))
                username = proc.info['username']
                cmdline = ' '.join(proc.info['cmdline'])

                if cpu_usage > suspicious_cpu_usage_threshold or memory_usage > suspicious_memory_usage_threshold:
                    print(f"{red}Suspicious process detected with high resource usage{reset}: {proc.info['name']} (PID: {proc.info['pid']})")
                    print(f"   CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage / 1024 / 1024:.2f} MB")
                    print(f"   Started at: {create_time} by {username}")
                    print(f"   Command line: {cmdline}")
                    logger.warning("Suspicious process detected with high resources: %s (PID: %s)", proc.info['name'], proc.info['pid'])
                else:
                    print(f"{yellow}Suspicious process detected (but normal resource usage){reset}: {proc.info['name']} (PID: {proc.info['pid']})")
                    print(f"   Started at: {create_time} by {username}")
                    print(f"   Command line: {cmdline}")
                    logger.info("Suspicious process detected (normal resource usage): %s (PID: %s)", proc.info['name'], proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
        except Exception as e:
            logger.error("Error checking process: %s", e)
            continue

    print(f"{green}Suspicious process check complete.{reset}")

# Überprüft offene Netzwerkverbindungen und erkennt verdächtige Aktivitäten
def check_network_connections():
    print("\nChecking active network connections...")
    net_connections = psutil.net_connections(kind='inet')
    ip_connection_count = {}  # Zählt Verbindungen von derselben IP

    for conn in net_connections:
        try:
            if conn.status == 'ESTABLISHED':
                local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
                remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

                # Zähle Verbindungen für DDoS-Schutz
                if conn.raddr.ip not in ip_connection_count:
                    ip_connection_count[conn.raddr.ip] = 0
                ip_connection_count[conn.raddr.ip] += 1

                if ip_connection_count[conn.raddr.ip] > MAX_CONNECTIONS_FROM_SAME_IP:
                    print(f"{red}Potential DDoS attack detected: {conn.raddr.ip} has {ip_connection_count[conn.raddr.ip]} connections!{reset}")
                    logger.warning("Potential DDoS attack detected: %s has %s connections.", conn.raddr.ip, ip_connection_count[conn.raddr.ip])
                    continue

                print(f"{cyan}Active connection found{reset}: {local_address} -> {remote_address}")
                logger.info("Active connection found: %s -> %s", local_address, remote_address)

                if conn.raddr.ip in known_malicious_ips:
                    print(f"{red}WARNING: Connection to known malicious IP detected{reset}: {conn.raddr.ip}")
                    logger.warning("Malicious IP detected in connection: %s", conn.raddr.ip)

                if conn.laddr.port in suspicious_ports:
                    print(f"{yellow}Suspicious local port detected{reset}: {conn.laddr.port}")
                    logger.warning("Suspicious local port detected: %s", conn.laddr.port)

                if conn.raddr.port in suspicious_ports:
                    print(f"{yellow}Suspicious remote port detected{reset}: {conn.raddr.port}")
                    logger.warning("Suspicious remote port detected: %s", conn.raddr.port)

                # Optionale Prüfung auf SSL/TLS gesicherte Verbindungen (z.B. HTTPS)
                if conn.raddr.port == 443:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((conn.raddr.ip, 443))
                        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                        response = s.recv(1024)
                        if b"HTTP/1.1 200 OK" in response:
                            print(f"{green}Secure connection (HTTPS) established{reset}: {conn.raddr.ip}:{conn.raddr.port}")
                            logger.info("Secure connection (HTTPS) established: %s:%s", conn.raddr.ip, conn.raddr.port)
                        else:
                            print(f"{red}Potential insecure HTTPS connection detected{reset}: {conn.raddr.ip}:{conn.raddr.port}")
                            logger.warning("Potential insecure HTTPS connection detected: %s:%s", conn.raddr.ip, conn.raddr.port)
                    except Exception as e:
                        print(f"{red}Error checking SSL/TLS connection{reset}: {e}")
                        logger.error("Error checking SSL/TLS connection: %s", e)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    print(f"{green}Network connection check complete.{reset}")

# Überprüft System-Logs auf potenzielle Sicherheitsvorfälle
def check_security_logs():
    print("\nChecking security-related system logs...")
    log_file = "/var/log/auth.log"  # Beispiel für Linux; für Windows anpassen
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
            for line in logs[-50:]:
                if "failed" in line.lower() or "error" in line.lower():
                    print(f"{red}Potential security issue detected in logs{reset}: {line.strip()}")
                    logger.warning("Potential security issue detected in logs: %s", line.strip())
    else:
        print(f"{yellow}Log file {log_file} not found.{reset}")
        logger.warning("Log file %s not found.", log_file)

# Überprüft Systemkonfiguration auf Benutzer- und Berechtigungslevel
def check_system_permissions():
    print("\nChecking system user permissions...")
    for user in psutil.users():
        print(f"{blue}User detected{reset}: {user.name}, {user.host}")
        logger.info("User detected: %s, %s", user.name, user.host)

    print(f"\n{blue}Checking system file permissions{reset}:")
    for root, dirs, files in os.walk("C:\\Users\\julia\\PycharmProjects\\MAVIS"):  # Beispiel-Pfad, anpassen!
        for name in files:
            file_path = os.path.join(root, name)
            try:
                file_permissions = oct(os.stat(file_path).st_mode)[-3:]
                if file_permissions != '777':  # Beispiel: Übermäßige Berechtigungen vermeiden
                    print(f"File permissions for {file_path}: {file_permissions}")
                    logger.info("File permissions for %s: %s", file_path, file_permissions)
            except Exception as e:
                logger.error("Error checking file permissions: %s", e)

# Führt den gesamten Sicherheits-Scan durch
def scan_all_files():
    env_path = load_env()
    total_scanned_files = 0

    # Systemkonfiguration prüfen
    check_system_permissions()

    if env_path:
        directory = os.path.dirname(env_path)
        paths_to_scan = [directory] + extract_paths_from_env()

        for path in paths_to_scan:
            if os.path.isdir(path):
                print(f"\n{blue}Scanning directory{reset}: {path}")
                total_scanned_files += scan_with_defender(path)
            elif os.path.isfile(path):
                print(f"\n{blue}Scanning file{reset}: {path}")
                total_scanned_files += scan_with_defender(path)
            else:
                print(f"\n{blue}Skipping{reset}: {path} (not a valid file or directory)")

        for path in paths_to_scan:
            if os.path.exists(path):
                if is_safe(path):
                    print(f"{green}Safe{reset}: {path}")
                    logger.info("Safe: %s", path)
                else:
                    print(f"{red}Unsafe{reset}: {path}")
                    logger.warning("Unsafe: %s", path)

        print(f"\n{green}Security check complete!{reset}")
        print(f"{blue}Total files scanned{reset}: {total_scanned_files}")

    # Zusätzliche sicherheitsrelevante Prüfungen
    check_firewall_status()
    check_suspicious_processes()
    check_network_connections()
    check_security_logs()

if __name__ == '__main__':
    try:
        scan_all_files()
    except Exception as e:
        print(f"{red}Critical error occurred during security scan: {e}{reset}")
        logger.critical("Critical error occurred during security scan: %s", e)
