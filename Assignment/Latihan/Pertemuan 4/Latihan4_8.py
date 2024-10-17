from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore
class MyWindow(QMainWindow):
    def __init_(self):
        super()._init__()
        self.label = QLabel(self)
        self.label.setText("Labell")
        self.label.move(200, 8)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry (0,0, 300, 300)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry()  # cek ukuran main window app kita
        cwc = QDesktopWidget().availableGeometry().center() # pada screen saya: (682,363)
        #print(cwc)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(500,500) # agar tidak bisa di-resizel icon maximize juga akan otomatis hilang
        # self.setiwindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()