from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
import main as main
class FrameFactory(QFrame):
    def __init__(self, parent=None):
        super(FrameFactory, self).__init__(parent)
        
    def createFrame(title="", Content=" ", Time_created="", Time_modified=""):
        frame = ClickableFrame()
        frame.setFixedSize(250, 400)
        frame.setStyleSheet(
            """
            QFrame {
                background-color: rgb(54, 55, 60);
                border-radius: 5px;
                border: 1px solid transparent;
            }
            QFrame:hover {
                border: 1px solid #71c5e8;
            }
            """
        )

        layout = QVBoxLayout(frame)

        imageMain = QLabel(frame)
        imageMain.setMaximumSize(16777215, 150)
        imageMain.setStyleSheet("image: url(:/newPrefix/setting.png);")
        imageMain.setText("")
        imageMain.setScaledContents(True)
        layout.addWidget(imageMain)

        line = QFrame(frame)
        line.setStyleSheet("")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.setSpacing(0)

        imageChild_1 = QLabel(frame)
        imageChild_1.setMaximumSize(50, 50)
        imageChild_1.setStyleSheet("image: url(:/newPrefix/setting.png);")
        imageChild_1.setText("")
        imageChild_1.setScaledContents(True)
        horizontalLayout.addWidget(imageChild_1)

        imageChild_2 = QLabel(frame)
        imageChild_2.setMaximumSize(50, 50)
        imageChild_2.setStyleSheet("image: url(:/newPrefix/setting.png);")
        imageChild_2.setText("")
        imageChild_2.setScaledContents(True)
        horizontalLayout.addWidget(imageChild_2)

        imageChild_3 = QLabel(frame)
        imageChild_3.setMaximumSize(50, 50)
        imageChild_3.setStyleSheet("image: url(:/newPrefix/setting.png);")
        imageChild_3.setText("")
        imageChild_3.setScaledContents(True)
        horizontalLayout.addWidget(imageChild_3)

        layout.addLayout(horizontalLayout)

        line_3 = QFrame(frame)
        line_3.setFrameShape(QFrame.HLine)
        line_3.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line_3)

        title_text = QLabel(frame)
        title_text.setMaximumSize(16777215, 30)
        title_text.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(title_text)

        time_created = QLabel(frame)
        time_created.setMaximumSize(16777215, 30)
        time_created.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(time_created)

        content = QLabel(frame)
        content.setFont(QtGui.QFont("Arial", 10))
        content.setLayoutDirection(Qt.LeftToRight)
        content.setStyleSheet("color: rgb(255, 255, 255);")
        content.setScaledContents(True)
        content.setWordWrap(True)
        layout.addWidget(content)

        line_2 = QFrame(frame)
        line_2.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        line_2.setFrameShape(QFrame.HLine)
        line_2.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line_2)

        frame_2 = QFrame(frame)
        frame_2.setMaximumSize(16777215, 20)
        frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        frame_2.setFrameShape(QFrame.StyledPanel)
        frame_2.setFrameShadow(QFrame.Raised)

        horizontalLayout_3 = QHBoxLayout(frame_2)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.setSpacing(0)

        time_modified = QLabel(frame_2)
        time_modified.setFont(QtGui.QFont("Arial" ,9))
        time_modified.setStyleSheet("background-color: transparent; color: white;")
        horizontalLayout_3.addWidget(time_modified)

        button_edit = QPushButton(frame_2)
        button_edit.setMaximumSize(30, 30)
        button_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button_edit.setStyleSheet(
            u"QPushButton {\n"
            "                background-color: transparent;\n"
            "                color: white;\n"
            "                border: none;\n"
            "                padding: 5px;\n"
            "            }\n"
            "            QPushButton:hover {\n"
            "                background-color: rgba(255, 255, 255, 30);\n"
            "            }"
        )
        button_edit.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_edit.setIcon(icon)
        button_edit.setIconSize(QtCore.QSize(27, 21))
        button_edit.clicked.connect(frame.show_edit)
        horizontalLayout_3.addWidget(button_edit)

        button_delete = QPushButton(frame_2)
        button_delete.setMaximumSize(30, 30)
        button_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button_delete.setText("")
        button_delete.setStyleSheet(
            u"QPushButton {\n"
            "                background-color: transparent;\n"
            "                color: white;\n"
            "                border: none;\n"
            "                padding: 5px;\n"
            "            }\n"
            "            QPushButton:hover {\n"
            "                background-color: rgba(255, 255, 255, 30);\n"
            "            }"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_delete.setIcon(icon1)
        button_delete.setIconSize(QtCore.QSize(26, 26))
        button_delete.clicked.connect(frame.show_delete)
        horizontalLayout_3.addWidget(button_delete)

        layout.addWidget(frame_2)

        title_text.setText(title)
        time_created.setText(Time_created)
        content.setText(Content)
        time_modified.setText(Time_modified)
        
        return frame
    def showConfirmation(self):
        reply = QMessageBox.question(self , 'Confirmation', 'Are you sure you want to delete?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('Deleting...')
            # Thêm logic xóa ở đây
        else:
            print('Deletion canceled')    

class ClickableFrame(QFrame):
    clicked = pyqtSignal()
    deleteClicked = pyqtSignal()
    editClicked = pyqtSignal()

    def __init__(self, parent=None):
        super(ClickableFrame, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super(ClickableFrame, self).mousePressEvent(event)

    def show_delete(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('Deleting...')
        else:
            print('Deletion canceled')

    def show_edit(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Ayou want to edit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('Deleting...')
            # Thêm logic xóa ở đây
        else:
            print('Deletion canceled')

