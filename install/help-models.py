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
import os
import subprocess
import logging
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel, QScrollArea
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import Qt
import platform
from concurrent.futures import ThreadPoolExecutor

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_model_with_ollama(model_version: str) -> bool:
    """
    Überprüft, ob ein Modell in Ollama verfügbar ist.

    :param model_version: Der Name des zu prüfenden Modells.
    :return: True, wenn das Modell verfügbar ist, andernfalls False.
    """
    try:
        result = subprocess.run(
            ["ollama", "show", model_version],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=True  # Wirf eine Ausnahme, wenn der Befehl fehlschlägt
        )
        return result.returncode == 0  # Wenn der Rückgabewert 0 ist, wurde das Modell gefunden
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler beim Überprüfen des Modells {model_version}: {e.stderr}")
        return False
    except Exception as e:
        logging.error(f"Unbekannter Fehler beim Überprüfen des Modells {model_version}: {e}")
        return False

def fetch_models():
    return {
        "DeepScaleR 1.5b": "deepscaler",
        "Qwen 0.5b": "qwen:0.5b",
        "Qwen 1.8b": "qwen:1.8b",
        "Qwen 4b": "qwen:4b",
        "Qwen 7b": "qwen:7b",
        "Qwen 14b": "qwen:14b",
        "Qwen 32b": "qwen:32b",
        "Qwen 72b": "qwen:72b",
        "Qwen 110b": "qwen:110b",
        "Qwen 2 0.5b": "qwen2:0.5b",
        "Qwen 2 1.5b": "qwen2:1.5b",
        "Qwen 2 7b": "qwen2:7b",
        "Qwen 2 110b": "qwen2:110b",
        "Qwen 2.5 0.5b": "qwen2.5:0.5b",
        "Qwen 2.5 1.5b": "qwen2.5:1.5b",
        "Qwen 2.5 3b": "qwen2.5:3b",
        "Qwen 2.5 7b": "qwen2.5:7b",
        "Qwen 2.5 14b": "qwen2.5:14b",
        "Qwen 2.5 32b": "qwen2.5:32b",
        "Qwen 2.5 72b": "qwen2.5:72b",
        "Qwen 2.5 coder 0.5b": "qwen2.5-coder:0.5b",
        "Qwen 2.5 coder 1.5b": "qwen2.5-coder:1.5b",
        "Qwen 2.5 coder 3b": "qwen2.5-coder:3b",
        "Qwen 2.5 coder 7b": "qwen2.5-coder:7b",
        "Qwen 2.5 coder 14b": "qwen2.5-coder:14b",
        "Qwen 2.5 coder 32b": "qwen2.5-coder:32b",
        "Phi 3 3.8b": "phi3:14b",
        "Phi 3 14b": "phi3:14b",
        "Phi 4 14b": "phi4",
        "Phi 4 mini 3.8b": "phi4-mini",
        "SeepSeek-v3 671": "deepseek-v3",
        "SeepSeek-r1 1.5b": "deepseek-r1:1.5b",
        "SeepSeek-r1 7b": "deepseek-r1:7b",
        "SeepSeek-r1 8b": "deepseek-r1:8b",
        "SeepSeek-r1 14b": "deepseek-r1:14b",
        "SeepSeek-r1 32b": "deepseek-r1:32b",
        "SeepSeek-r1 70b": "deepseek-r1:70b",
        "SeepSeek-r1 671b": "deepseek-r1:671b",
        "Gemma 2b": "gemma:2b",
        "Gemma 7b": "gemma:7b",
        "Gemma 2 2b": "gemma3:2b",
        "Gemma 2 9b": "gemma3:9b",
        "Gemma 2 27b": "gemma3:27b",
        "Gemma 3 1b": "gemma3:1b",
        "Gemma 3 4b": "gemma3:4b",
        "Gemma 3 12b": "gemma3:12b",
        "Gemma 3 27b": "gemma3:27b",
        "QwQ": "qwq",
        "Code Llama 7b": "codellama:7b",
        "Code Llama 13b": "codellama:13b",
        "Code Llama 34b ": "codellama:32b",
        "Code Llama 70b": "codellama:70b",
        "Llama 2 7b": "llama2:8b",
        "Llama 2 13b": "llama2:13b",
        "Llama 2 70b": "llama2:70b",
        "Llama 3 8b": "llama3:8b",
        "Llama 3 70b": "llama3:70b",
        "Llama 3.1 8b": "llama3.1:8b",
        "Llama 3.1 70b": "llama3.1:70b",
        "Llama 3.1 405b": "llama3.1:405b",
        "Llama 3.2 1b": "llama3.2:1b",
        "Llama 3.2 3b": "llama3.2:3b",
        "Llama 3.2 Vision 11b": "llama3.2-vision:11b",
        "Llama 3.2 Vision 90b": "llama3.2-vision:90b",
        "Llama 3.3": "llama3.3",
        "mistral 7b": "mistral",
        "mistral-nemo 12b": "mistral-nemo",
        "LlaVA 7b": "llava:7b",
        "LlaVA 13b": "llava:13b",
        "LlaVA 34b": "llava:34b",
        "Tinyllama 1.1b": "tinyllama",
        "StarCoder2 3b": "starcoder2:3b",
        "StarCoder2 7b": "starcoder2:7b",
        "StarCoder2 15b": "starcoder2:15b",
        "Llama2 uncensored 7b": "llama2-uncensored:7b",
        "Llama2 uncensored 70b": "llama2-uncensored:70b",
        "deepseek-coder-v2 16b": "deepseek-coder-v2:16b",
        "deepseek-coder-v2 236": "deepseek-coder-v2:236b",
        "minicpm-v 8b": "minicpm-v",
        "deepseek-coder 1.3b": "deepseek-coder:1.3b",
        "deepseek-coder 6.7b": "deepseek-coder:6.7b",
        "deepseek-coder 33b": "deepseek-coder:33b",
        "mixtral 8x7b": "mixtral:8x7b",
        "mixtral 8x22b": "mixtral:8x22b",
        "codegemma 2b": "codegemma:2b",
        "codegemma 7b": "codegemma:7b",
        "dolphin-mixtral 8x7b": "dolphin-mixtral:8x7b",
        "dolphin-mixtral 8x22b": "dolphin-mixtral:8x22b",
        "openthinker 7b": "openthinker:7b",
        "openthinker 32b": "openthinker:32b",
        "phi 2.7b": "phi",
        "llava-llama3 8b": "llava-llama3",
        "dolphin3 8b": "dolphin3",
        "olmo2 7b": "olmo2:7b",
        "olmo2 13b": "olmo2:13b",
        "smollm2 135m": "smollm2:135m",
        "smollm2 360m": "smollm2:360m",
        "smollm2 1.7b": "smollm2:1.7b",
        "wizardlm2 7b": "wizardlm2:7b",
        "wizardlm2 8x22b": "wizardlm2:8x22b",
        "mistral-small 22b": "mistral-small:22b",
        "mistral-small 24b": "mistral-small:24b",
        "dolphin-mistral 7b": "dolphin-mistral:7b",
        "dolphin-llama3 8b": "dolphin-llama3:8b",
        "dolphin-llama3 70b": "dolphin-llama3:70b",
        "command-r 35b": "command-r",
        "orca-mini 3b": "orca-mini:3b",
        "orca-mini 7b": "orca-mini:7b",
        "orca-mini 13b": "orca-mini:13b",
        "orca-mini 70b": "orca-mini:70b",
        "yi 6b": "yi:6b",
        "yi 9b": "yi:69b",
        "yi 34b": "yi:34b",
    }

class FrameworkViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Framework Viewer")
        self.setGeometry(100, 100, 1000, 800)

        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = os.path.join(f"C:/Users/{user}/PycharmProjects/MAVIS/icons", "mavis-logo.ico")
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Modell", "Version"])
        layout.addWidget(self.tree)

        self.status_label = QLabel("Lade...")  # Lade-Status-Label
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.load_models()

    def set_dark_mode(self):
        """
        Setzt die Anwendung in den Dark Mode.
        """
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        self.setPalette(palette)

    def load_models(self):
        """
        Lädt die Modelle und fügt sie dem Baum hinzu.
        """
        models = fetch_models()
        self.tree.clear()

        # ThreadPoolExecutor verwenden, um Modelle asynchron zu überprüfen
        with ThreadPoolExecutor() as executor:
            futures = {model_name: executor.submit(check_model_with_ollama, model_version)
                       for model_name, model_version in models.items()}

            for model_name, future in futures.items():
                is_installed = future.result()  # Blockiert hier, bis das Ergebnis verfügbar ist
                model_version = models[model_name]
                item = QTreeWidgetItem([model_name, model_version])

                # Setze die Farbe der Modellzeile basierend auf der Installation
                if is_installed:
                    item.setForeground(0, QColor(0, 255, 0))  # Grün für installierte Modelle
                else:
                    item.setForeground(0, QColor(255, 0, 0))  # Rot für nicht installierte Modelle

                self.tree.addTopLevelItem(item)

        self.status_label.setText("Modelle erfolgreich geladen.")

    def resizeEvent(self, event):
        """
        Setzt die Breite der Spalten, wenn das Fenster resized wird.
        """
        super().resizeEvent(event)
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.50))
        self.tree.setColumnWidth(1, int(width * 0.40))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrameworkViewer()
    window.show()
    sys.exit(app.exec())
