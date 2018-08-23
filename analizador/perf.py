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



dict_parametros = {'Exudacion':['E',{'Alto':'A','Medio':'M','Bajo':'B'}],
                    'Bacheo':['B',{'Superficial':'S','Profundo':'P','Reparado':'R'}],
                    'Fisuras':['F',{'1':'1','2':'2','3':'3','4':'4','5':'5'}] }

class MyWindow(QtWidgets.QDialog):
    """Los perfiles son diccionarios el, default es
    dict_parametros = {'Exudacion':[False,['A','M','B']],'Bacheo':[False,['S','P','R']],'Fisuras':[True,['1','2','3','4','5']]}
    o sea, de la forma { 'Nombre_de_Parametro1':['cod_param1',['nombre_cat1':'cod_Cat','nombre_cat2':'cod_cat2']}
    """
    def __init__(self, parent=None):
       # global app
        super(MyWindow, self).__init__(parent)
        self.resize(754, 583)
        self.gridLayout_4 = QtWidgets.QGridLayout(self)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblPerfil = QtWidgets.QTextBrowser(self.groupBox_3)
        self.lblPerfil.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.lblPerfil.setObjectName("lblPerfil")
        self.gridLayout_3.addWidget(self.lblPerfil, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 1, 2, 4)
        self.btnExpPerfil = QtWidgets.QPushButton(self)
        self.btnExpPerfil.setObjectName("btnExpPerfil")
        self.gridLayout_4.addWidget(self.btnExpPerfil, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(93, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.btnNuevoPerfil = QtWidgets.QPushButton(self)
        self.btnNuevoPerfil.setObjectName("btnNuevoPerfil")
        self.gridLayout_4.addWidget(self.btnNuevoPerfil, 0, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnDelCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDelCat.setMaximumSize(QtCore.QSize(32, 32))
        self.btnDelCat.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_default/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelCat.setIcon(icon)
        self.btnDelCat.setObjectName("btnDelCat")
        self.gridLayout.addWidget(self.btnDelCat, 1, 3, 1, 1)
        self.btnAddCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddCat.setMaximumSize(QtCore.QSize(32, 32))
        self.btnAddCat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img_default/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddCat.setIcon(icon1)
        self.btnAddCat.setObjectName("btnAddCat")
        self.gridLayout.addWidget(self.btnAddCat, 0, 3, 1, 1)
        self.lnCategorias = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnCategorias.setText("")
        self.lnCategorias.setObjectName("lnCategorias")
        self.gridLayout.addWidget(self.lnCategorias, 0, 2, 1, 1)
        self.tblCategorias = QtWidgets.QTableWidget(self.groupBox_2)
        self.tblCategorias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCategorias.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblCategorias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCategorias.setObjectName("tblCategorias")
        self.tblCategorias.setColumnCount(2)
        self.tblCategorias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategorias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategorias.setHorizontalHeaderItem(1, item)
        self.tblCategorias.horizontalHeader().setVisible(True)
        self.tblCategorias.horizontalHeader().setDefaultSectionSize(50)
        self.tblCategorias.horizontalHeader().setHighlightSections(True)
        self.tblCategorias.horizontalHeader().setMinimumSectionSize(50)
        self.tblCategorias.horizontalHeader().setStretchLastSection(True)
        self.tblCategorias.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tblCategorias, 1, 0, 1, 3)
        self.lnCodeCat = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnCodeCat.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lnCodeCat.setObjectName("lnCodeCat")
        self.gridLayout.addWidget(self.lnCodeCat, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 3, 0, 2, 1)
        self.btnImpPerfil = QtWidgets.QPushButton(self)
        self.btnImpPerfil.setObjectName("btnImpPerfil")
        self.gridLayout_4.addWidget(self.btnImpPerfil, 0, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(93, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 1, 1)
        self.combPerfil = QtWidgets.QComboBox(self)
        self.combPerfil.setObjectName("combPerfil")
        self.gridLayout_4.addWidget(self.combPerfil, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lnCodeParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCodeParam.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lnCodeParam.setObjectName("lnCodeParam")
        self.gridLayout_2.addWidget(self.lnCodeParam, 0, 0, 1, 1)
        self.btnAddParam = QtWidgets.QPushButton(self.groupBox)
        self.btnAddParam.setMaximumSize(QtCore.QSize(32, 32))
        self.btnAddParam.setText("")
        self.btnAddParam.setIcon(icon1)
        self.btnAddParam.setObjectName("btnAddParam")
        self.gridLayout_2.addWidget(self.btnAddParam, 0, 2, 1, 2)
        self.btnDelParam = QtWidgets.QPushButton(self.groupBox)
        self.btnDelParam.setMaximumSize(QtCore.QSize(32, 32))
        self.btnDelParam.setText("")
        self.btnDelParam.setIcon(icon)
        self.btnDelParam.setObjectName("btnDelParam")
        self.gridLayout_2.addWidget(self.btnDelParam, 1, 3, 1, 1)
        self.lnNombreParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnNombreParam.setObjectName("lnNombreParam")
        self.gridLayout_2.addWidget(self.lnNombreParam, 0, 1, 1, 1)
        self.tblParametros = QtWidgets.QTableWidget(self.groupBox)
        self.tblParametros.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblParametros.setProperty("showDropIndicator", True)
        self.tblParametros.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblParametros.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblParametros.setShowGrid(True)
        self.tblParametros.setObjectName("tblParametros")
        self.tblParametros.setColumnCount(2)
        self.tblParametros.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblParametros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblParametros.setHorizontalHeaderItem(1, item)
        self.tblParametros.horizontalHeader().setCascadingSectionResizes(False)
        self.tblParametros.horizontalHeader().setDefaultSectionSize(50)
        self.tblParametros.horizontalHeader().setSortIndicatorShown(False)
        self.tblParametros.horizontalHeader().setStretchLastSection(True)
        self.tblParametros.verticalHeader().setVisible(False)
        self.tblParametros.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.tblParametros, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 4, 4, 1, 1)

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
        self.tblParametros.currentItemChanged.connect(self.seleccion_parametro)
    #cargo el default

        self.cargar_diccionario('perfiles/default.json')
        self.actualizar_todo()
        self.tblParametros.setCurrentCell(0,0)
       # self.tblCategorias.setHorizontalHeaderLabels(['Codigo','Nombre de Categoria'])
       # self.tblParametros.setHorizontalHeaderLabels(['Codigo','Nombre de Categoria'])
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_3.setTitle(_translate("Dialog", "Previsualizacion del Perfil"))
        self.lblPerfil.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnExpPerfil.setText(_translate("Dialog", "Exportar Perfil"))
        self.btnNuevoPerfil.setText(_translate("Dialog", "Nuevo Perfil"))
        self.groupBox_2.setTitle(_translate("Dialog", "Categorias"))
        self.lnCategorias.setPlaceholderText(_translate("Dialog", "Nombre de categoria"))
        item = self.tblCategorias.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Codigo"))
        item = self.tblCategorias.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Categoria"))
        self.lnCodeCat.setPlaceholderText(_translate("Dialog", "COD"))
        self.btnImpPerfil.setText(_translate("Dialog", "Importar Perfil"))
        self.pushButton.setText(_translate("Dialog", "Borrar Perfil"))
        self.label.setText(_translate("Dialog", "Perfil Actual"))
        self.groupBox.setTitle(_translate("Dialog", "Parametros"))
        self.lnCodeParam.setPlaceholderText(_translate("Dialog", "COD"))
        self.lnNombreParam.setPlaceholderText(_translate("Dialog", "Nombre de parametro"))
        item = self.tblParametros.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Codigo"))
        item = self.tblParametros.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Parametro"))
        


        """
        self.lblPerfil.setObjectName("lblPerfil")
        self.lnNombreParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCodeParam = QtWidgets.QLineEdit(self.groupBox)
        self.lnCategorias
        self.tblCategorias = QtWidgets.QListView(self.groupBox_2)
        self.combPerfil = QtWidgets.QComboBox(Dialog)
       """

    def btn_DelCat(self):
        if self.tblParametros.currentItem():
            actual_param = self.tblParametros.item(self.tblParametros.currentRow(),1).text()
            if self.tblCategorias.currentItem():
                item = self.tblCategorias.item(self.tblCategorias.currentRow(),1).text()
                del self.perfil_Actual[actual_param][1][item]
                self.tblCategorias.removeRow(self.tblCategorias.currentRow())
                self.actualizar_arbol()
        
    def btn_DelParam(self):
        if self.tblParametros.currentItem():
            self.tblCategorias.clearContents()
            actual_param = self.tblParametros.item(self.tblParametros.currentRow(),1).text()
            del self.perfil_Actual[actual_param]
            self.tblParametros.removeRow(self.tblParametros.currentRow())
            self.actualizar_arbol()
        
    def btn_ExpPerfil(self):
        arch_json = QtWidgets.QFileDialog.getSaveFileName(self, 'Ingrese nombre y destino', '/' , filter='*.json')[0]
        if arch_json:
            if not arch_json.lower().endswith('.json'):
                arch_json += '.json'
            print('[Exportar Perfil] Guardo .json en archivo {}'.format( arch_json) )
        else:
            return
        with open(arch_json,'w') as archivo:
            json.dump(self.perfil_Actual,archivo)
            print('exporto a archivo:',arch_json)
        
    def btn_ImpPerfil(self):
        pass
    def btn_NuevoPerfil(self):
        pass
    def btn_AddParam(self):
        if self.lnNombreParam.text() and self.lnCodeParam.text():
            print (self.lnNombreParam.text())
            self.perfil_Actual[self.lnNombreParam.text()]=[self.lnCodeParam.text(),{}]
            self.lnNombreParam.setText('')
            self.lnCodeParam.setText('')
            self.actualizar_todo()
            #print(self.tblParametros.count())
            self.tblParametros.setCurrentCell(self.tblParametros.rowCount()-1,1)
    
    def btn_AddCat(self):   #cambiar line edit por lnCodeCat 
        print(self.lnCategorias.text())
        if self.tblParametros.currentItem():
            parametro_seleccionado = self.tblParametros.item(self.tblParametros.currentRow(),1).text()
            if self.lnCategorias.text() and self.lnCodeCat.text() :
                self.perfil_Actual[parametro_seleccionado][1][self.lnCategorias.text()] = self.lnCodeCat.text()
                self.cargar_categorias()
                self.actualizar_arbol()
                self.lnCategorias.setText('')
                self.lnCodeCat.setText('')
        
      #  parametro = str(self.tblParametros.currentItem().text()[0])
      #  nombre = self.tblParametros.currentItem().text()
      #  categoria = str(self.combValorParam.currentText())
        
    def seleccion_parametro(self):
        self.cargar_categorias()
    
    def cargar_categorias(self):
        self.tblCategorias.clearContents()
        self.tblCategorias.setRowCount(0)
        #self.tblParametros.setRowCount(len(self.perfil_Actual))
        if self.tblParametros.currentItem():
            parametro_seleccionado = self.tblParametros.item(self.tblParametros.currentRow(),1).text()
          #  print(dir(self.tblParametros.currentItem()))
          #  print (self.tblParametros.currentItem())
            dic_cat=self.perfil_Actual[parametro_seleccionado][1]
            for i, nom_categoria in enumerate(dic_cat):
                #parsear evento
                self.tblCategorias.insertRow(i)
                codigo = dic_cat[nom_categoria]
                self.tblCategorias.setItem(i, 0, QtWidgets.QTableWidgetItem(codigo)) 
                self.tblCategorias.setItem(i, 1, QtWidgets.QTableWidgetItem(nom_categoria)) 
   
    
    
    def cargar_diccionario(self,archivo):
        with open(archivo,'r') as file:
            self.perfil_Actual = json.loads(file.read())
            
        self.perfil_Actual = dict_parametros #sacar depues de debug
        
    def cargar_parametros(self):
        self.tblParametros.clearContents()
         #lleno tabla
        self.tblParametros.setRowCount(len(self.perfil_Actual))
        for i, nom_parametro in enumerate(self.perfil_Actual):
            #parsear evento
            codigo = self.perfil_Actual[nom_parametro][0]
            self.tblParametros.setItem(i, 0, QtWidgets.QTableWidgetItem(codigo)) 
            self.tblParametros.setItem(i, 1, QtWidgets.QTableWidgetItem(nom_parametro)) 
    
    def crear_Arbol(self,dictionary):
        arbol=''
        print('el dic es: \n',dictionary)
        for nom_parametro in dictionary:
            arbol += nom_parametro +' - Cod: '+ str(dictionary[nom_parametro][0])+'\n' #el codigo del param
            dict_categorias = dictionary[nom_parametro][1]
            print( 'las cat son :\n',dict_categorias)
            for categoria in dict_categorias: # es un diccionario {'nom_cat1':'cod_cat1', 'nom_cat22:'cod_2'... }
                print('cat:',categoria,'')
                arbol += '\t-->  ' + categoria +' - Cod: ' + dict_categorias[categoria]+ '\n'
            arbol +='\n'
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
    
