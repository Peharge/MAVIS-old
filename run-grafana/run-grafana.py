
import os
import subprocess
import platform
import logging
import time
import requests
from urllib.request import urlretrieve

# Konfiguration des Loggings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

GRAFANA_VERSION = "11.1.5"
GRAFANA_WINDOWS_URL = f"https://dl.grafana.com/oss/release/grafana-{GRAFANA_VERSION}.windows-amd64.zip"
GRAFANA_WINDOWS_ZIP = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "run-grafana", "grafana.zip")
GRAFANA_DIR = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "run-grafana", "Grafana")
GRAFANA_EXEC_TEMPLATE = os.path.join(GRAFANA_DIR, "grafana-v11.1.5", "bin", "grafana-server.exe")
GRAFANA_EXEC = os.path.join(GRAFANA_DIR, "bin", "grafana-server.exe")

def download_grafana():
    """Lädt das Grafana-Archiv herunter und überprüft den Download."""
    try:
        logging.info("Download Grafana for Windows...")
        urlretrieve(GRAFANA_WINDOWS_URL, GRAFANA_WINDOWS_ZIP)
        logging.info(f"Grafana was downloaded successfully: {GRAFANA_WINDOWS_ZIP}")
    except Exception as e:
        logging.error(f"Error downloading Grafana: {e}")
        raise

def verify_download():
    """Überprüft, ob die heruntergeladene Datei existiert und die Größe korrekt ist."""
    if not os.path.exists(GRAFANA_WINDOWS_ZIP):
        logging.error("The downloaded archive does not exist.")
        return False
    return True

def extract_grafana():
    """Entpackt das heruntergeladene Grafana-Archiv und überprüft, ob grafana-server.exe existiert."""
    try:
        logging.info("Unpacking Grafana...")
        subprocess.run(["powershell", "-Command", f"Expand-Archive -Path '{GRAFANA_WINDOWS_ZIP}' -DestinationPath '{GRAFANA_DIR}' -Force"], check=True)

        # Nach dem Entpacken prüfen, ob die Datei existiert
        extracted_exec = find_grafana_exec()
        if extracted_exec and os.path.exists(extracted_exec):
            logging.info(f"Grafana was successfully unpacked: {extracted_exec}")
        else:
            logging.error("Error: grafana-server.exe was not found after unpacking!")
            raise FileNotFoundError("Extracting Grafana failed: grafana-server.exe not found.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error unpacking Grafana: {e}")
        raise

def find_grafana_exec():
    """Sucht die Datei grafana-server.exe und gibt den korrekten Pfad zurück."""
    versioned_grafana_dir = os.path.join(GRAFANA_DIR, f"grafana-v{GRAFANA_VERSION}")
    grafana_exec = os.path.join(versioned_grafana_dir, "bin", "grafana-server.exe")

    if os.path.exists(grafana_exec):
        logging.info(f"Found Grafana executable: {grafana_exec}")
        return grafana_exec
    else:
        logging.error(f"ERROR: grafana-server.exe NOT found in: {grafana_exec}")
        return None

def start_grafana():
    """Startet den Grafana-Server und zeigt die Ausgaben an."""
    try:
        grafana_exec = find_grafana_exec()
        if grafana_exec:
            logging.info("Starting Grafana...")

            grafana_homepath = os.path.dirname(os.path.dirname(grafana_exec))

            process = subprocess.Popen([grafana_exec, "--homepath", grafana_homepath],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=grafana_homepath)

            # Echtzeit-Ausgabe von Grafana anzeigen
            for line in process.stdout:
                logging.info(line.strip())
            for line in process.stderr:
                logging.error(line.strip())

            process.wait()
            logging.info("Grafana was started successfully.")
        else:
            logging.error("ERROR: Grafana executable not found. Cannot start Grafana!")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error starting Grafana: {e}")

def wait_for_grafana():
    """Wartet, bis Grafana unter localhost:3000 läuft."""
    while not is_grafana_running():
        logging.info("Waiting for Grafana to start...")
        time.sleep(5)  # Warte 5 Sekunden, bevor erneut geprüft wird

def is_grafana_running():
    """Prüft, ob Grafana unter localhost:3000 läuft."""
    try:
        response = requests.get("http://localhost:3000", timeout=10)
        if response.status_code == 200:
            logging.info("Grafana runs successfully at http://localhost:3000")
            return True
        else:
            logging.warning(f"Grafana responds with status code {response.status_code}.")
            return False
    except requests.ConnectionError:
        logging.warning("Connection to Grafana failed. Grafana is probably not running yet.")
        return False

def install_grafana():
    """Installiert Grafana auf Windows, falls es noch nicht vorhanden ist."""
    try:
        system = platform.system()
        if system != "Windows":
            logging.error("This operating system is not supported.")
            return

        # Prüfen, ob Grafana bereits installiert ist
        grafana_exec = find_grafana_exec()
        if grafana_exec:
            logging.info("Grafana is already installed.")
            return

        # Falls ZIP existiert, nur entpacken
        if os.path.exists(GRAFANA_WINDOWS_ZIP):
            logging.info("Grafana ZIP file already exists. Extracting...")
            extract_grafana()
        else:
            logging.info("Downloading Grafana...")
            download_grafana()
            extract_grafana()

        # Nach der Installation erneut prüfen
        grafana_exec = find_grafana_exec()
        if not grafana_exec:
            logging.error("Installation failed: grafana-server.exe is missing!")
            return

        logging.info("Grafana installation completed successfully.")

    except Exception as e:
        logging.error(f"Installation failed: {e}")
        raise

def ask_to_start_grafana():
    """Fragt den Benutzer, ob er Grafana starten möchte."""
    while True:
        print("\nGrafana Information:")
        print("--------------------")
        choice = input("Do you want to start Grafana? [y/n]:").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            logging.info("Grafana won't start.")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def main():
    try:
        if ask_to_start_grafana():
            install_grafana()
            start_grafana()
            wait_for_grafana()
            logging.info("Grafana now runs at http://localhost:3000")
            # Der Code läuft weiter, solange Grafana unter localhost:3000 läuft
            while is_grafana_running():
                time.sleep(5)  # Alle 5 Sekunden prüfen, ob Grafana noch läuft
        else:
            logging.info("The script exits without starting Grafana.")
    except Exception as e:
        logging.error(f"Error during execution: {e}")
        logging.info("Grafana could not be installed or started correctly.")

if __name__ == "__main__":
    main()
