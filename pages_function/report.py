import logging
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.pages.report_ui import Ui_MainWindow
import main as main
from PyQt5.QtCore import Qt,QDateTime, QTimer
from pages_function.report_class import report_class
from pages_function.report_home import report_home
from pages_function.report_source import report_source
from pages_function.report_time_range import report_time_range
from pages_function.report_person_attributes import report_person_attributes
from pages_function.report_dashboard import report_dashboard
from pages_function.report_orders import report_orders
from pages_function.report_products import report_products
from pages_function.report_customers import report_customers
from pages_function.report_color import report_color
from pages_function.report_size import report_size
from pages_function.report_speed import report_speed
from pages_function.report_dwell import report_dwell
from pages_function.report_direction import report_direciton
from pages_function.report_proximity import report_proximity
from pages_function.report_appearance_similarity import report_appearance_similarity
from pages_function.report_face_recognition import report_face_recognition
from pages_function.report_license_plate_reco import report_license_plate_reco
app = QApplication(sys.argv)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.ui.exit_btn_1.clicked.connect(self.exit_btn)
        self.ui.exit_btn_2.clicked.connect(self.exit_btn)

        self.report_home = report_home(self)

        self.report_dashboard = report_dashboard(self)

        self.report_orders = report_orders(self)

        self.report_products = report_products(self)

        self.report_customers = report_customers(self)

        self.report_source = report_source(self)

        self.report_time_range = report_time_range(self)

        self.report_class = report_class(self)

        self.report_person_attributes = report_person_attributes(self)

        self.report_color = report_color(self)
        
        self.report_size = report_size(self)

        self.report_speed = report_speed(self)

        self.report_dwell = report_dwell(self)

        self.report_direction = report_direciton(self)

        self.report_proximity = report_proximity(self)

        self.report_appearance_similarity = report_appearance_similarity(self)

        self.report_face_recognition = report_face_recognition(self)

        self.report_license_plate_reco = report_license_plate_reco(self)
        
    #     self.setWindowFlag(Qt.WindowTitleHint, False)
    #     self.setWindowFlag(Qt.WindowSystemMenuHint, False)
    #     self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
    #     self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
    #     self.setWindowFlag(Qt.WindowCloseButtonHint, False)

    #     # Thêm chức năng thu nhỏ, phóng to và tắt
    #     minimize_button = QPushButton('-', self)
    #     minimize_button.clicked.connect(self.showMinimized)

    #     maximize_button = QPushButton('[]', self)
    #     maximize_button.clicked.connect(self.toggleMaximized)

    #     close_button = QPushButton('X', self)
    #     close_button.clicked.connect(self.close)
    # def toggleMaximized(self):
    #     if self.isMaximized():
    #         self.showNormal()
    #     else:
    #         self.showMaximized()
    def exit_btn(self):
        try:
            global ui
            ui = main.main()
            self.hide()
        except Exception as e:
            logging.error("button_report %s", str(e))


    ## Function for searching
    def on_search_btn_clicked(self):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton)
        self.ui.stackedWidget.setCurrentIndex(len(btn_list)-1) 
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton)
        self.ui.stackedWidget.setCurrentIndex(len(btn_list)) 

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        btn_list_number = self.ui.icon_only_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [len(btn_list_number)-1,len(btn_list_number)]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_source_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_source_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_time_range_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_time_range_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_class_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_class_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_person_attributes_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_person_attributes_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_color_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def on_color_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def on_size_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def on_size_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(10)       

    def on_speed_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def on_speed_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(11)     

    def on_dwell_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def on_dwell_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(12)  

    def on_direction_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def on_direction_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(13)  

    def on_proximity_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(14)

    def on_proximity_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(14)  

    def on_appearance_similarity_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(15)

    def on_appearance_similarity_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(15)  

    def on_face_recognition_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(16)

    def on_face_recognition_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(16)  

    def on_License_plate_reco_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(17)

    def on_License_plate_reco_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(17)  
def main_report():
    global ui
    ui = MainWindow()
    ui.show()
if __name__ == "__main__":
    try:
        ## loading style file
        # with open("style.qss", "r") as style_file:
        #     style_str = style_file.read()
        # app.setStyleSheet(style_str)

        ## loading style file, Example 2
        style_file = QFile("ui/pages/style.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())
        main_report()
    except Exception as e:
        # Ghi lại lỗi nếu có
        logging.error("__name__ == __main__ : Loi chuong trinh report: %s", str(e))
    sys.exit(app.exec())



