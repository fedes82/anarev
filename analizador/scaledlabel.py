from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore

#https://stackoverflow.com/questions/21041941/how-to-autoresize-qlabel-pixmap-keeping-ratio-without-using-classes
# Lo saque de aca


IMG_DEFAULT = 'img_default/ok.png'
#IMG_DEFAULT = 'img_default/imgDefault.jpg'


class ScaledLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self)
        self.setPixmap(QtGui.QPixmap(IMG_DEFAULT))
        self._pixmap = QtGui.QPixmap(self.pixmap())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def resizeEvent(self, event):
        self.setPixmap(self._pixmap.scaled(
            self.width(), self.height(),
            QtCore.Qt.KeepAspectRatio))
    
    def actualizar(self,pix):
        self.setPixmap(QtGui.QPixmap(pix))
        self._pixmap = QtGui.QPixmap(self.pixmap())
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(self._pixmap.scaled(
            self.width(), self.height(),
            QtCore.Qt.KeepAspectRatio))
