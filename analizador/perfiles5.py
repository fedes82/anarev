# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfiles.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 583)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(57, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.widget)
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout_4.addWidget(self.btnGuardar, 1, 6, 1, 1)
        self.btnEdicion = QtWidgets.QPushButton(self.widget)
        self.btnEdicion.setObjectName("btnEdicion")
        self.gridLayout_4.addWidget(self.btnEdicion, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(63, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 8, 1, 1)
        self.btnImpPerfil = QtWidgets.QPushButton(self.widget)
        self.btnImpPerfil.setObjectName("btnImpPerfil")
        self.gridLayout_4.addWidget(self.btnImpPerfil, 0, 9, 1, 1)
        self.combPerfil = QtWidgets.QComboBox(self.widget)
        self.combPerfil.setObjectName("combPerfil")
        self.gridLayout_4.addWidget(self.combPerfil, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(63, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 8, 1, 1)
        self.btnNuevoPerfil = QtWidgets.QPushButton(self.widget)
        self.btnNuevoPerfil.setObjectName("btnNuevoPerfil")
        self.gridLayout_4.addWidget(self.btnNuevoPerfil, 0, 4, 1, 1)
        self.btnExpPerfil = QtWidgets.QPushButton(self.widget)
        self.btnExpPerfil.setObjectName("btnExpPerfil")
        self.gridLayout_4.addWidget(self.btnExpPerfil, 1, 9, 1, 1)
        self.lblPerfilPrincipal = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPerfilPrincipal.setFont(font)
        self.lblPerfilPrincipal.setObjectName("lblPerfilPrincipal")
        self.gridLayout_4.addWidget(self.lblPerfilPrincipal, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.btnBorrar = QtWidgets.QPushButton(self.widget)
        self.btnBorrar.setObjectName("btnBorrar")
        self.gridLayout_4.addWidget(self.btnBorrar, 1, 7, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Documentos/ingenia/revwin-1-0/analizador/img_default/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddParam.setIcon(icon)
        self.btnAddParam.setObjectName("btnAddParam")
        self.gridLayout_2.addWidget(self.btnAddParam, 0, 2, 1, 2)
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
        self.gridLayout_2.addWidget(self.tblParametros, 1, 0, 1, 3)
        self.btnDelParam = QtWidgets.QPushButton(self.groupBox)
        self.btnDelParam.setMaximumSize(QtCore.QSize(32, 32))
        self.btnDelParam.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Documentos/ingenia/revwin-1-0/analizador/img_default/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelParam.setIcon(icon1)
        self.btnDelParam.setObjectName("btnDelParam")
        self.gridLayout_2.addWidget(self.btnDelParam, 1, 3, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblPerfil = QtWidgets.QTextBrowser(self.groupBox_3)
        self.lblPerfil.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.lblPerfil.setObjectName("lblPerfil")
        self.gridLayout_3.addWidget(self.lblPerfil, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAddCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAddCat.setMaximumSize(QtCore.QSize(32, 32))
        self.btnAddCat.setText("")
        self.btnAddCat.setIcon(icon)
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
        self.btnDelCat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDelCat.setMaximumSize(QtCore.QSize(32, 32))
        self.btnDelCat.setText("")
        self.btnDelCat.setIcon(icon1)
        self.btnDelCat.setObjectName("btnDelCat")
        self.gridLayout.addWidget(self.btnDelCat, 1, 3, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 2, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.combPerfil, self.btnNuevoPerfil)
        Dialog.setTabOrder(self.btnNuevoPerfil, self.btnEdicion)
        Dialog.setTabOrder(self.btnEdicion, self.btnGuardar)
        Dialog.setTabOrder(self.btnGuardar, self.btnBorrar)
        Dialog.setTabOrder(self.btnBorrar, self.btnImpPerfil)
        Dialog.setTabOrder(self.btnImpPerfil, self.btnExpPerfil)
        Dialog.setTabOrder(self.btnExpPerfil, self.lnCodeParam)
        Dialog.setTabOrder(self.lnCodeParam, self.lnNombreParam)
        Dialog.setTabOrder(self.lnNombreParam, self.btnAddParam)
        Dialog.setTabOrder(self.btnAddParam, self.tblParametros)
        Dialog.setTabOrder(self.tblParametros, self.btnDelParam)
        Dialog.setTabOrder(self.btnDelParam, self.lnCodeCat)
        Dialog.setTabOrder(self.lnCodeCat, self.lnCategorias)
        Dialog.setTabOrder(self.lnCategorias, self.btnAddCat)
        Dialog.setTabOrder(self.btnAddCat, self.tblCategorias)
        Dialog.setTabOrder(self.tblCategorias, self.btnDelCat)
        Dialog.setTabOrder(self.btnDelCat, self.lblPerfil)
        Dialog.setTabOrder(self.lblPerfil, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnGuardar.setText(_translate("Dialog", "Guardar"))
        self.btnEdicion.setText(_translate("Dialog", "Editar"))
        self.btnImpPerfil.setText(_translate("Dialog", "Importar Perfil"))
        self.btnNuevoPerfil.setText(_translate("Dialog", "Nuevo Perfil"))
        self.btnExpPerfil.setText(_translate("Dialog", "Exportar Perfil"))
        self.lblPerfilPrincipal.setText(_translate("Dialog", "texto"))
        self.label.setText(_translate("Dialog", "Perfil cargado actualmente:"))
        self.btnBorrar.setText(_translate("Dialog", "Borrar Perfil"))
        self.groupBox.setTitle(_translate("Dialog", "Parametros"))
        self.lnCodeParam.setPlaceholderText(_translate("Dialog", "COD"))
        self.lnNombreParam.setPlaceholderText(_translate("Dialog", "Nombre de parametro"))
        item = self.tblParametros.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Codigo"))
        item = self.tblParametros.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Parametro"))
        self.groupBox_3.setTitle(_translate("Dialog", "Previsualizacion del Perfil"))
        self.lblPerfil.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "Categorias"))
        self.lnCategorias.setPlaceholderText(_translate("Dialog", "Nombre de categoria"))
        item = self.tblCategorias.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Codigo"))
        item = self.tblCategorias.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Categoria"))
        self.lnCodeCat.setPlaceholderText(_translate("Dialog", "COD"))

