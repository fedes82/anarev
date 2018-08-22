#ver perf.py
# https://stackoverflow.com/questions/35810346/pyqt5-popup-window
# https://stackoverflow.com/questions/33945911/close-and-get-data-from-a-custom-dialog-pyqt5

#este esta piola
#https://stackoverflow.com/questions/30080927/pop-up-dialog-from-one-button-on-the-main-window-pyqt5

#from PyQt5.QtCore import Qt
##PARA EL GUI

from PyQt5 import QtGui, QtWidgets, QtCore

import sys
import json
import pprint
#import perfiles5

#class ProfilesWindow(QtWidgets.QMainWindow, perfiles5.Ui_Dialog):
    
#    def __init__(self,parent=None):

class MyWindow(QtWidgets.QDialog):
    """Los perfiles son diccionarios el, default es
    dict_parametros = {'Exudacion':[False,['A','M','B']],'Bacheo':[False,['S','P','R']],'Fisuras':[True,['1','2','3','4','5']]}
    o sea, de la forma { 'Nombre_de_Parametro':['codigo',['categoria1','categoria2'],'valor']}
    """
    def __init__(self, parent=None):
       # global app
        super(MyWindow, self).__init__(parent)
        self.resize(754, 532)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(180, 480, 521, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.combPerfil = QtWidgets.QComboBox(self)
        self.combPerfil.setGeometry(QtCore.QRect(130, 20, 231, 33))
        self.combPerfil.setObjectName("combPerfil")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 30, 56, 17))
        self.label.setObjectName("label")
        self.btnImpPerfil = QtWidgets.QPushButton(self)
        self.btnImpPerfil.setGeometry(QtCore.QRect(500, 50, 131, 27))
        self.btnImpPerfil.setObjectName("btnImpPerfil")
        self.btnExpPerfil = QtWidgets.QPushButton(self)
        self.btnExpPerfil.setGeometry(QtCore.QRect(500, 20, 131, 27))
        self.btnExpPerfil.setObjectName("btnExpPerfil")
        self.lblPerfil = QtWidgets.QTextBrowser(self)
        self.lblPerfil.setGeometry(QtCore.QRect(450, 130, 271, 331))
        self.lblPerfil.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblPerfil.setObjectName("lblPerfil")
        self.btnNuevoPerfil = QtWidgets.QPushButton(self)
        self.btnNuevoPerfil.setGeometry(QtCore.QRect(380, 20, 85, 27))
        self.btnNuevoPerfil.setObjectName("btnNuevoPerfil")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 161, 17))
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 311, 241))
        self.groupBox.setObjectName("groupBox")
        self.lnNombreParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnNombreParam.setGeometry(QtCore.QRect(10, 60, 113, 27))
        self.lnNombreParam.setObjectName("lnNombreParam")
        self.lnCodeParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCodeParam.setGeometry(QtCore.QRect(190, 60, 31, 27))
        self.lnCodeParam.setObjectName("lnCodeParam")
        self.btnAddParam = QtWidgets.QPushButton(self.groupBox)
        self.btnAddParam.setGeometry(QtCore.QRect(240, 60, 41, 27))
        self.btnAddParam.setObjectName("btnAddParam")
        self.btnDelParam = QtWidgets.QPushButton(self.groupBox)
        self.btnDelParam.setGeometry(QtCore.QRect(230, 150, 31, 27))
        self.btnDelParam.setObjectName("btnDelParam")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 320, 341, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lnCategorias = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnCategorias.setGeometry(QtCore.QRect(10, 30, 113, 27))
        self.lnCategorias.setObjectName("lnCategorias")
        self.btnAddCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddCat.setGeometry(QtCore.QRect(130, 30, 31, 27))
        self.btnAddCat.setObjectName("btnAddCat")
        self.btnDelCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDelCat.setGeometry(QtCore.QRect(250, 90, 31, 27))
        self.btnDelCat.setObjectName("btnDelCat")
        self.lstCategorias = QtWidgets.QListWidget(self.groupBox_2)
        self.lstCategorias.setGeometry(QtCore.QRect(10, 70, 221, 101))
        self.lstParametros = QtWidgets.QListWidget(self.groupBox)
        self.lstParametros.setGeometry(QtCore.QRect(10, 100, 191, 121))
        self.lstCategorias.setObjectName("lstCategorias")
        self.lstParametros.setObjectName("lstParametros")
        
        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
       
        
        ###-------------------------------------------------######
                #connects
        self.btnDelCat.clicked.connect(self.btn_DelCat)
        self.btnImpPerfil.clicked.connect(self.btn_ImpPerfil)
        self.btnAddParam.clicked.connect(self.btn_AddParam)
        self.btnDelParam.clicked.connect(self.btn_DelParam)
        self.btnAddCat.clicked.connect(self.btn_AddCat)
        self.btnNuevoPerfil.clicked.connect(self.btn_NuevoPerfil)
        self.btnExpPerfil.clicked.connect(self.btn_ExpPerfil)
        self.lstParametros.currentItemChanged.connect(self.seleccion_parametro)
    #cargo el default

        self.cargar_diccionario('perfiles/default.json')
        self.actualizar_todo()
        self.lstParametros.setCurrentRow(0)
        
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Perfil"))
        self.btnImpPerfil.setText(_translate("Dialog", "Importar Perfil"))
        self.btnExpPerfil.setText(_translate("Dialog", "Exportar Perfil"))
        self.lblPerfil.setText(_translate("Dialog", "TextLabel"))
        self.btnNuevoPerfil.setText(_translate("Dialog", "Nuevo Perfil"))
        self.label_4.setText(_translate("Dialog", "Previsualizacion del perfil"))
        self.groupBox.setTitle(_translate("Dialog", "Parametros"))
        self.btnAddParam.setText(_translate("Dialog", "++"))
        self.btnDelParam.setText(_translate("Dialog", "--"))
        self.groupBox_2.setTitle(_translate("Dialog", "Categorias"))
        self.btnAddCat.setText(_translate("Dialog", "++"))
        self.btnDelCat.setText(_translate("Dialog", "--"))
        


        """
        self.lblPerfil.setObjectName("lblPerfil")
        self.lnNombreParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCodeParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCategorias
        self.lstCategorias = QtWidgets.QListView(self.groupBox_2)
        self.combPerfil = QtWidgets.QComboBox(Dialog)
       """
#        self.buttonBox.accepted.connect(Dialog.accept)
#        self.buttonBox.rejected.connect(Dialog.reject)
    def btn_DelCat(self):
        if self.lstParametros.currentItem():
            actual_param = str(self.lstParametros.currentItem().text())
            if self.lstCategorias.currentItem():
                del self.perfil_Actual[actual_param][1][self.lstCategorias.currentRow()]
                self.lstCategorias.takeItem(self.lstCategorias.currentRow())
                self.actualizar_arbol()
        
    def btn_DelParam(self):
        print('entre a del')
        self.lstCategorias.clear()
        if self.lstParametros.currentItem():
           # print('current', str(self.lstParametros.currentItem().text()))
            actual = str(self.lstParametros.currentItem().text())
            del self.perfil_Actual[actual]
            self.lstParametros.takeItem(self.lstParametros.currentRow())
            self.actualizar_arbol()
        
    def btn_ExpPerfil(self):
        pass
        
    def btn_ImpPerfil(self):
        pass
    def btn_NuevoPerfil(self):
        pass
    def btn_AddParam(self):
        if self.lnNombreParam.text():
            print (self.lnNombreParam.text())
            self.perfil_Actual[self.lnNombreParam.text()]=[self.lnCodeParam.text(),[],'']
            self.lnNombreParam.setText('')
            self.lnCodeParam.setText('')
            self.actualizar_todo()
            print(self.lstParametros.count())
            self.lstParametros.setCurrentRow(self.lstParametros.count()-1)
    
    def btn_AddCat(self):
        print(self.lnCategorias.text())
        if self.lstParametros.currentItem():
            parametro_seleccionado = self.lstParametros.currentItem().text()
            if self.lnCategorias.text():
                self.perfil_Actual[parametro_seleccionado][1].append(self.lnCategorias.text())
                self.cargar_categorias()
                self.actualizar_arbol()
                self.lnCategorias.setText('')
        
      #  parametro = str(self.lstParametros.currentItem().text()[0])
      #  nombre = self.lstParametros.currentItem().text()
      #  categoria = str(self.combValorParam.currentText())
        
    def seleccion_parametro(self):
        self.cargar_categorias()
    
    def cargar_categorias(self):
        self.lstCategorias.clear()
        if self.lstParametros.currentItem():
            parametro_seleccionado = self.lstParametros.currentItem().text()
          #  print(dir(self.lstParametros.currentItem()))
          #  print (self.lstParametros.currentItem())
            for item in self.perfil_Actual[parametro_seleccionado][1]:
                self.lstCategorias.addItem(item)
    
    
    def cargar_diccionario(self,archivo):
        with open(archivo,'r') as file:
            self.perfil_Actual = json.loads(file.read())
        
    def cargar_parametros(self):
        self.lstParametros.clear()
        for key in self.perfil_Actual:
            self.lstParametros.addItem(key)
    
    def crear_Arbol(self,dictionary):
        arbol=''
        for key in dictionary:
            arbol += key +' - Cod: '+ str(dictionary[key][0])+'\n'#, dictionary[key][0] +'\n'
            for item in dictionary[key][1]:
                arbol += '\t-- ' + item + '\n'
        print(arbol)
        return arbol
        
    def actualizar_arbol(self):
        self.arbol = self.crear_Arbol(self.perfil_Actual)
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

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    d = MyWindow()
    d.show()
    d.raise_()
    
    app.exec_()
    print( 'tengo para devolver o buscar',d.perfil_Actual)
    if d.accepted:
        print('Acepte papa')
    
