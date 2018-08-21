# -*- coding: UTF-8 -*-
version = '1.0'

#import sip
#sip.setapi('QString', 2)
#sip.setapi('QVariant', 1)

####  PARA EL PYINSTALLER, HAY QUE AGREGAR :
##   --hidden-import PyQt5.sip
## EN EL COMANDO pyinstaller analizador.py, o sea:
## pyinstaller analizador.py --hidden-import PyQt5.sip 
from PyQt5.QtCore import Qt
##PARA EL GUI
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialogButtonBox, QDialogButtonBox,QMessageBox
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
#### para crear el python que hace falta para cargar el archivo que crea 
#### el qtdesigner usar:
####  pyuic4 analizador-form-1-0.ui -o interface.py
#### con analizador-form-1-0.ui es el archivo qtdesigner
#### y interface.py el que importo en el main
import sys
import interface

##GRAL
import os
import os.path
from os.path import expanduser
import random

from collections import defaultdict
import json
import csv
import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED
#PIL imports
from PIL import Image as PILImage
from PIL import ImageFont as PILImageFont
from PIL import ImageDraw as PILImageDraw

#import cPickle as pickle
from pathlib2 import Path ##importanchi






###---------------------------------------------------PARA LOGGEAR

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('bitacora.log')
handler_traceback = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


###para sacar el traceback por el logger
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
# add the handlers to the logger
logger.addHandler(handler_traceback)
logger.addHandler(handler)

####---------------------------------------------------FIN LOGGEAR


class Info():
    def __init__(self):
        self.operador = 'ND'
        self.fecha = 'ND'
        self.ruta='ND'
        self.sentido='ND'
        self.dist_inicial='ND'
        self.dist_final='ND'
    def cargar_info(self,archivo):
        if os.path.exists(archivo):
            with open(archivo,'r') as arch:
                info = arch.readlines()
                self.operador = info.pop()[:-2]
                self.fecha = info.pop()
                self.ruta=info[0]
                self.sentido=info[0]
                self.dist_inicial=info[0]
                
                self.dist_final='ND'
            logger.info( '[leer_info] la info de la sesion es:{}'.format( self.info))
        else:
            logger.info('[leer_info] no se encontro info.txt')
    
    def reset(self):
        self.operador = 'ND'
        self.fecha = 'ND'
        self.ruta='ND'
        self.sentido='ND'
        self.dist_inicial='ND'
        self.dist_final='ND'




### VER PARA CERRAR Y DEVOLVER EL PATH  
###  https://stackoverflow.com/questions/11544800/pyqt4-closing-a-dialog-window-exec-not-working
#class MyWindow(QtGui.QWidget):
class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
       # global app
        super(MyWindow, self).__init__(parent)
        self.resize(1024, 600)
     #   self.move(app.desktop().screen().rect().center() - main.rect().center())
        self.pathRoot = QtCore.QDir.rootPath()

        self.model = QtWidgets.QFileSystemModel(self)
        self.model.setRootPath('/')
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Dirs | QtCore.QDir.Drives)
        self.indexRoot = self.model.index(self.model.myComputer())
        self.otro =  self.model.index('C:\\')

        self.treeView = QtWidgets.QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.expand(self.otro)
        #self.treeView.setRootIndex(self.indexRoot)
        self.treeView.header().hide()
        #Con esto no muestro tamano ni fecha ni nada mas que el nombre
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        
        self.treeView.clicked.connect(self.on_treeView_clicked)
        
        self.labelFileName = QtWidgets.QLabel(self)
        self.labelFileName.setText("Carpeta:")

        self.lineEditFileName = QtWidgets.QLineEdit(self)

        self.labelFilePath = QtWidgets.QLabel(self)
        self.labelFilePath.setText("Path:")

        self.lineEditFilePath = QtWidgets.QLineEdit(self)
        
        # self.btnOK = QtWidgets.QPushButton(self)
        # self.btnOK.setText('Aceptar')
        # self.btnOK.clicked.connect(self.boton_ok)
        # self.btnCancel = QtWidgets.QPushButton(self)
        # self.btnCancel.setText('Cancelar')
        # self.btnCancel.clicked.connect(self.boton_cancel)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.boton_ok)
        self.buttons.rejected.connect(self.boton_cancel)
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addWidget(self.labelFileName, 0, 0)
        self.gridLayout.addWidget(self.lineEditFileName, 0, 1)
        self.gridLayout.addWidget(self.labelFilePath, 1, 0)
        self.gridLayout.addWidget(self.lineEditFilePath, 1, 1)
       # self.gridLayout.addWidget(self.btnCancel,2,0)
       # self.gridLayout.addWidget(self.btnOK,2,1)
        

        #self.lblImgPreview = ScaledLabel()
        #self.lblImgPreview.setObjectName(("lblImgPreview"))
        self.lblImg = QtWidgets.QLabel(self)
        self.lblImg.setPixmap(QtGui.QPixmap(IMG_DEFAULT).scaled(
            520, 320,
            QtCore.Qt.KeepAspectRatio))
        
        #self.lblImg.setPixmap(self._pixmap.
        self.lblInfo = QtWidgets.QLabel(self)
        self.lblInfo.setText('No se encontro archivo info.txt')
        
        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV1.addWidget(self.treeView)
        self.layoutV1.addLayout(self.gridLayout)
        self.layoutV1.addWidget(self.buttons)
        
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV2.addWidget(self.lblImg)
        self.layoutV2.addWidget(self.lblInfo)
        
        self.layoutH = QtWidgets.QHBoxLayout(self)
        self.layoutH.addLayout(self.layoutV1)
        self.layoutH.addLayout(self.layoutV2)
        
        self.treeView.setCurrentIndex(self.model.index(home))
        self.treeView.expand(self.model.index(home))
        self.fileName_selected = ''
        self.filePath_selected = ''
        self.setWindowTitle('Seleccionar carpeta de sesión')
        
    def boton_ok(self):
        print('ok')
        print( self.fileName_selected)
        print( self.filePath_selected)
        super(MyWindow, self).accept()
    
    def boton_cancel(self):
        print ('cancel')
        super(MyWindow, self).reject()
    
    
    ### ACA INCLUYO LA ACTUALIZACION DE INFO E IMAGEN
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        #aca hacer filtro y hab o no el aceptar
        indexItem = self.model.index(index.row(), 0, index.parent())

        self.fileName_selected = self.model.fileName(indexItem)
        self.filePath_selected = self.model.filePath(indexItem)

        self.lineEditFileName.setText(self.fileName_selected)
        self.lineEditFilePath.setText(self.filePath_selected)
        
        #filtro preview e info
        if os.path.isdir(self.filePath_selected):
            print (self.filePath_selected, ' es dir')
            if os.path.isfile(os.path.join(self.filePath_selected,'info.txt')):
                print ('encontre info')
                with open(os.path.join(self.filePath_selected,'info.txt'),'r') as info:
                    self.lblInfo.setText(info.read())
                    self.lblInfo.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            else:
                self.lblInfo.setText('No se encontró archivo info.txt')
            archivos = os.listdir(self.filePath_selected)
            random.shuffle(archivos)
            for archivo in archivos:
                if 'c1' in archivo and archivo.endswith('.jpg'):
                    print( 'es imagen, la cargo :',self.filePath_selected)
                    self.lblImg.setPixmap(QtGui.QPixmap(os.path.join(self.filePath_selected, archivo)).scaled(
                        520, 320,
                        QtCore.Qt.KeepAspectRatio))
                    return
            self.lblImg.setPixmap(QtGui.QPixmap(IMG_DEFAULT).scaled(
                520, 320,
                QtCore.Qt.KeepAspectRatio))
        else:
            print( self.filePath_selected, ' NO es dir')
                
        
        

class Mojon:
    def __init__(self,progresiva):
        self.progresiva = progresiva
        self.latitud = ''
        self.longitud = ''
        self.eventos = []
        self.archivos_img =['','','']
        self.mapas = ['','']

    def __repr__(self):
        """Esto define como lo muestra, o sea que en una lista de estos objetos
        cada item se va a representar con lo que tenga en progresiva"""
        return repr(self.progresiva)
    def __eq__(self,otro):
        """Aca defino que es lo que hace cuando compara este objeto con algo mas,
        yo lo uso para poder ver si ya existe un objeto con prog 'xxx' en la lista de 
        objetos, haciendo: if  'xxx' in lista : ...."""
        return self.progresiva == otro

def parsear_nombre(nom_img):
        """toma el nombre como parametro y devuelve
        progresiva,latitud,longitud,camara"""
        progresiva = nom_img[:6]
        #por compatibilidad hacia atras
        nom_img = nom_img.split('.jpg')[0]
        nom_img = nom_img.split('MARCA')[0]
        try:    
            if nom_img.split('GPS_')[1].startswith('Sin'):
                lat = '-'
                long = '-'
            else:
                lat = nom_img.split('GPS_')[1][:-4].split(',')[0]
                long = nom_img.split('GPS_')[1][:-4].split(',')[1]
        except IndexError:
            lat = 'e'
            long = 'e'
        if '__c1__' in nom_img: cam = 0
        elif '__c2__' in nom_img: cam = 1
        else: cam = 2
        return progresiva,lat,long,cam

        
        #serializo lista de objetos
def serializo_y_guardo(lista_de_objetos, arch_destino, delimitador ='\n'):
    q=''    #cuerpo del archivo
    for objeto in lista_de_objetos:
        linea = json.dumps(objeto.__dict__)
        q = q + linea + delimitador
    with open(arch_destino,'w') as f:
        f.write(q)
    
        

def deserializo_y_cargo(arch_fuente, delimitador='\n'):
    with open(arch_fuente,'r') as f:
        lineas_json=f.read().rsplit(delimitador)
    l = []  #lista de objetos resultante
    for linea in lineas_json:
        if not linea: continue
        d = json.loads(linea)
        l.append(Mojon(d['progresiva']))
        l[-1].latitud = d['latitud']
        l[-1].longitud = d['longitud']
        l[-1].mapas = d['mapas']
        l[-1].archivos_img = d['archivos_img']
        l[-1].eventos = d['eventos']
    return l
    
    
#CARPETA_SESION = 'SESIONES/'
#CARPETA_SESION_FOTOS = 'SESIONES/s1/'
#CARPETA_SESION_FOTOS = 'C:/Users/fede/Desktop/SESIONES/Cno_de_la_Costa_Brava_Term_Zarate/'
#CARPETA_SESION_FOTOS = 'C:/Users/fede/Desktop/SESIONES/incompleto/'
IMG_DEFAULT = 'img_default/imgDefault.jpg'
#IMG_DEFAULT = 'SESIONES/rotadas/c2__000047m_2016_03_03_19h22m08.465186sMARCA.jpg'
CARPETA_SESION_FOTOS = ''
F = [1,2,3,4,5]
B = ['S','P','R']
E = ['A','M','B']
#Los paramatros los guardo en un diccionario que tiene:
# 'Nombre que muestra en la lista' : [valor_extra(True/False),[Lista para el combo]]
#quizas se puede hacer un diccionario de diccionarios
#onda dictgral ={ 'exudacion':dictexudacion, 'bacheo':dictbacheo }
dict_parametros = {'Exudacion':[False,['A','M','B']],'Bacheo':[False,['S','P','R']],'Fisuras':[True,['1','2','3','4','5']]}

with open('perfiles/default.json','r') as file:
    dict_parametros = json.loads(file.read())
print('los param son',dict_parametros)
DEBUG = True

##para serializacion con json
## https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183


class RevisadorApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    global DEBUG
    global CARPETA_SESION_FOTOS
    #defaultdict me permite crear un diccionario del tipo
    # 'key':[lista]
    #medio facilito
    #ver https://docs.python.org/2/library/collections.html#defaultdict-examples
    eventos_sesion_modificado = False
    pos1 = 0
    pos2 = 1
    pos3 = 2
    dirsesion = ''
    info = ''
    mojones = []
    
    def __init__(self, parent=None):
        super(RevisadorApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(QPixmap('img_default/icono.ico')))
###Uso Qlabels para mostrar las imagenes, tengo que 
### indicarle q son mapa de bits y no texto
        self.lblimg1.actualizar(IMG_DEFAULT)
        self.lblimg2.actualizar(IMG_DEFAULT)
        self.lblimg3.actualizar(IMG_DEFAULT)
        self.lblimg2.mousePressEvent = self.focoenventana2
        self.lblimg3.mousePressEvent=  self.focoenventana3
        self.lblimg1.mousePressEvent= self.focoenventana1
        
        ##### VALIDACION DE ENTRADA EN LINE EDIT    lnValorParam
        ##### PARA QUE SOLO ACEPTE NUMEROS DE HASTA TRES DIGITOS
        regex = QRegExp("[0-9][0-9][0-9]")
        validator = QRegExpValidator(regex)
        self.lnValorParam.setValidator(validator)
    
##   Vinculos con los elementos graficos
        self.btnAnterior.clicked.connect(self.btn_Anterior)
        self.btnSiguiente.clicked.connect(self.btn_Siguiente)
        self.btnAgregarEvento.clicked.connect(self.agregar_evento)
        self.btnElimEvento.clicked.connect(self.eliminar_evento)
        self.btnEventSig.clicked.connect(self.btn_Event_Sig)
        self.btnEventAnt.clicked.connect(self.btn_Event_Ant)
        
        self.statusBar().showMessage('Listo')
        self.sldrPosicion.valueChanged.connect(self.saltar_a_valor)
        self.tbtnPlay.clicked.connect(self.play)
        self.timerPlay = QTimer()
        self.timerPlay.timeout.connect(self.btn_Siguiente)
        
        self.lstParametros.currentItemChanged.connect(self.seleccion_parametro)
        
    #### cargo la lista de parametros
        self.cargar_parametros()
    ##  para el menu
        self.actionAbrir.setShortcut('Ctrl+A')
        self.actionAbrir.setStatusTip('Abrir sesión')
        self.actionAbrir.triggered.connect(self.abrir_sesion2)
        self.actionSalir.setShortcut('Ctrl+Q')
        self.actionSalir.setStatusTip('Salir de la aplicación')
        self.actionSalir.triggered.connect(self.salir)
        self.actionGuardar.triggered.connect(self.guardar_sesion)
        self.actionGuardar.setShortcut('Ctrl+G')
        self.actionExportar_ANAX.triggered.connect(self.exportar_anax)
        self.actionInfo.triggered.connect(self.ver_info)
        self.actionExportar_ANAX.setStatusTip('Exportar aechivo ANAX, para ser utilizado con el soft Analizador')
        self.actionExportar_CSV.setStatusTip('Exportar aechivo CSV, para ser utilizado con soft de planilla de cálculo (Excel o similar)')     
        self.actionExportar_CSV.triggered.connect(self.exportar_csv)
        self.btnSiguiente.setStatusTip('Siguiente hito')
        self.btnAnterior.setStatusTip('Anterior hito')
        self.btnEventSig.setStatusTip('Siguiente hito con observaciones')
        self.btnEventAnt.setStatusTip('Anterior hito con observaciones')
        self.btnElimEvento.setStatusTip('Eliminar observación seleccionada de la lista')
        self.btnAgregarEvento.setStatusTip('Agregar observación')
        self.spinBox.setStatusTip('Ingrese retardo entre hitos, en milisegundos')
        self.lstParametros.setStatusTip('Seleccione parametro')
        self.combValorParam.setStatusTip('Seleccione categoria')
        self.lnValorParam.setStatusTip('Ingrese valor:  000 - 999')
        self.lstEventos.setStatusTip('Observaciones para este hito')
        self.lblimg1.setStatusTip('Haga click para mostrar en principal')
        self.lblimg2.setStatusTip('Haga click para mostrar en principal')
        self.lblimg3.setStatusTip('Haga click para mostrar en orden inicial')
        
       ### Deshabilito todo hasta que se cargue una sesion
        
        self.Habilitar_botones(False)
    ### inicializo variables internas - quizas despues tenga que 
    ### implementar un .ini que me guarde las cosas de la configuracion
    ### entre sesiones
        self.indice = 0
        self.AUTOMATICO = False
        self.setWindowTitle('ANALIZADOR PAVIMENTOS -- REFOCA ')
     
    def closeEvent(self, event):
        print( "User has clicked the red x on the main window")
        self.salir()
        
    def cargar_parametros(self):
        self.lstParametros.clear()
        for key in dict_parametros:
            self.lstParametros.addItem(key)
        
    def Habilitar_botones(self,estado):
        self.btnSiguiente.setEnabled(estado)
        self.btnAnterior.setEnabled(estado)
        self.btnEventSig.setEnabled(estado)
        self.btnEventAnt.setEnabled(estado)
        self.tbtnPlay.setEnabled(estado)
        self.btnAgregarEvento.setEnabled(estado)
        self.btnElimEvento.setEnabled(estado)
        logger.info('hab botones e n fun {}'.format(sys._getframe().f_code.co_name))
 
    def salir(self):
        mensaje = 'La sesión ha sido modificada\n¿Desea guardar la sesión antes de salir?'
        if self.eventos_sesion_modificado:
            choice = QtWidgets.QMessageBox.question(self, 'Guardar Sesión',
                                            (mensaje),
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.guardar_sesion()  
        logger.info('[salir] Cierro programa')
        sys.exit()
        #QtWidgets.qApp.quit()
        
    def focoenventana1(self,event):
        temp= self.pos3
        self.pos3 = self.pos1
        self.pos1 = temp
        self.cargar_mojon_gui(self.indice)
    
    def focoenventana2(self,event):
        temp= self.pos3
        self.pos3 = self.pos2
        self.pos2 = temp
        self.cargar_mojon_gui(self.indice)
        
    def focoenventana3(self,event):
        self.pos1 = 0
        self.pos2 = 1
        self.pos3 = 2
        self.cargar_mojon_gui(self.indice)
    
    def ver_info(self,event):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        obs = 0
        for mojon in self.mojones[:]:
            if  mojon.eventos:
                obs+=1
        print( 'obs',obs)
        if self.info:
            self.msg.setText('info.txt:\n'+self.info)
        else:
            self.msg.setText('No se encontró el archivo "info.txt"') 
        self.msg.setInformativeText('Path de la sesión: \n'+ self.dirsesion+'\nNro Observaciones:\n'+str(obs))
        self.msg.setWindowTitle('Información de la sesión')
        #msg.setDetailedText("The details are as follows:")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
        self.msg.exec_()
        
    def cargar_info(self,path):
        try:
            with open(path,'r') as txt:
                self.info = txt.read()
        except:
            logger.info('[cargar_info] no se encontro info.txt')
            self.info = ''
        
    def exportar_anax(self):    ###CAMBIAR CON OS:PATH:JOIN LOS PATHS
        """https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys"""
        """ https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects """
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Ingrese nombre y destino', self.dirsesion , filter='*.anax')[0]
        if fileName:
            if not fileName.lower().endswith('.anax'):
                fileName += '.anax'
            logger.info('[Exportar ANAX] Guardo .anax en archivo {}'.format( fileName) )
        else:
            return
        mojones_a_exportar = []
        for mojon in self.mojones[:]:
            if  mojon.eventos:
                mojones_a_exportar.append(mojon)
        serializo_y_guardo( mojones_a_exportar, os.path.join(self.dirsesion,'analizador.pkl') )
        with zipfile.ZipFile(fileName,'w') as zip:
            for mojon in mojones_a_exportar:
                    for archivo in mojon.archivos_img:
                        zip.write(os.path.join(self.dirsesion,archivo),arcname=archivo,compress_type=compression)
            if os.path.exists(os.path.join(self.dirsesion,'analizador.pkl')):
                zip.write(os.path.join(self.dirsesion,'analizador.pkl'),arcname='analizador.pkl',compress_type=compression)
                os.remove( os.path.join(self.dirsesion,'analizador.pkl') )
            if os.path.exists(os.path.join(self.dirsesion,'info.txt')):
                zip.write(os.path.join(self.dirsesion,'info.txt'),arcname='info.txt',compress_type=compression)
        
    def exportar_csv(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Ingrese nombre y destino', self.dirsesion, filter='*.csv')[0]
        if fileName:
            logger.info("[Exportar CSV] Guardo .csv en archivo {}".format( fileName) )
        else:
            return
        mojones_a_exportar = []
        for mojon in self.mojones[:]:
            if  mojon.eventos:
                mojones_a_exportar.append(mojon)
        with open(fileName,'w',newline='') as f:  #es necesario el modo binario por que usa \n\r para nueva linea y con 'w' solo queda un espacio de mas
            writer = csv.writer(f)
            writer.writerow( ['Dist Progresiva','Latitud','Longitud','Parametro','Categoria','Valor'])
            for mojon in mojones_a_exportar:
                logger.debug( '[Exportar evento] mojon {}'.format( mojon))
                for evento in mojon.eventos:
                    logger.debug( '[Exportar evento] evento:'.format(evento))
                    logger.debug('[Exportar evento] escribo linea {}'.format( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento))
                    writer.writerow( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento)
    

    def agregar_evento(self):
        parametro = str(self.lstParametros.currentItem().text()[0])
        nombre = self.lstParametros.currentItem().text()
        categoria = str(self.combValorParam.currentText())
        if self.lnValorParam.isEnabled():
            valor = str(self.lnValorParam.text())
        else:
            valor = ''  
        evento = [parametro,categoria,valor]
        self.mojones[self.indice].eventos.append(evento)
        evento_texto = '{}m {},{} -- {} {} {}'.format(self.mojones[self.indice].progresiva,
                                                        self.mojones[self.indice].latitud,
                                                        self.mojones[self.indice].longitud,
                                                        parametro, categoria, valor)
        self.lstEventos.addItem(evento_texto)
        self.eventos_sesion_modificado = True
        logger.info('[agregar_evento] Agregue evento {}'.format(evento_texto))
    
    def eliminar_evento(self):
        self.lstEventos.takeItem(self.lstEventos.currentRow())
        a = self.mojones[self.indice].eventos.pop(self.lstEventos.currentRow())
        logger.info('[eliminar_evento] Elimino en prog {} - evento {}'.format(self.mojones[self.indice].progresiva,a))
       # print 'saco: ',self.lstEventos.currentRow(),' que es tipo: ',type(self.lstEventos.currentRow())
        self.eventos_sesion_modificado = True
       # print 'hay eventos',self.mojones[self.indice].eventos
        
        
        
    def guardar_sesion(self):
        if os.path.exists(os.path.join(self.dirsesion,'sesion.pkl')):
            choice = QtWidgets.QMessageBox.question(self, 'Guardar Sesión',
                                            "¿Desea sobreescribir los datos de la sesión?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                serializo_y_guardo( self.mojones, os.path.join(self.dirsesion,'sesion.pkl') )
                self.eventos_sesion_modificado = False
                logger.info('[guardar_sesion] Ya existe el archivo sesion.pkl, lo sobreescribo')
            else:
                logger.info('[guardar_sesion] Ya existe el archivo sesion.pkl, NO guardo sesion')
        else:
            serializo_y_guardo( self.mojones, os.path.join(self.dirsesion,'sesion.pkl') )
            self.eventos_sesion_modificado = False
        
    def seleccion_parametro(self):
        #print 'seleccione ',       self.lstParametros.currentItem().text()
        parametro = self.lstParametros.currentItem().text()
        self.actualizar_parametros(self.lstParametros.currentItem().text())
        
    def actualizar_parametros(self, parametro_seleccionado):
        print( 'entre a actualizar_parametros con parametro ',parametro_seleccionado)
        self.combValorParam.clear()
        for item in dict_parametros:
            if item == parametro_seleccionado:
                if dict_parametros[item][0] == False:
                    self.lnValorParam.setEnabled(False)
                else:
                    self.lnValorParam.setEnabled(True)
                for parametro in dict_parametros[item][1]:
                    self.combValorParam.addItem(parametro)

    def play(self):
        if not self.AUTOMATICO:
            self.timerPlay.start(self.spinBox.value())
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img_default/player_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tbtnPlay.setIcon(icon)
            self.AUTOMATICO = True
            self.tbtnPlay.setStatusTip('Detener avance automático')
            logger.info('[play] Activo avance automatico')
        else:
            self.stop_automatico()
    
    def stop_automatico(self):
        self.timerPlay.stop()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_default/player_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbtnPlay.setIcon(icon)
        self.AUTOMATICO = False
        self.tbtnPlay.setStatusTip('Comenzar avance automático')
        logger.info('[play] Desactivo avance automatico')
        
    def abrir_sesion2(self):
        dialogo_abrir = MyWindow()
        if  dialogo_abrir.exec_(): # Si accept, devuelve 1, si cancel devuelve 0
            self.dirsesion = dialogo_abrir.filePath_selected
            print( 'tengo despues de abrir: ',self.dirsesion)
            logger.info( '[Abrir Sesion] - Abro carpeta: {}'.format(self.dirsesion))
            if not self.cargar_pickle(self.dirsesion):
                self.mojones = self.crear_lista_mojones(self.dirsesion)
            self.sldrPosicion.setMaximum (len(self.mojones)-1)
            self.sldrPosicion.setMinimum(0)
            if len(self.mojones)/20 >= 1:
                self.sldrPosicion.setPageStep(int(len(self.mojones)/20))
                self.sldrPosicion.setTickInterval(int(len(self.mojones)/20))
            else:
                self.sldrPosicion.setPageStep(5)
                self.sldrPosicion.setTickInterval(1)
            #REINICIAR VISTAS
            #REINICIAR AUTOMATICO
            self.stop_automatico()
            #REINICIAR INDICE
            self.indice = 0
            self.cargar_mojon_gui(self.indice)
            #REINICIAR MODIFICADO SESIONE
            self.MODIFICADO = False
            self.Habilitar_botones(True)
            self.cargar_info(os.path.join(self.dirsesion,'info.txt'))
    
    def abrir_sesion(self):
        dirname = str(QtWidgets.QFileDialog.getExistingDirectory(self, 
                    caption='Seleccionar Sesión',
                    options=QtWidgets.QFileDialog.ShowDirsOnly))
        self.dirsesion = dirname + '/'
        logger.info( '[Abrir Sesion] - Abro carpeta: {}'.format(self.dirsesion))
        if not self.cargar_pickle(self.dirsesion):
            self.mojones = self.crear_lista_mojones(self.dirsesion)
        self.sldrPosicion.setMaximum (len(self.mojones)-1)
        self.sldrPosicion.setMinimum(0)
        #REINICIAR VISTAS
        #REINICIAR AUTOMATICO
        self.stop_automatico()
        #REINICIAR INDICE
        self.indice = 0
        self.cargar_mojon_gui(self.indice)
        #REINICIAR MODIFICADO SESIONE
        self.MODIFICADO = False
        self.Habilitar_botones(True)
        self.info.cargar_info(os.path.join(self.dirsesion,'info.txt'))
        #
    
    def cargar_pickle(self,carpeta):
        if os.path.exists(os.path.join(carpeta,'sesion.pkl')):
            self.mojones = deserializo_y_cargo(os.path.join(carpeta,'sesion.pkl'))
            self.sldrPosicion.setMaximum (len(self.mojones)-1)
            self.sldrPosicion.setMinimum(0)
            logger.info( '[cargar_pickle]Existe archivo sesion.pkl, tonces lo cargo')
            return True
        else:
            logger.info('[cargar_pickle] No existe archivo sesion.pkl')
            return False
        
    
    def crear_lista_mojones(self,carpeta):
        archivos = os.listdir(carpeta)
        if len(archivos) > 4000:
            mensaje = 'Cargar la sesión puede tardar y el programa no responder.\nEsto ocurre solo la primera vez que abre la sesión'
            result = QMessageBox.information(self, 'Espere por favor', mensaje, QMessageBox.Ok , QMessageBox.Ok)
        #borro los q no son imagenes
        for item in archivos[:]:
            if not item.lower().endswith('.jpg'):
                archivos.remove(item)
                continue
            elif not ('__c1__' in item or '__c2__' in item or '__c3__' in item):
                archivos.remove(item)
        lista=[]
        for nombre in archivos:
            progresiva,latitud,longitud,camara = parsear_nombre(nombre)
            if progresiva in lista:
                #print 'ya existe el mojon'
                lista[lista.index(progresiva)].archivos_img[camara] = nombre
                print( lista[lista.index(progresiva)].archivos_img)
            else:
                lista.append(Mojon(progresiva))
                lista[lista.index(progresiva)].archivos_img[camara] = nombre
                lista[lista.index(progresiva)].latitud = latitud
                lista[lista.index(progresiva)].longitud = longitud
                print( lista[lista.index(progresiva)].archivos_img)
            #print lista
        lista.sort(key=lambda x : x.progresiva)
        logger.info('[crear_lista_mojones] Cargue {} mojones'.format(len(lista)))
        return lista

    
    def cargar_mojon_gui(self,indice):
        imagenes =[IMG_DEFAULT,IMG_DEFAULT,IMG_DEFAULT]
        if os.path.isfile(os.path.join(self.dirsesion,self.mojones[indice].archivos_img[0])):
            imagenes[0]=os.path.join(self.dirsesion,self.mojones[indice].archivos_img[0])
        if os.path.isfile(os.path.join(self.dirsesion,self.mojones[indice].archivos_img[1])):
            imagenes[1]=os.path.join(self.dirsesion,self.mojones[indice].archivos_img[1])
        if os.path.isfile(os.path.join(self.dirsesion,self.mojones[indice].archivos_img[2])):
            imagenes[2]=os.path.join(self.dirsesion,self.mojones[indice].archivos_img[2])
        self.lblimg1.actualizar(imagenes[self.pos1])
        self.lblimg2.actualizar(imagenes[self.pos2])
        self.lblimg3.actualizar(imagenes[self.pos3])
        self.setWindowTitle('ANALIZADOR PAVIMENTOS -- REFOCA -- {} -- {}m - Lat:{} Long:{}'.format(self.dirsesion,
            self.mojones[indice].progresiva,
            self.mojones[indice].latitud,
            self.mojones[indice].longitud))
        self.lstEventos.clear()
        for evento in self.mojones[self.indice].eventos:
            evento_texto = '{}m {},{} -- {} {} {}'.format(self.mojones[self.indice].progresiva,
                                                        self.mojones[self.indice].latitud,
                                                        self.mojones[self.indice].longitud,
                                                        evento[0], evento[1], evento[2])
            self.lstEventos.addItem(evento_texto)
        
    
    def btn_Event_Sig(self):
        for ix in range(self.indice+1,len(self.mojones)-1):
            if self.mojones[ix].eventos:
                self.indice = ix
                self.cargar_mojon_gui(self.indice)
                self.sldrPosicion.setValue(self.indice)
                return
        for ix in range(0, self.indice):
            if self.mojones[ix].eventos:
                self.indice = ix
                self.cargar_mojon_gui(self.indice)
                self.sldrPosicion.setValue(self.indice)
                return
        logger.info( 'No hay eventos - btnEventSig')
    
    def btn_Event_Ant(self):
        for ix in range(self.indice-1,-1,-1):
            if self.mojones[ix].eventos:
                self.indice = ix
                self.cargar_mojon_gui(self.indice)
                self.sldrPosicion.setValue(self.indice)
                return
        for ix in range(len(self.mojones)-1, self.indice,-1):
            if self.mojones[ix].eventos:
                self.indice = ix
                self.cargar_mojon_gui(self.indice)
                self.sldrPosicion.setValue(self.indice)
                return
        logger.info( 'No hay eventos - btnEventSig')
    
    def btn_Anterior(self):
        self.lstEventos.clear()
        #foto = self.mojones[self.indice]
        print( 'retrocedo con indice ',self.indice)
        if self.indice == 0 :
            self.indice = (len(self.mojones) -1)
        else:
            self.indice = self.indice - 1
       #self.cargar_eventos_en_ventana()
        self.cargar_mojon_gui(self.indice)
        self.sldrPosicion.setValue(self.indice)
        print( 'nuevo indice', self.indice)

        
    def btn_Siguiente(self):
        #self.lstEventos.clear()
        print( 'avanzo con indice ',self.indice)
        if self.indice >= (len(self.mojones) -1):
            self.indice = 0
        else:
            self.indice = self.indice + 1
        #self.cargar_eventos_en_ventana()
        #self.actualizar_gui(self.indice)
        self.cargar_mojon_gui(self.indice)
        self.sldrPosicion.setValue(self.indice)
        print( 'nuevo indice', self.indice)

    
    def saltar_a_valor(self,valor):
        print( 'slide ()', valor)
        self.indice = valor
        self.cargar_mojon_gui(self.indice)
        #self.actualizar_gui(self.indice)
        print( 'nuevo indice', self.indice)


home = expanduser("~")

def main():
   # global app
    logger.info('---------------------------------------------------')
    logger.info('Inicio Programa Revisador')
    app = QtWidgets.QApplication(sys.argv)
    form = RevisadorApp()
    form.showMaximized()
    print( form.size())
    app.exec_()

if __name__ == '__main__':
    main()
    
