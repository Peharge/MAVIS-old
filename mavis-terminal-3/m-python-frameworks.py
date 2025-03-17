import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel, QScrollArea, \
    QTextEdit
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


def get_installed_frameworks():
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_list_cmd = f"{env_path}\\Scripts\\python.exe -m pip list"

    try:
        result = subprocess.run(pip_list_cmd, shell=True, capture_output=True, text=True, check=True)
        lines = result.stdout.split('\n')[2:]
        frameworks = {}

        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                frameworks[parts[0]] = parts[1]

        return frameworks
    except Exception as e:
        return {"Error": str(e)}


def get_framework_details(name):
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_show_cmd = f"{env_path}\\Scripts\\python.exe -m pip show {name}"

    try:
        result = subprocess.run(pip_show_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving details: {str(e)}"


class FrameworkViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Framework Viewer")
        self.setGeometry(100, 100, 1000, 800)

        self.set_dark_mode()

        layout = QVBoxLayout()

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

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Framework", "Version"])
        self.tree.itemExpanded.connect(self.load_details_on_expand)
        layout.addWidget(self.tree)

        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.load_frameworks()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_frameworks(self):
        frameworks = get_installed_frameworks()
        self.tree.clear()

        for name, version in frameworks.items():
            item = QTreeWidgetItem([name, version])
            item.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy.ShowIndicator)
            self.tree.addTopLevelItem(item)

        self.status_label.setText("Frameworks loaded successfully.")

    def load_details_on_expand(self, item):
        if item.childCount() == 0:  # Load details only if not already loaded
            details_text = get_framework_details(item.text(0))
            details_widget = QTextEdit()
            details_widget.setPlainText(details_text)
            details_widget.setReadOnly(True)
            details_widget.setStyleSheet("background-color: sqrt(40, 40, 40); color: white; border: none; padding: 5px;")
            details_widget.setFixedHeight(200)

            container = QTreeWidgetItem()
            item.addChild(container)
            self.tree.setItemWidget(container, 0, details_widget)
            item.setExpanded(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 66% of the width for the 'Framework' column
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.66))  # First column (Framework) 66% of the window width
        self.tree.setColumnWidth(1, int(width * 0.30))  # Second column (Version) 34% of the window width


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrameworkViewer()
    window.show()
    sys.exit(app.exec())
