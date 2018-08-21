#ver perf.py
# https://stackoverflow.com/questions/35810346/pyqt5-popup-window
# https://stackoverflow.com/questions/33945911/close-and-get-data-from-a-custom-dialog-pyqt5


from PyQt5.QtCore import Qt
##PARA EL GUI
from PyQt5 import QtGui, QtWidgets

import sys

import perfiles5

class ProfilesWindow(QtWidgets.QMainWindow, perfiles5.Ui_Dialog):
    
    def __init__(self,parent=None):
        super().__init__()
       # self.setupUi()
    #connects
    
    
    
    def cargar_parametros(self):
        self.lstParametros.clear()
        for key in dict_parametros:
            self.lstParametros.addItem(key)
        
def main():
   # global app
    app = QtWidgets.QApplication(sys.argv)
    form = ProfilesWindow()
    form.showMaximized()
    print( form.size())
    app.exec_()

if __name__ == '__main__':
    main()
    