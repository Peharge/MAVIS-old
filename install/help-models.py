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
from concurrent.futures import ThreadPoolExecutor

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea,
    QFrame, QSizePolicy, QPushButton, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QPalette, QColor, QIcon, QFont
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_model_with_ollama(model_version: str) -> bool:
    """
    Überprüft, ob ein Modell in Ollama verfügbar ist.
    """
    try:
        result = subprocess.run(
            ["ollama", "show", model_version],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking model {model_version}: {e.stderr}")
        return False
    except Exception as e:
        logging.error(f"Unbekannter Fehler beim Überprüfen des Modells {model_version}: {e}")
        return False


def fetch_models():
    # Beispielhafte Modelle mit Name, Version, Kategorie und Bewertung
    return [
        {"name": "Xc++ I 11b", "version": "xcpp:11b", "category": "Vision Tools", "rating": 4},
        {"name": "Xc++ II 11b", "version": "xcpp2:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Xc++ III 11b", "version": "xcpp3:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Xc++ IV 11b", "version": "xcpp4:11b", "category": "Vision Tools", "rating": 6},
        {"name": "Gemma 3 1b", "version": "gemma3:1b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 4b", "version": "gemma3:4b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 12b", "version": "gemma3:12b", "category": "Vision Tools", "rating": 6},
        {"name": "Gemma 3 27b", "version": "gemma3:27b", "category": "Vision Tools", "rating": 6},
        {"name": "QwQ", "version": "qwq", "category": "Language Model", "rating": 6},
        {"name": "Llama 3.1 8b", "version": "llama3.1:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 70b", "version": "llama3.1:70b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 405b", "version": "llama3.1:405b", "category": "Language Model", "rating": 5},
        {"name": "Llama 3.2 1b", "version": "llama3.2:1b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 3b", "version": "llama3.2:3b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 Vision 11b", "version": "llama3.2-vision:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Llama 3.2 Vision 90b", "version": "llama3.2-vision:90b", "category": "Vision Tools", "rating": 5},
        {"name": "Llama 3.3 70b", "version": "llama3.3", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 14b", "version": "phi4", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 mini 3.8b", "version": "phi4-mini", "category": "Language Model", "rating": 4},
        {"name": "SeepSeek-v3 671", "version": "deepseek-v3", "category": "Language Model", "rating": 4},
        {"name": "SeepSeek-r1 1.5b", "version": "deepseek-r1:1.5b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 7b", "version": "deepseek-r1:7b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 8b", "version": "deepseek-r1:8b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 14b", "version": "deepseek-r1:14b", "category": "Language Model", "rating": 6},
        {"name": "SeepSeek-r1 32b", "version": "deepseek-r1:32b", "category": "Language Model", "rating": 6},
        {"name": "SeepSeek-r1 70b", "version": "deepseek-r1:70b", "category": "Language Model", "rating": 6},
        {"name": "SeepSeek-r1 671b", "version": "deepseek-r1:671b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 2.5 0.5b", "version": "qwen2.5:0.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 1.5b", "version": "qwen2.5:1.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 3b", "version": "qwen2.5:3b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 7b", "version": "qwen2.5:7b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 14b", "version": "qwen2.5:14b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 32b", "version": "qwen2.5:32b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 72b", "version": "qwen2.5:72b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 coder 0.5b", "version": "qwen2.5-coder:0.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 1.5b", "version": "qwen2.5-coder:1.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 3b", "version": "qwen2.5-coder:3b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 7b", "version": "qwen2.5-coder:7b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 14b", "version": "qwen2.5-coder:14b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 32b", "version": "qwen2.5-coder:32b", "category": "Language Model", "rating": 5},
        {"name": "EXAONE Deep 2.4b", "version": "exaone-deep:2.4b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 7.8b", "version": "exaone-deep:7.8b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 32b", "version": "exaone-deep:32b", "category": "Language Model", "rating": 3},
        {"name": "DeepScaleR 1.5b", "version": "deepscaler", "category": "Language Model", "rating": 5},
        {"name": "Mistral Large 123B", "version": "mistral-large", "category": "Language Model", "rating": 5},
        {"name": "Qwen 0.5b", "version": "qwen:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 1.8b", "version": "qwen:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 4b", "version": "qwen:4b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 7b", "version": "qwen:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 14b", "version": "qwen:14b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 32b", "version": "qwen:32b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 72b", "version": "qwen:72b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 110b", "version": "qwen:110b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 0.5b", "version": "qwen2:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 1.5b", "version": "qwen2:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 7b", "version": "qwen2:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 110b", "version": "qwen2:110b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 3.8b", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 14b", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2b", "version": "gemma:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 7b", "version": "gemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 2b", "version": "gemma3:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 9b", "version": "gemma3:9b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 27b", "version": "gemma3:27b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 7b", "version": "codellama:7b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 13b", "version": "codellama:13b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 34b", "version": "codellama:32b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 70b", "version": "codellama:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 7b", "version": "llama2:8b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 13b", "version": "llama2:13b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 70b", "version": "llama2:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 8b", "version": "llama3:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3 70b", "version": "llama3:70b", "category": "Language Model", "rating": 4},
        {"name": "Mistral 7b", "version": "mistral", "category": "Language Model", "rating": 4},
        {"name": "Mistral nemo 12b", "version": "mistral-nemo", "category": "Language Model", "rating": 4},
        {"name": "LlaVA 7b", "version": "llava:7b", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA 13b", "version": "llava:13b", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA 34b", "version": "llava:34b", "category": "Vision Tools", "rating": 3},
        {"name": "Tinyllama 1.1b", "version": "tinyllama", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 3b", "version": "starcoder2:3b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 7b", "version": "starcoder2:7b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 15b", "version": "starcoder2:15b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 7b", "version": "llama2-uncensored:7b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 70b", "version": "llama2-uncensored:70b", "category": "Language Model",
         "rating": 3},
        {"name": "DeepSeek coder v2 16b", "version": "deepseek-coder-v2:16b", "category": "Language Model",
         "rating": 4},
        {"name": "DeepSeek coder v2 236", "version": "deepseek-coder-v2:236b", "category": "Language Model",
         "rating": 4},
        {"name": "Minicpm v 8b", "version": "minicpm-v", "category": "Vision Tools", "rating": 3},
        {"name": "Deepseek coder 1.3b", "version": "deepseek-coder:1.3b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 6.7b", "version": "deepseek-coder:6.7b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 33b", "version": "deepseek-coder:33b", "category": "Language Model", "rating": 3},
        {"name": "Mixtral 8x7b", "version": "mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Mixtral 8x22b", "version": "mixtral:8x22b", "category": "Language Model", "rating": 5},
        {"name": "codegemma 2b", "version": "codegemma:2b", "category": "Language Model", "rating": 3},
        {"name": "codegemma 7b", "version": "codegemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Mixtral 8x7b", "version": "dolphin-mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin Mixtral 8x22b", "version": "dolphin-mixtral:8x22b", "category": "Language Model",
         "rating": 4},
        {"name": "Open Thinker 7b", "version": "openthinker:7b", "category": "Language Model", "rating": 4},
        {"name": "Open Thinker 32b", "version": "openthinker:32b", "category": "Language Model", "rating": 4},
        {"name": "Phi 2.7b", "version": "phi", "category": "Language Model", "rating": 3},
        {"name": "LlaVA Llama3 8b", "version": "llava-llama3", "category": "Vision Tools", "rating": 4},
        {"name": "Dolphin 3 8b", "version": "dolphin3", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 7b", "version": "olmo2:7b", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 13b", "version": "olmo2:13b", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 135m", "version": "smollm2:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 360m", "version": "smollm2:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 1.7b", "version": "smollm2:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 7b", "version": "wizardlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 8x22b", "version": "wizardlm2:8x22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 22b", "version": "mistral-small:22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 24b", "version": "mistral-small:24b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin mistral 7b", "version": "dolphin-mistral:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 8b", "version": "dolphin-llama3:8b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 70b", "version": "dolphin-llama3:70b", "category": "Language Model", "rating": 3},
        {"name": "Command r 35b", "version": "command-r", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 3b", "version": "orca-mini:3b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 7b", "version": "orca-mini:7b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 13b", "version": "orca-mini:13b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 70b", "version": "orca-mini:70b", "category": "Language Model", "rating": 3},
        {"name": "yi 6b", "version": "yi:6b", "category": "Language Model", "rating": 3},
        {"name": "yi 9b", "version": "yi:69b", "category": "Language Model", "rating": 3},
        {"name": "yi 34b", "version": "yi:34b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 1.5b", "version": "qwen2-math:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 7b", "version": "qwen2-math:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 72b", "version": "qwen2-math:72b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 3b", "version": "hermes3:3b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 8b", "version": "hermes3:8b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 70b", "version": "hermes3:70b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 405b", "version": "hermes3:405b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3.5 3.8b", "version": "phi3.5", "category": "Language Model", "rating": 4},
        {"name": "Smollm 125m", "version": "smollm:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 360m", "version": "smollm:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 1.7b", "version": "smollm:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Nuextract 3.8b", "version": "nuextract", "category": "Language Model", "rating": 3},
        {"name": "Firefunction v2 70b", "version": "firefunction-v2", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 groq tool use 8b", "version": "llama3-groq-tool-use:8b", "category": "Language Model",
         "rating": 3},
        {"name": "Llama 3 groq tool use 70b", "version": "llama3-groq-tool-use:70b", "category": "Language Model",
         "rating": 3},
        {"name": "Mathstral 7b", "version": "mathstral", "category": "Language Model", "rating": 3},
        {"name": "Codegee x4 9b", "version": "codegeex4", "category": "Language Model", "rating": 3},
        {"name": "glm4 9b", "version": "glm4", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1m", "version": "internlm2:1m", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1.8b", "version": "internlm2:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 7b", "version": "internlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 20b", "version": "internlm2:20b", "category": "Language Model", "rating": 3},
        {"name": "Codestral 22b", "version": "codestral", "category": "Language Model", "rating": 4},
        {"name": "Granite 3.2 Vision 2b", "version": "granite3.2-vision", "category": "Vision Tools", "rating": 3},
        {"name": "Moon Dream 1.8b", "version": "moondream", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA Llama3 8b", "version": "llava-llama3", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA Phi3 3.8b", "version": "llava-phi3", "category": "Vision Tools", "rating": 3},
        {"name": "Bak LlaVA 7b", "version": "bakllava", "category": "Vision Tools", "rating": 3}
    ]


class ModelCard(QFrame):
    def __init__(self, model: dict, is_installed: bool, parent=None):
        super().__init__(parent)
        self.model = model
        self.is_installed = is_installed
        self.setup_ui()
        self.setup_shadow()
        self.setMouseTracking(True)
        # Feste Höhe für Listendarstellung
        self.setMaximumHeight(100)
        self.setMinimumHeight(100)

    def setup_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setStyleSheet("""
            QFrame {
                background-color: #3b3f44;
                border-radius: 10px;
            }
            QLabel {
                background: transparent;
            }
        """)
        # Horizontales Layout für eine kompakte Listendarstellung
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(15)

        # Name Label
        self.name_label = QLabel(self.model["name"])
        self.name_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.name_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.name_label, 2)

        # Kategorie als Badge
        self.category_label = QLabel(self.model["category"])
        self.category_label.setFont(QFont("Segoe UI", 11))
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.category_label.setStyleSheet("""
            background-color: #ffffff;
            color: #000000;
            padding: 2px 8px;
            border-radius: 8px;
        """)
        self.category_label.setFixedHeight(35)
        layout.addWidget(self.category_label, 1)

        # Sternebewertung
        stars = "★" * self.model["rating"] + "☆" * (6 - self.model["rating"])
        self.rating_label = QLabel(stars)
        self.rating_label.setFont(QFont("Segoe UI", 12))
        self.rating_label.setStyleSheet("color: #f1c40f;")
        layout.addWidget(self.rating_label, 1)

        # Version
        self.version_label = QLabel(f"V: {self.model['version']}")
        self.version_label.setFont(QFont("Segoe UI", 11))
        self.version_label.setStyleSheet("color: #bdc3c7;")
        layout.addWidget(self.version_label, 1)

        # Installationsstatus
        status_text = "Installed" if self.is_installed else "Not Installed"
        status_color = "green" if self.is_installed else "red"
        self.status_label = QLabel(status_text)
        self.status_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.status_label.setStyleSheet(f"color: {status_color};")
        layout.addWidget(self.status_label, 1)

        # Optional: Ein Button für weitere Informationen
        self.info_button = QPushButton("Details")
        self.info_button.setFont(QFont("Segoe UI", 11))
        self.info_button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: none;
                padding: 4px 8px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
        """)
        self.info_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.info_button.setFixedHeight(35)
        layout.addWidget(self.info_button, 1)

        self.setLayout(layout)

    def setup_shadow(self):
        # Schatteneffekt für 3D-Optik
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, event):
        # Schatten wird beim Hover animiert
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(20)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Schatten kehrt zurück
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(10)
        self.anim.start()
        super().leaveEvent(event)


class ModelShop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Model Shop")
        self.setGeometry(100, 100, 1200, 600)
        self.set_dark_mode()
        self.set_background_gradient()

        # Optional: Icon setzen, falls vorhanden
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = os.path.join(f"C:/Users/{user}/PycharmProjects/MAVIS/icons", "mavis-logo.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout(self)
        header = QLabel("Welcome to MAVIS Model Shop")
        header.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        header.setStyleSheet("color: #ecf0f1; padding: 20px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # ScrollArea konfigurieren für die Listendarstellung
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: none;
            }

            QScrollBar:vertical {
                background-color: none;
                width: 10px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: none;
            }

            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {
                background: none;
            }

            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)

        self.content_widget = QWidget()
        # Verwende ein vertikales Layout für die Listendarstellung
        self.vbox_layout = QVBoxLayout(self.content_widget)
        self.vbox_layout.setSpacing(15)
        self.vbox_layout.setContentsMargins(30, 30, 30, 30)
        self.scroll_area.setWidget(self.content_widget)
        main_layout.addWidget(self.scroll_area)

        self.load_models()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
        self.setPalette(palette)

    def set_background_gradient(self):
        # Dezenter vertikaler Farbverlauf als Hintergrund
        self.setStyleSheet("""
            QWidget { 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #000000);
            }
        """)

    def load_models(self):
        models = fetch_models()
        with ThreadPoolExecutor() as executor:
            futures = {model["name"]: executor.submit(check_model_with_ollama, model["version"]) for model in models}
            for model in models:
                is_installed = futures[model["name"]].result()
                card = ModelCard(model, is_installed)
                # Jedes Card-Widget wird untereinander im V-Layout eingefügt
                self.vbox_layout.addWidget(card)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelShop()
    window.show()
    sys.exit(app.exec())
