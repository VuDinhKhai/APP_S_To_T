import logging
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from ui.pages.create_new_case_ui import Ui_Form
from datetime import datetime
from PyQt5.QtCore import QDateTime, Qt


app = QApplication(sys.argv)

class create_new_case(QWidget):
    def __init__(self,main_window):
        super(create_new_case, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setMaximumSize(984, 619)
        self.ui.Button_create.clicked.connect(self.button_create)
        self.main_window = main_window
        self.ui.Button_cancel.clicked.connect(self.button_cancel)

    def button_create(self):
        text_Title = self.ui.text_Title.toPlainText()
        text_content = self.ui.text_description.toPlainText()
        dateEdit = self.ui.dateEdit.date()
        dateEdit_string = dateEdit.toString("yyyy-MM-dd")
        timeEdit = self.ui.timeEdit.time()
        timeEdit_string = timeEdit.toString("hh:mm:ss")
        Time_created = f"Ngày tạo: {dateEdit_string} {timeEdit_string}"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Time_modifed = current_time

        self.main_window.addFrame(text_Title,text_content,Time_created,Time_modifed)
        self.main_window.setEnabled(True)
        ui.hide()
    def button_cancel(self):
        self.main_window.setEnabled(True)
        ui.hide()
    
    def closeEvent(self, event):
        self.main_window.setEnabled(True)
        event.accept()

def main(main_window):
    global ui
    ui = create_new_case(main_window)
    ui.show()


if __name__ == "__main__":
    try:
        # Thực hiện một thao tác nào đó
        main()
    except Exception as e:
        # Ghi lại lỗi nếu có
        logging.error("__name__ == __main__ : Loi chuong trinh: %s", str(e))
    sys.exit(app.exec_())