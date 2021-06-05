from qr import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import sys
import qrcode
from PIL import ImageQt
import os


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("QR Code Generator")
        self.setWindowIcon(QtGui.QIcon("icon/qr.png"))

        self.ui.btn_qr.clicked.connect(self.generate_qr)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_save.clicked.connect(self.save_qr)

    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2,
        )
        txt = self.ui.txt_url.text()

        if txt == "":
            self.ui.lbl_qr.setGeometry(110, 160, 220, 40)
            self.ui.lbl_qr.setText("Alert: Please Enter URL!!")
        else:
            # txt = self.make_URL_shorter(txt)
            qr.add_data(txt)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            image = ImageQt.ImageQt(img)
            pix = QPixmap.fromImage(image)

            self.resize(420, 420)

            self.ui.lbl_qr.setGeometry(90, 150, 250, 250)
            self.ui.lbl_qr.setPixmap(pix)

    def clear(self):
        self.ui.lbl_qr.clear()
        self.ui.txt_url.clear()
        self.resize(420, 200)

    def save_qr(self):
        current_dir = os.getcwd()
        file_name = "qr"

        if file_name:
            self.ui.lbl_qr.pixmap().save(os.path.join(current_dir, file_name + ".png"))
            msg = QMessageBox()
            msg.setWindowTitle("QR saved")

            msg.setFixedSize(400, 200)
            msg.setText("File saved at: " + current_dir)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon("icon/qr.png"))

            x = msg.exec_()


    # @staticmethod
    # def make_URL_shorter(url):
    #     short_url = pyshorteners.Shortener().tinyurl.short(url)
    #     return short_url


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()
