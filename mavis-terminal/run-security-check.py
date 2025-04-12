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
from logging.handlers import RotatingFileHandler
import time
from datetime import datetime
from pathlib import Path
import requests

# ============================
# Konfiguration / Konstanten
# ============================
CRITICAL_VARS = [
    'SECRET_KEY', 'DB_PASSWORD', 'API_KEY', 'JWT_SECRET', 'EMAIL_PASSWORD', 'DEBUG',
    'ALLOWED_HOSTS', 'DATABASE_URL', 'REDIS_URL', 'CELERY_BROKER_URL', 'LOG_LEVEL',
    'SSL_CERT_PATH', 'SSL_KEY_PATH', 'OAUTH_CLIENT_ID', 'OAUTH_CLIENT_SECRET',
    'S3_BUCKET_NAME', 'S3_ACCESS_KEY', 'S3_SECRET_KEY', 'SENDGRID_API_KEY',
    'GITHUB_TOKEN', 'TWITTER_API_KEY', 'TWITTER_API_SECRET'
]

# Farben für Konsolenausgabe
COLORS = {
    'red': "\033[91m",
    'green': "\033[92m",
    'yellow': "\033[93m",
    'blue': "\033[94m",
    'magenta': "\033[95m",
    'cyan': "\033[96m",
    'white': "\033[97m",
    'reset': "\033[0m",
    'bold': "\033[1m"
}

# Bekannte bösartige IPs (Dummy – bitte bei Bedarf aktualisieren)
KNOWN_MALICIOUS_IPS = {"192.168.1.100", "203.0.113.5"}

# Überwachte Ports, die oft missbraucht werden
SUSPICIOUS_PORTS = {22, 23, 25, 3306, 3389}

# Maximale Anzahl von Verbindungen von derselben IP (DDoS-Schutz)
MAX_CONNECTIONS_FROM_SAME_IP = 10

# Schwellenwerte für Ressourcenverbrauch bei Prozessen
SUSPICIOUS_CPU_THRESHOLD = 70              # in Prozent
SUSPICIOUS_MEMORY_THRESHOLD = 1_000_000_000  # in Bytes (1GB)

# Basisverzeichnis des Projekts (bitte anpassen, falls erforderlich)
DEFAULT_PROJECT_DIR = Path.home() / "PycharmProjects" / "MAVIS"

# ============================
# Logging-Konfiguration
# ============================
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler("security_scan.log", maxBytes=5*1024*1024, backupCount=2)
log_handler.setFormatter(log_formatter)
logger = logging.getLogger("SecurityScanner")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# ============================
# Umgebungsvariablen laden
# ============================
def load_env() -> Path:
    """
    Lädt die .env-Datei und gibt den Pfad zurück. Fehler werden geloggt.
    """
    try:
        try:
            user = os.getlogin()
        except Exception:
            user = os.environ.get("USERNAME", "default")
        env_path = Path(f"C:/Users/{user}/PycharmProjects/MAVIS/.env")
        if env_path.exists():
            load_dotenv(dotenv_path=str(env_path))
            print(f"{COLORS['blue']}INFO{COLORS['reset']}: .env file loaded successfully.")
            logger.info("Loaded .env file successfully.")
        else:
            print(f"{COLORS['yellow']}WARNING{COLORS['reset']}: No .env file found at {env_path}.")
            logger.warning("No .env file found at %s.", env_path)
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Failed to load .env file – {e}")
        logger.error("Failed to load .env file: %s", e)
    return env_path

# ============================
# Sichere Dateiauflistung
# ============================
def safe_iter_files(directory: Path):
    """
    Iteriert rekursiv über ein Verzeichnis und liefert Dateien, wobei Zugriffsfehler
    abgefangen und geloggt werden, sodass der Scan nicht unterbrochen wird.
    """
    try:
        for entry in directory.iterdir():
            try:
                if entry.is_file():
                    yield entry
                elif entry.is_dir():
                    yield from safe_iter_files(entry)
            except Exception as e:
                logger.error("Error accessing entry %s: %s", entry, e)
                continue
    except Exception as e:
        logger.error("Error scanning directory %s: %s", directory, e)

# ============================
# Dateien listen und zählen
# ============================
def list_files_for_scan(directory: Path) -> int:
    """
    Gibt alle Dateien aus und zählt diese im Verzeichnis (mit sicherer Iteration).
    """
    file_count = 0
    print("\nFiles to be scanned:")
    for file_path in safe_iter_files(directory):
        print(f"   - {file_path}")
        file_count += 1
    return file_count

# ============================
# Windows Defender Scan ausführen
# ============================
def scan_with_defender(target: Path) -> int:
    """
    Führt einen Windows Defender Scan auf dem angegebenen Pfad durch.
    """
    print(f"\nRunning Windows Defender Scan on: {target}")
    if not target.exists():
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: The specified path does not exist: {target}")
        logger.error("Invalid target for scan: %s", target)
        return 0

    try:
        total_files = list_files_for_scan(target)
        ps_command = [
            "powershell", "-Command",
            "Start-MpScan", "-ScanType", "CustomScan", "-ScanPath", str(target)
        ]
        result = subprocess.run(ps_command,
                                capture_output=True,
                                text=True,
                                timeout=300,
                                encoding="cp1252",
                                errors="ignore")
        if result.stdout.strip():
            print(result.stdout)
            logger.info("Windows Defender scan result: %s", result.stdout)
        else:
            print(f"{COLORS['green']}No threats detected.{COLORS['reset']}")
            logger.info("No threats detected during scan on %s", target)
        return total_files
    except subprocess.TimeoutExpired:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Windows Defender scan timed out.")
        logger.error("Windows Defender scan timed out for target: %s", target)
        return 0
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Windows Defender scan failed – {e}")
        logger.error("Windows Defender scan failed for %s: %s", target, e)
        return 0

# ============================
# Überprüfung, ob Pfad als sicher gilt
# ============================
def is_safe(file_path: Path) -> bool:
    """
    Dummy-Funktion. Zur weiteren Erweiterung (z. B. Hash-Prüfung, Zertifikatsvergleiche).
    """
    return True

# ============================
# Extrahieren von Pfaden/URLs aus Umgebungsvariablen
# ============================
def extract_paths_from_env() -> list:
    """
    Extrahiert Pfade und URLs aus kritischen Umgebungsvariablen.
    """
    paths = []
    for var in CRITICAL_VARS:
        value = os.getenv(var)
        if value:
            candidate = Path(value)
            if candidate.exists():
                paths.append(candidate)
                logger.info("Local path found: %s -> %s", var, value)
            elif value.startswith("http"):
                print(f"{COLORS['blue']}URL found{COLORS['reset']}: {var} -> {value}")
                logger.info("URL found: %s -> %s", var, value)
    return paths

# ============================
# Firewall-Status prüfen
# ============================
def check_firewall_status():
    print("\nChecking firewall status...")
    try:
        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True, text=True, timeout=60
        )
        if "State" in result.stdout:
            print(f"{COLORS['green']}Firewall is enabled{COLORS['reset']}")
            logger.info("Firewall is enabled")
        else:
            print(f"{COLORS['red']}Firewall is not enabled{COLORS['reset']}")
            logger.warning("Firewall is not enabled")
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Failed to check firewall status – {e}")
        logger.error("Failed to check firewall status: %s", e)

# ============================
# Überprüfung verdächtiger Prozesse
# ============================
def check_suspicious_processes():
    print("\nChecking for suspicious processes...")
    suspicious_processes = {
        "cmd.exe", "powershell.exe", "netstat.exe", "whois.exe",
        "python.exe", "java.exe", "wget.exe", "curl.exe", "nc.exe", "nmap.exe"
    }

    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_info', 'create_time', 'username']):
        try:
            name = (proc.info['name'] or "").lower()
            if name in suspicious_processes:
                cpu_usage = proc.info.get('cpu_percent', 0)
                mem_info = proc.info.get('memory_info')
                memory_usage = getattr(mem_info, 'rss', 0) if mem_info else 0
                create_time = datetime.fromtimestamp(proc.info.get('create_time', time.time())).strftime("%Y-%m-%d %H:%M:%S")
                username = proc.info.get('username', 'Unknown')
                cmdline = " ".join(proc.info.get('cmdline', []))
                if cpu_usage > SUSPICIOUS_CPU_THRESHOLD or memory_usage > SUSPICIOUS_MEMORY_THRESHOLD:
                    print(f"{COLORS['red']}Suspicious process detected with high resource usage{COLORS['reset']}: {proc.info['name']} (PID: {proc.info['pid']})")
                    print(f"   CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage / (1024*1024):.2f} MB")
                    print(f"   Started at: {create_time} by {username}")
                    print(f"   Command line: {cmdline}")
                    logger.warning("High resource usage process: %s (PID: %s)", proc.info['name'], proc.info['pid'])
                else:
                    print(f"{COLORS['yellow']}Suspicious process detected (but normal resource usage){COLORS['reset']}: {proc.info['name']} (PID: {proc.info['pid']})")
                    print(f"   Started at: {create_time} by {username}")
                    print(f"   Command line: {cmdline}")
                    logger.info("Process detected: %s (PID: %s)", proc.info['name'], proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
        except Exception as e:
            logger.error("Error checking process: %s", e)
            continue
    print(f"{COLORS['green']}Suspicious process check complete.{COLORS['reset']}")

# ============================
# Überprüfung offener Netzwerkverbindungen
# ============================
def check_network_connections():
    print("\nChecking active network connections...")
    try:
        net_connections = psutil.net_connections(kind='inet')
    except Exception as e:
        print(f"{COLORS['red']}ERROR{COLORS['reset']}: Failed to retrieve network connections – {e}")
        logger.error("Failed to get network connections: %s", e)
        return

    ip_connection_count = {}
    for conn in net_connections:
        try:
            if conn.status == 'ESTABLISHED' and conn.raddr:
                local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}"
                remote_ip = conn.raddr.ip
                ip_connection_count[remote_ip] = ip_connection_count.get(remote_ip, 0) + 1
                if ip_connection_count[remote_ip] > MAX_CONNECTIONS_FROM_SAME_IP:
                    print(f"{COLORS['red']}Potential DDoS attack detected{COLORS['reset']}: {remote_ip} has {ip_connection_count[remote_ip]} connections!")
                    logger.warning("Potential DDoS: %s has %s connections.", remote_ip, ip_connection_count[remote_ip])
                    continue
                print(f"{COLORS['cyan']}Active connection found{COLORS['reset']}: {local_addr} -> {remote_addr}")
                logger.info("Active connection: %s -> %s", local_addr, remote_addr)
                if remote_ip in KNOWN_MALICIOUS_IPS:
                    print(f"{COLORS['red']}WARNING: Connection to known malicious IP detected{COLORS['reset']}: {remote_ip}")
                    logger.warning("Malicious IP connection: %s", remote_ip)
                if conn.laddr.port in SUSPICIOUS_PORTS:
                    print(f"{COLORS['yellow']}Suspicious local port detected{COLORS['reset']}: {conn.laddr.port}")
                    logger.warning("Suspicious local port: %s", conn.laddr.port)
                if conn.raddr.port in SUSPICIOUS_PORTS:
                    print(f"{COLORS['yellow']}Suspicious remote port detected{COLORS['reset']}: {conn.raddr.port}")
                    logger.warning("Suspicious remote port: %s", conn.raddr.port)
                if conn.raddr.port == 443:
                    try:
                        with socket.create_connection((remote_ip, 443), timeout=5) as s:
                            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                            response = s.recv(1024)
                        if b"HTTP/1.1 200 OK" in response or b"HTTP/1.0 200 OK" in response:
                            print(f"{COLORS['green']}Secure connection (HTTPS) established{COLORS['reset']}: {remote_ip}:443")
                            logger.info("Secure HTTPS connection: %s:443", remote_ip)
                        else:
                            print(f"{COLORS['red']}Potential insecure HTTPS connection detected{COLORS['reset']}: {remote_ip}:443")
                            logger.warning("Insecure HTTPS connection: %s:443", remote_ip)
                    except Exception as e:
                        print(f"{COLORS['red']}Error checking SSL/TLS connection{COLORS['reset']}: {e}")
                        logger.error("SSL/TLS check error for %s:443 – %s", remote_ip, e)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"{COLORS['green']}Network connection check complete.{COLORS['reset']}")

# ============================
# System-Logs auf Sicherheitsvorfälle prüfen
# ============================
def check_security_logs():
    print("\nChecking security-related system logs...")
    # Beispielpfad für Linux – bitte bei Bedarf anpassen (unter Windows andere Logs)
    log_file = Path("/var/log/auth.log")
    if log_file.exists():
        try:
            with log_file.open("r", encoding="utf-8", errors="ignore") as f:
                logs = f.readlines()[-50:]  # Letzte 50 Zeilen
                for line in logs:
                    if "failed" in line.lower() or "error" in line.lower():
                        print(f"{COLORS['red']}Potential security issue detected in logs{COLORS['reset']}: {line.strip()}")
                        logger.warning("Security issue in log: %s", line.strip())
        except Exception as e:
            print(f"{COLORS['red']}ERROR{COLORS['reset']}: Failed to read log file – {e}")
            logger.error("Failed to read log file %s: %s", log_file, e)
    else:
        print(f"{COLORS['yellow']}Log file {log_file} not found.{COLORS['reset']}")
        logger.warning("Log file %s not found.", log_file)

# ============================
# Systemkonfiguration prüfen (Benutzer & Dateiberechtigungen)
# ============================
def check_system_permissions():
    print("\nChecking system user permissions...")
    try:
        for user in psutil.users():
            print(f"{COLORS['blue']}User detected{COLORS['reset']}: {user.name}, {user.host}")
            logger.info("User detected: %s, %s", user.name, user.host)
    except Exception as e:
        logger.error("Failed to check system users: %s", e)

    print(f"\n{COLORS['blue']}Checking system file permissions{COLORS['reset']}:")
    base_dir = DEFAULT_PROJECT_DIR
    for file_path in safe_iter_files(base_dir):
        try:
            permissions = oct(os.stat(file_path).st_mode & 0o777)[2:]
            # Warnung, falls Berechtigungen zu offen sind (hier: über 755 wird als zu permissiv gewertet)
            if int(permissions, 8) > 0o755:
                print(f"{COLORS['yellow']}Warning: Overly permissive permissions for {file_path}: {permissions}{COLORS['reset']}")
                logger.warning("Overly permissive permissions for %s: %s", file_path, permissions)
            else:
                logger.info("File permissions for %s: %s", file_path, permissions)
        except Exception as e:
            logger.error("Error checking file permissions for %s: %s", file_path, e)

# ============================
# Gesamter Sicherheits-Scan
# ============================
def scan_all_files():
    env_path = load_env()
    total_scanned_files = 0

    # Systemkonfiguration und Dateiberechtigungen prüfen
    check_system_permissions()

    if env_path:
        base_directory = env_path.parent
        paths_to_scan = [base_directory] + extract_paths_from_env()
        for path in paths_to_scan:
            if path.is_dir():
                print(f"\n{COLORS['blue']}Scanning directory{COLORS['reset']}: {path}")
                total_scanned_files += scan_with_defender(path)
            elif path.is_file():
                print(f"\n{COLORS['blue']}Scanning file{COLORS['reset']}: {path}")
                total_scanned_files += scan_with_defender(path)
            else:
                print(f"\n{COLORS['blue']}Skipping{COLORS['reset']}: {path} (invalid file/directory)")
                logger.info("Skipping invalid path: %s", path)
        for path in paths_to_scan:
            if path.exists():
                if is_safe(path):
                    print(f"{COLORS['green']}Safe{COLORS['reset']}: {path}")
                    logger.info("Safe: %s", path)
                else:
                    print(f"{COLORS['red']}Unsafe{COLORS['reset']}: {path}")
                    logger.warning("Unsafe: %s", path)
        print(f"\n{COLORS['green']}Security check complete!{COLORS['reset']}")
        print(f"{COLORS['blue']}Total files scanned{COLORS['reset']}: {total_scanned_files}")
    else:
        print(f"{COLORS['red']}Critical Error: Unable to determine project environment.{COLORS['reset']}")
        logger.critical("No .env file loaded; cannot determine project environment.")

    # Weitere Prüfungen
    check_firewall_status()
    check_suspicious_processes()
    check_network_connections()
    check_security_logs()

# ============================
# Main-Block
# ============================
if __name__ == '__main__':
    try:
        scan_all_files()
    except Exception as e:
        print(f"{COLORS['red']}Critical error occurred during security scan: {e}{COLORS['reset']}")
        logger.critical("Critical error occurred during security scan: %s", e)
