from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

class ServerManagerDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Менеджер серверов")
        self.resize(450, 300)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Список серверов:"))

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)