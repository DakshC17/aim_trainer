import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5.QtCore import Qt

class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProLabs Launcher")
        self.showFullScreen()
        self.setup_ui()

    def setup_ui(self):
        # Gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#0f2027"))
        gradient.setColorAt(0.5, QColor("#203a43"))
        gradient.setColorAt(1.0, QColor("#2c5364"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # Main vertical layout
        layout = QVBoxLayout()
        layout.setSpacing(40)
        layout.setAlignment(Qt.AlignCenter)

        # Game title
        title = QLabel("🔥 ProLabs 🔥")
        title.setFont(QFont("Verdana", 48, QFont.Bold))
        title.setStyleSheet("""
            color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                   stop:0 #00f0ff, stop:1 #ff00ff);
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Play Button
        play_button = QPushButton("▶  Play")
        play_button.setFixedSize(220, 70)
        play_button.setFont(QFont("Segoe UI", 18))
        play_button.setStyleSheet("""
            QPushButton {
                background-color: #00c9a7;
                color: white;
                border-radius: 30px;
                border: 2px solid #00fff0;
            }
            QPushButton:hover {
                background-color: #00e6bf;
                color: #000;
            }
        """)
        play_button.clicked.connect(self.launch_game)
        layout.addWidget(play_button, alignment=Qt.AlignCenter)

        # Exit Button
        exit_button = QPushButton("✖  Exit")
        exit_button.setFixedSize(200, 70)
        exit_button.setFont(QFont("Segoe UI", 16))
        exit_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 25px;
                border: 2px solid #ff9999;
            }
            QPushButton:hover {
                background-color: #ff6f61;
                color: #000;
            }
        """)
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def launch_game(self):
        subprocess.Popen([sys.executable, "/home/dakshchoudhary/Desktop/projects/aim_trainer/main.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = GameLauncher()
    launcher.show()
    sys.exit(app.exec_())
