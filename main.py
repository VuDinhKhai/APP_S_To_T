import logging
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QWidget, QGridLayout, QFrame, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QPushButton, QScrollArea, QGridLayout
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,pyqtSignal
from ui.main_window import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import pages_function.create_new_case as create_new_case
import pages_function.report as report
import pages_function.infomation_in_page_main as infomation_in_page_main
import sys
app = QApplication(sys.argv)    

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setMinimumSize(screen.width(), screen.height())

        ## Get all the objects in windows
        ## =======================================================================================================
        self.main_btn = self.ui.Button_pageMain
        self.report_btn = self.ui.Button_Report
        self.add_btn = self.ui.Button_Add
        self.setting_btn = self.ui.Button_Setting
        self.search_btn = self.ui.Button_Search
        self.create_btn = self.ui.Button_Create

        self.frames = []
        self.create_btn.clicked.connect(self.button_create)
        self.ui.content_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Đặt về đầu giống flex-start
        self.ui.scrollArea.setWidget(self.ui.content_widget)
        self.ui.Button_pageMain.clicked.connect(self.button_pagemain)
        self.report_btn.clicked.connect(self.button_report)

    def button_report(self):
        try:
            global ui
            ui = report.main_report()
            self.hide()
        except Exception as e:
            logging.error("button_report %s", str(e))
    def button_pagemain(self):
        print(self.frames)
    def button_create(self):
        try:
            global ui
            ui = create_new_case.main(self)
            self.setEnabled(False)
        except Exception as e:
            logging.error("button_create %s", str(e))

    def addFrame(self,title= "",Content = " ",Time_created  = " ", Time_modifed = "" ):
        new_frame = self.createFrame(title,Content,Time_created,Time_modifed)
        self.frames.append(new_frame)
        self.addFrameToLayout(new_frame)

    def createFrame(self, title="", Content=" ", Time_created="", Time_modified=""):
        self.clickable_frame = infomation_in_page_main.FrameFactory.createFrame(title=title, Content=Content, Time_created=Time_created, Time_modified=Time_modified)
        # self.clickable_frame.clicked.connect(self.onFrameClicked)
        return self.clickable_frame



    def addFrameToLayout(self, frame):
        if frame is not None:
            # Tính toán vị trí hàng và cột mới
            row = (len(self.frames)-1) // 7
            col = (len(self.frames)-1) % 7

            # Kiểm tra nếu cần thêm dòng mới
            if col == 0:
                self.ui.content_layout.addWidget(frame, row, 0)
            # Thêm frame vào layout
            self.ui.content_layout.addWidget(frame, row, col)

    def onFrameClicked(self):
        sender = self.sender()
        if sender in self.frames:
            print(sender)
            # Loại bỏ frame khi click
            self.removeFrame(sender)
            # Cập nhật lại layout
            # self.updateLayout()

    def removeFrame(self, frame):
        if frame in self.frames:
            self.frames.remove(frame)
            frame.deleteLater() # Gỡ bỏ frame khỏi parent để xóa nó

def main():
    global ui
    ui = MyWindow()
    ui.show()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('main', str(e))
    sys.exit(app.exec())
