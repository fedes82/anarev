# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maps.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_diagConfMapas(object):
    def setupUi(self, diagConfMapas):
        diagConfMapas.setObjectName("diagConfMapas")
        diagConfMapas.resize(559, 249)
        self.verticalLayout = QtWidgets.QVBoxLayout(diagConfMapas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(diagConfMapas)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbBING = QtWidgets.QRadioButton(self.groupBox)
        self.rbBING.setObjectName("rbBING")
        self.verticalLayout_2.addWidget(self.rbBING)
        self.rb = QtWidgets.QRadioButton(self.groupBox)
        self.rb.setObjectName("rb")
        self.verticalLayout_2.addWidget(self.rb)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lnKEY = QtWidgets.QLineEdit(self.groupBox)
        self.lnKEY.setText("")
        self.lnKEY.setPlaceholderText("")
        self.lnKEY.setObjectName("lnKEY")
        self.verticalLayout_2.addWidget(self.lnKEY)
        self.rb.raise_()
        self.lnKEY.raise_()
        self.label.raise_()
        self.rbBING.raise_()
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.btnGuardar = QtWidgets.QPushButton(diagConfMapas)
        self.btnGuardar.setEnabled(False)
        self.btnGuardar.setCheckable(False)
        self.btnGuardar.setFlat(False)
        self.btnGuardar.setObjectName("btnGuardar")
        self.horizontalLayout_3.addWidget(self.btnGuardar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(diagConfMapas)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sBoxZoom = QtWidgets.QSpinBox(self.groupBox_2)
        self.sBoxZoom.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sBoxZoom.setObjectName("sBoxZoom")
        self.horizontalLayout.addWidget(self.sBoxZoom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sBoxZoom.raise_()
        self.label_2.raise_()
        self.sBoxZoom.raise_()
        self.label_2.raise_()
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(diagConfMapas)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(diagConfMapas)
        self.buttonBox.accepted.connect(diagConfMapas.accept)
        self.buttonBox.rejected.connect(diagConfMapas.reject)
        QtCore.QMetaObject.connectSlotsByName(diagConfMapas)

    def retranslateUi(self, diagConfMapas):
        _translate = QtCore.QCoreApplication.translate
        diagConfMapas.setWindowTitle(_translate("diagConfMapas", "Configuracion del servidor de mapas"))
        self.groupBox.setTitle(_translate("diagConfMapas", "Proveedor"))
        self.rbBING.setText(_translate("diagConfMapas", "BING Maps"))
        self.rb.setText(_translate("diagConfMapas", "Google Maps"))
        self.label.setText(_translate("diagConfMapas", "Llave (API KEY)"))
        self.btnGuardar.setText(_translate("diagConfMapas", "Guardar Cambios"))
        self.label_2.setText(_translate("diagConfMapas", "Zoom"))
