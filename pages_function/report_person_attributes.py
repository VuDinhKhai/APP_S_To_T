from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QDateTime, QTimer
from ui.pages.report_ui import Ui_MainWindow
class report_person_attributes():
    def __init__(self, main_window):
        # Receive the MainWindow instance as a parameter
        self.main_window = main_window
        self.ui = main_window.ui  # Use the UI instance from MainWindow
        # self.ui = Ui_MainWindow()
        self.update_time()
        timer = QTimer(self.main_window)
        timer.timeout.connect(self.update_time)
        timer.start(1000)


    def update_time(self):
        # Lấy thời gian hiện tại và thời gian sau một khoảng cố định (ví dụ: 60 phút)
        current_date_time = QDateTime.currentDateTime()
        future_date_time = current_date_time.addSecs(60 * 60)

        # Chuyển đổi thời gian thành chuỗi với định dạng yêu cầu
        current_time_string = current_date_time.toString("M/d/yyyy hh:mm:ss")
        future_time_string = future_date_time.toString("M/d/yyyy hh:mm:ss")

        # Tạo chuỗi kết quả
        result_string = f"{current_time_string} - {future_time_string}"
        
        # Đặt chuỗi vào QLabel
        self.ui.page_person_time_label.setText(result_string)
