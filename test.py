# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QPushButton, QScrollArea, QGridLayout
# from PyQt5.QtCore import Qt, pyqtSignal

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Resizable Frames with Scroll Area')
#         self.setGeometry(100, 100, 800, 600)

#         main_layout = QVBoxLayout(self)

#         scroll_area = QScrollArea(self)
#         scroll_area.setWidgetResizable(True)

#         self.content_widget = QWidget()
#         self.content_layout = QGridLayout(self.content_widget)
#         self.content_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Đặt về đầu giống flex-start
#         self.content_layout.setHorizontalSpacing(10)  # Khoảng cách giữa các frame
#         self.content_layout.setVerticalSpacing(10)  # Khoảng cách giữa các dòng

#         self.frames = []

#         scroll_area.setWidget(self.content_widget)

#         main_layout.addWidget(scroll_area)

#         add_button = QPushButton('Add Frame', self)
#         add_button.clicked.connect(self.addFrame)
#         main_layout.addWidget(add_button)

#         self.setLayout(main_layout)

#     def createFrame(self):
#         frame = ClickableFrame(self)  # Sử dụng lớp ClickableFrame thay vì QFrame
#         frame.setStyleSheet('background-color: red;')
#         frame.setFixedWidth(350)
#         frame.setFixedHeight(400)
#         frame.clicked.connect(self.onFrameClicked)
#         return frame

#     def addFrameToLayout(self, frame):
#         if frame is not None:
#             total_frames = len(self.frames)
#             num_cols = 5

#             # Tính toán số dòng dựa trên số lượng frame hiện tại
#             num_rows = (total_frames + 1) // num_cols
#             if (total_frames + 1) % num_cols != 0:
#                 num_rows += 1

#             # Tìm vị trí trống để thêm frame
#             for row in range(num_rows):
#                 for col in range(num_cols):
#                     if (row * num_cols + col) < total_frames:
#                         continue  # Ô đã có frame, bỏ qua
#                     else:
#                         self.content_layout.addWidget(frame, row, col)
#                         return  # Đã thêm frame, kết thúc hàm

#             # Nếu không có ô trống, thêm frame ở cuối dòng hiện tại
#             self.content_layout.addWidget(frame, num_rows - 1, num_cols - 1)

#     def addFrame(self):
#         new_frame = self.createFrame()
#         self.frames.append(new_frame)
#         self.addFrameToLayout(new_frame)

#     def onFrameClicked(self):
#         sender = self.sender()
#         if sender in self.frames:
#             # Thay đổi màu của frame được click
#             sender.setStyleSheet('background-color: blue;')

# # Lớp ClickableFrame mở rộng từ QFrame và thêm một tín hiệu clicked
# class ClickableFrame(QFrame):
#     clicked = pyqtSignal()

#     def mousePressEvent(self, event):
#         self.clicked.emit()
#         super().mousePressEvent(event)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Confirmation Dialog')

        self.btn_delete = QPushButton('Delete', self)
        self.btn_delete.setGeometry(100, 100, 100, 30)
        self.btn_delete.clicked.connect(self.showConfirmation)

    def showConfirmation(self):
        # Create a QMessageBox with Yes and No buttons
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # Check the user's response
        if reply == QMessageBox.Yes:
            print('Deleting...')
            # Add your delete logic here
        else:
            print('Deletion canceled')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()



































# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QPushButton, QScrollArea, QGridLayout
# from PyQt5.QtCore import Qt
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Resizable Frames with Scroll Area')
#         self.setGeometry(100, 100, 800, 600)

#         main_layout = QVBoxLayout(self)

#         scroll_area = QScrollArea(self)
#         scroll_area.setWidgetResizable(True)

#         self.content_widget = QWidget()
#         self.content_layout = QGridLayout(self.content_widget)
#         self.content_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Đặt về đầu giống flex-start
#         self.content_layout.setHorizontalSpacing(10)  # Khoảng cách giữa các frame
#         self.content_layout.setVerticalSpacing(10)  # Khoảng cách giữa các dòng

#         self.frames = []


#         scroll_area.setWidget(self.content_widget)

#         main_layout.addWidget(scroll_area)

#         add_button = QPushButton('Add Frame', self)
#         add_button.clicked.connect(self.addFrame)
#         main_layout.addWidget(add_button)

#         self.setLayout(main_layout)

#     def createFrame(self):
#         frame = QFrame(self)
#         frame.setStyleSheet('background-color: red;')
#         frame.setFixedWidth(350)
#         frame.setFixedHeight(400)
#         return frame

#     def addFrameToLayout(self, frame):
#         row, col = divmod(len(self.frames), 5)  # Tính toán dòng và cột cho frame mới
#         self.content_layout.addWidget(frame, row, col)

#     def addFrame(self):
#         new_frame = self.createFrame()
#         self.frames.append(new_frame)
#         self.addFrameToLayout(new_frame)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
