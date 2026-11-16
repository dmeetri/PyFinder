from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QWidget

from .server_manager import ServerManagerDialog

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PyFinder")
        self.resize(900, 600)

        self.server_window: ServerManagerDialog | None = None

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self._build_menu_bar()

    def _build_menu_bar(self) -> None:
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&Файл")

        servers_action = QAction("Менеджер серверов", self)
        servers_action.setShortcut("Ctrl+S")
        servers_action.triggered.connect(self.open_server_manager)
        file_menu.addAction(servers_action)

        file_menu.addSeparator()

        exit_action = QAction("Выход", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_server_manager(self) -> None:
        if self.server_window is None:
            self.server_window = ServerManagerDialog(self)

        self.server_window.show()
        self.server_window.raise_()
        self.server_window.activateWindow()
