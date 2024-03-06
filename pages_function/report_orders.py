from ui.pages.report_ui import Ui_MainWindow
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import QDateTime, QTimer
import sys

class report_orders():
    def __init__(self, main_window):
        # Receive the MainWindow instance as a parameter
        self.main_window = main_window
        self.ui = main_window.ui  # Use the UI instance from MainWindow
        # self.ui = Ui_MainWindow()