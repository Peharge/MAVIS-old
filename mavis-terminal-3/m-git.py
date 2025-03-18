import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel, QScrollArea
from PyQt6.QtGui import QPalette, QColor, QIcon


def get_git_commits(repo_path):
    os.chdir(repo_path)
    try:
        # Lokale Commits abrufen
        local_commits = subprocess.check_output(["git", "log", "--pretty=format:%H %h %s"], text=True).split("\n")

        # Sicheren Hauptbranch ermitteln
        branches = subprocess.check_output(["git", "ls-remote", "--heads", "origin"], text=True).split("\n")
        main_branch = None
        for branch in branches:
            if "refs/heads/main" in branch:
                main_branch = "origin/main"
                break
            elif "refs/heads/master" in branch:
                main_branch = "origin/master"
                break

        if not main_branch:
            return []  # Kein Main-Branch gefunden

        # Remote-Commits abrufen
        remote_commits = subprocess.check_output(["git", "log", main_branch, "--pretty=format:%H"], text=True).split(
            "\n")
        remote_hashes = set(remote_commits)

        commits = []
        for commit in local_commits:
            if commit:
                full_hash, short_hash, message = commit.split(" ", 2)
                color = "red" if full_hash not in remote_hashes else "green"
                commits.append((short_hash, message, color))

        return commits
    except subprocess.CalledProcessError:
        return []


class CommitExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Commit Explorer")
        self.setGeometry(100, 100, 1000, 800)
        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/PycharmProjects/MAVIS"

        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Commit Hash", "Message", "Status"])
        layout.addWidget(self.tree)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Dies wird jetzt auf die Instanz von QApplication angewendet
        app.setStyleSheet("""
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

        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.load_commits()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_commits(self):
        self.tree.clear()
        commits = get_git_commits(self.repo_path)
        for short_hash, message, color in commits:
            item = QTreeWidgetItem([short_hash, message, "Not Pulled" if color == "red" else "Pulled"])
            item.setForeground(2, QColor(color))
            self.tree.addTopLevelItem(item)

        self.status_label.setText("Commits loaded successfully.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommitExplorer()
    window.show()
    sys.exit(app.exec())
