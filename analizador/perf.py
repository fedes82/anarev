#ver perf.py
# https://stackoverflow.com/questions/35810346/pyqt5-popup-window
# https://stackoverflow.com/questions/33945911/close-and-get-data-from-a-custom-dialog-pyqt5


from PyQt5.QtCore import Qt
##PARA EL GUI
from PyQt5 import QtGui, QtWidgets

import sys
import json

import perfiles5

class ProfilesWindow(QtWidgets.QMainWindow, perfiles5.Ui_Dialog):
    
    def __init__(self,parent=None):
        super().__init__()
       # self.setupUi()
    #connects
        self.btnDelCat.clicked.connect(self.btn_DelCat)
        self.btnImpPerfil.clicked.connect(self.btn_ImpPerfil)
        self.btnAddParam.clicked.connect(self.btn_AddParam)
        self.btnDelParam.clicked.connect(self.btn_DelParam)
        self.btnAddCat.clicked.connect(self.btn_AddCat)
        self.btnNuevoPerfil.clicked.connect(self.btn_NuevoPerfil)
        self.btnExpPerfil.clicked.connect(self.btn_ExpPerfil)
    
    #cargo el default
        self.cargar_diccionario('perfiles/default.json')
        self.actualizar_todo()
        self.lblPerfil.setObjectName("lblPerfil")
        self.lnNombreParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCodeParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCategorias
        self.lstCategorias = QtWidgets.QListView(self.groupBox_2)
        self.combPerfil = QtWidgets.QComboBox(Dialog)
        
#        self.buttonBox.accepted.connect(Dialog.accept)
#        self.buttonBox.rejected.connect(Dialog.reject)
    
    def btn_AddParam(self):
        parametro = str(self.lstParametros.currentItem().text()[0])
        nombre = self.lstParametros.currentItem().text()
        categoria = str(self.combValorParam.currentText())
        
        
    def cargar_diccionario(self,archivo):
        with open('archivo','r') as file:
            self.dict_parametros = json.loads(file.read())
        
    def cargar_parametros(self):
        self.lstParametros.clear()
        for key in dict_parametros:
            self.lstParametros.addItem(key)
    
    def crear_Arbol(self,dictionary):
        arbol=''
        for key in dictionary:
            arbol += key +' - Cod: '+'\n'#, dictionary[key][0] +'\n'
            for item in dictionary[key][1]:
                arbol += '\t-- ' + item + '\n'
        print(arbol)
        return arbol
        
    def actualizar_arbol(self):
        self.arbol = crear_Arbol(self.dict_parametros)
        self.lblPerfil.setText(self.arbol)
        
    def actualizar_todo(self):
        self.cargar_parametros()
        self.actualizar_arbol()
def main():
   # global app
    app = QtWidgets.QApplication(sys.argv)
    form = ProfilesWindow()
    form.showMaximized()
    print( form.size())
    app.exec_()

if __name__ == '__main__':
    main()
    