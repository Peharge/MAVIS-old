import sys
import os
import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout,
    QFrame, QSizePolicy, QGraphicsDropShadowEffect
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
        {"name": "Xc++ I", "version": "xcpp:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Xc++ II", "version": "xcpp2:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Xc++ III", "version": "xcpp3:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Xc++ IV", "version": "xcpp4:11b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 1b", "version": "gemma3:1b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 4b", "version": "gemma3:4b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 12b", "version": "gemma3:12b", "category": "Vision Tools", "rating": 5},
        {"name": "Gemma 3 27b", "version": "gemma3:27b", "category": "Vision Tools", "rating": 5},
        {"name": "QwQ", "version": "qwq", "category": "Language Model", "rating": 5},
        {"name": "Llama 3.1 8b", "version": "llama3.1:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 70b", "version": "llama3.1:70b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 405b", "version": "llama3.1:405b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 1b", "version": "llama3.2:1b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 3b", "version": "llama3.2:3b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 Vision 11b", "version": "llama3.2-vision:11b", "category": "Vision Tools","rating": 4},
        {"name": "Llama 3.2 Vision 90b", "version": "llama3.2-vision:90b", "category": "Vision Tools","rating": 4},
        {"name": "Llama 3.3", "version": "llama3.3", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 14b", "version": "phi4", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 mini 3.8b", "version": "phi4-mini", "category": "Language Model", "rating": 4},
        {"name": "SeepSeek-v3 671", "version": "deepseek-v3", "category": "Language Model", "rating": 4},
        {"name": "SeepSeek-r1 1.5b", "version": "deepseek-r1:1.5b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 7b", "version": "deepseek-r1:7b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 8b", "version": "deepseek-r1:8b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 14b", "version": "deepseek-r1:14b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 32b", "version": "deepseek-r1:32b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 70b", "version": "deepseek-r1:70b", "category": "Language Model", "rating": 5},
        {"name": "SeepSeek-r1 671b", "version": "deepseek-r1:671b", "category": "Language Model", "rating": 3},
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
        {"name": "mistral 7b", "version": "mistral", "category": "Language Model", "rating": 4},
        {"name": "mistral-nemo 12b", "version": "mistral-nemo", "category": "Language Model", "rating": 4},
        {"name": "LlaVA 7b", "version": "llava:7b", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA 13b", "version": "llava:13b", "category": "Vision Tools", "rating": 3},
        {"name": "LlaVA 34b", "version": "llava:34b", "category": "Vision Tools", "rating": 3},
        {"name": "Tinyllama 1.1b", "version": "tinyllama", "category": "Language Model", "rating": 3},
        {"name": "StarCoder2 3b", "version": "starcoder2:3b", "category": "Language Model", "rating": 3},
        {"name": "StarCoder2 7b", "version": "starcoder2:7b", "category": "Language Model", "rating": 3},
        {"name": "StarCoder2 15b", "version": "starcoder2:15b", "category": "Language Model", "rating": 3},
        {"name": "Llama2 uncensored 7b", "version": "llama2-uncensored:7b", "category": "Language Model", "rating": 3},
        {"name": "Llama2 uncensored 70b", "version": "llama2-uncensored:70b", "category": "Language Model","rating": 3},
        {"name": "deepseek-coder-v2 16b", "version": "deepseek-coder-v2:16b", "category": "Language Model","rating": 4},
        {"name": "deepseek-coder-v2 236", "version": "deepseek-coder-v2:236b", "category": "Language Model","rating": 4},
        {"name": "minicpm-v 8b", "version": "minicpm-v", "category": "Vision Tools", "rating": 3},
        {"name": "deepseek-coder 1.3b", "version": "deepseek-coder:1.3b", "category": "Language Model", "rating": 3},
        {"name": "deepseek-coder 6.7b", "version": "deepseek-coder:6.7b", "category": "Language Model", "rating": 3},
        {"name": "deepseek-coder 33b", "version": "deepseek-coder:33b", "category": "Language Model", "rating": 3},
        {"name": "mixtral 8x7b", "version": "mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "mixtral 8x22b", "version": "mixtral:8x22b", "category": "Language Model", "rating": 5},
        {"name": "codegemma 2b", "version": "codegemma:2b", "category": "Language Model", "rating": 3},
        {"name": "codegemma 7b", "version": "codegemma:7b", "category": "Language Model", "rating": 3},
        {"name": "dolphin-mixtral 8x7b", "version": "dolphin-mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "dolphin-mixtral 8x22b", "version": "dolphin-mixtral:8x22b", "category": "Language Model","rating": 4},
        {"name": "openthinker 7b", "version": "openthinker:7b", "category": "Language Model", "rating": 4},
        {"name": "openthinker 32b", "version": "openthinker:32b", "category": "Language Model", "rating": 4},
        {"name": "phi 2.7b", "version": "phi", "category": "Language Model", "rating": 3},
        {"name": "llava-llama3 8b", "version": "llava-llama3", "category": "Vision Tools", "rating": 4},
        {"name": "dolphin3 8b", "version": "dolphin3", "category": "Language Model", "rating": 3},
        {"name": "olmo2 7b", "version": "olmo2:7b", "category": "Language Model", "rating": 3},
        {"name": "olmo2 13b", "version": "olmo2:13b", "category": "Language Model", "rating": 3},
        {"name": "smollm2 135m", "version": "smollm2:135m", "category": "Language Model", "rating": 3},
        {"name": "smollm2 360m", "version": "smollm2:360m", "category": "Language Model", "rating": 3},
        {"name": "smollm2 1.7b", "version": "smollm2:1.7b", "category": "Language Model", "rating": 3},
        {"name": "wizardlm2 7b", "version": "wizardlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "wizardlm2 8x22b", "version": "wizardlm2:8x22b", "category": "Language Model", "rating": 4},
        {"name": "mistral-small 22b", "version": "mistral-small:22b", "category": "Language Model", "rating": 4},
        {"name": "mistral-small 24b", "version": "mistral-small:24b", "category": "Language Model", "rating": 4},
        {"name": "dolphin-mistral 7b", "version": "dolphin-mistral:7b", "category": "Language Model", "rating": 3},
        {"name": "dolphin-llama3 8b", "version": "dolphin-llama3:8b", "category": "Language Model", "rating": 3},
        {"name": "dolphin-llama3 70b", "version": "dolphin-llama3:70b", "category": "Language Model", "rating": 3},
        {"name": "command-r 35b", "version": "command-r", "category": "Language Model", "rating": 3},
        {"name": "orca-mini 3b", "version": "orca-mini:3b", "category": "Language Model", "rating": 3},
        {"name": "orca-mini 7b", "version": "orca-mini:7b", "category": "Language Model", "rating": 3},
        {"name": "orca-mini 13b", "version": "orca-mini:13b", "category": "Language Model", "rating": 3},
        {"name": "orca-mini 70b", "version": "orca-mini:70b", "category": "Language Model", "rating": 3},
        {"name": "yi 6b", "version": "yi:6b", "category": "Language Model", "rating": 3},
        {"name": "yi 9b", "version": "yi:69b", "category": "Language Model", "rating": 3},
        {"name": "yi 34b", "version": "yi:34b", "category": "Language Model", "rating": 3},
        {"name": "qwen2-math 1.5b", "version": "qwen2-math:1.5b", "category": "Language Model", "rating": 3},
        {"name": "qwen2-math 7b", "version": "qwen2-math:7b", "category": "Language Model", "rating": 3},
        {"name": "qwen2-math 72b", "version": "qwen2-math:72b", "category": "Language Model", "rating": 3},
        {"name": "hermes3 3b", "version": "hermes3:3b", "category": "Language Model", "rating": 3},
        {"name": "hermes3 8b", "version": "hermes3:8b", "category": "Language Model", "rating": 3},
        {"name": "hermes3 70b", "version": "hermes3:70b", "category": "Language Model", "rating": 3},
        {"name": "hermes3 405b", "version": "hermes3:405b", "category": "Language Model", "rating": 3},
        {"name": "phi3.5 3.8b", "version": "phi3.5", "category": "Language Model", "rating": 4},
        {"name": "smollm 125m", "version": "smollm:135m", "category": "Language Model", "rating": 3},
        {"name": "smollm 360m", "version": "smollm:360m", "category": "Language Model", "rating": 3},
        {"name": "smollm 1.7b", "version": "smollm:1.7b", "category": "Language Model", "rating": 3},
        {"name": "nuextract 3.8b", "version": "nuextract", "category": "Language Model", "rating": 3},
        {"name": "firefunction-v2 70b", "version": "firefunction-v2", "category": "Language Model", "rating": 3},
        {"name": "llama3-groq-tool-use 8b", "version": "llama3-groq-tool-use:8b", "category": "Language Model","rating": 3},
        {"name": "llama3-groq-tool-use 70b", "version": "llama3-groq-tool-use:70b", "category": "Language Model","rating": 3},
        {"name": "mathstral 7b", "version": "mathstral", "category": "Language Model", "rating": 3},
        {"name": "codegeex4 9b", "version": "codegeex4", "category": "Language Model", "rating": 3},
        {"name": "glm4 9b", "version": "glm4", "category": "Language Model", "rating": 3},
        {"name": "internlm2 1m", "version": "internlm2:1m", "category": "Language Model", "rating": 3},
        {"name": "internlm2 1.8b", "version": "internlm2:1.8b", "category": "Language Model", "rating": 3},
        {"name": "internlm2 7b", "version": "internlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "internlm2 20b", "version": "internlm2:20b", "category": "Language Model", "rating": 3},
        {"name": "codestral 22b", "version": "codestral", "category": "Language Model", "rating": 4},
        {"name": "granite3.2-vision", "version": "granite3.2-vision", "category": "Vision Tools", "rating": 3},
        {"name": "moondream", "version": "moondream", "category": "Vision Tools", "rating": 3},
        {"name": "llava-llama3", "version": "llava-llama3", "category": "Vision Tools", "rating": 3},
        {"name": "llava-phi3", "version": "llava-phi3", "category": "Vision Tools", "rating": 3},
        {"name": "bakllava", "version": "bakllava", "category": "Vision Tools", "rating": 3}
    ]


class ModelCard(QFrame):
    def __init__(self, model: dict, is_installed: bool, parent=None):
        super().__init__(parent)
        self.model = model
        self.is_installed = is_installed
        self.setup_ui()
        self.setup_shadow()
        self.setMouseTracking(True)

    def setup_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setStyleSheet("""
            QFrame {
                background-color: #3b3f44;
                border-radius: 15px;
                padding: 15px;
            }
            QLabel {
                background: transparent;
            }
        """)
        layout = QVBoxLayout()
        layout.setSpacing(8)

        # Name
        self.name_label = QLabel(self.model["name"])
        self.name_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.name_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.name_label)

        # Kategorie als Badge
        self.category_label = QLabel(self.model["category"])
        self.category_label.setFont(QFont("Segoe UI", 10))
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.category_label.setStyleSheet("""
            background-color: #e67e22;
            color: white;
            padding: 4px 10px;
            border-radius: 10px;
            max-width: 140px;
        """)
        layout.addWidget(self.category_label)

        # Sternebewertung
        stars = "★" * self.model["rating"] + "☆" * (5 - self.model["rating"])
        self.rating_label = QLabel(stars)
        self.rating_label.setFont(QFont("Segoe UI", 16))
        self.rating_label.setStyleSheet("color: #f1c40f;")
        layout.addWidget(self.rating_label)

        # Version
        self.version_label = QLabel(f"Name: {self.model['version']}")
        self.version_label.setFont(QFont("Segoe UI", 12))
        self.version_label.setStyleSheet("color: #bdc3c7;")
        layout.addWidget(self.version_label)

        # Installationsstatus
        status_text = "Installed" if self.is_installed else "Not Installed"
        status_color = "#27ae60" if self.is_installed else "#e74c3c"
        self.status_label = QLabel(status_text)
        self.status_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.status_label.setStyleSheet(f"color: {status_color};")
        layout.addWidget(self.status_label)

        layout.addStretch()
        self.setLayout(layout)

    def setup_shadow(self):
        # Initialer Schatteneffekt
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, event):
        # Animiert den Schatten beim Hover
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(25)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Rückkehr zum ursprünglichen Schatten
        self.anim = QPropertyAnimation(self.shadow, b"blurRadius")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(15)
        self.anim.start()
        super().leaveEvent(event)


class ModelShop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Model Shop")
        self.setGeometry(100, 100, 1500, 800)
        self.set_dark_mode()
        self.set_background_gradient()

        # Optional: Icon setzen, falls vorhanden
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = os.path.join(f"C:/Users/{user}/PycharmProjects/MAVIS/icons", "mavis-logo.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout(self)
        header = QLabel("Welcome to MAVIS Model Shop")
        header.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        header.setStyleSheet("color: #ecf0f1; padding: 20px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # ScrollArea konfigurieren
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
        self.grid_layout = QGridLayout(self.content_widget)
        self.grid_layout.setSpacing(25)
        self.grid_layout.setContentsMargins(30, 30, 30, 30)
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
        # Setzt einen dezenten vertikalen Farbverlauf als Hintergrund
        self.setStyleSheet("""
            QWidget { 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #000000);
            }
        """)

    def load_models(self):
        models = fetch_models()
        with ThreadPoolExecutor() as executor:
            futures = {model["name"]: executor.submit(check_model_with_ollama, model["version"]) for model in models}
            for index, model in enumerate(models):
                is_installed = futures[model["name"].strip()].result()
                card = ModelCard(model, is_installed)
                # Platziere die Karten in einem Grid (z.B. 3 Spalten pro Zeile)
                self.grid_layout.addWidget(card, index // 4, index % 4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelShop()
    window.show()
    sys.exit(app.exec())
