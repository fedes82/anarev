# -*- coding: UTF-8 -*-
version = '1.2'
##PARA EL GUI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore
import sys
import interface
#### para crear el python que hace falta para cargar el archivo que crea 
#### el qtdesigner usar:
####  pyuic5 test.ui -o interface.py
#### con test.ui es el archivo qtdesigner
#### y interface.py el que importo en el main
    

###---------------------------------------------------PARA LOGGEAR

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('revisador.log')
handler_traceback = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(processName)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


def handle_exception(exc_type, exc_value, exc_traceback):
    """para sacar el traceback por el logger"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
# add the handlers to the logger
logger.addHandler(handler_traceback)
logger.addHandler(handler)

####---------------------------------------------------FIN LOGGEAR


##GRAL
import os
import os.path
import copy
from collections import defaultdict
import json
import zipfile
import tempfile
import csv
import re
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED
#PIL imports
from PIL import Image as PILImage
from shutil import rmtree, copy2
from urllib.request import urlopen
import urllib.request
from urllib.error import URLError, HTTPError

DEBUG = True


 ## asi veo si hay objeto 'whatever en la lista'
 ##any(obj.string == 'whatever' for obj in mylist)
### para crear json a partir de lista:y de objetos##
### transformando cada objeto en un diccionario
## json_string = json.dumps([ob.__dict__ for ob in y] )


IMG_DEFAULT = 'img_default/imgDefault.jpg'
JSON_MAPAS = 'maps.json'

     
##esto es el dialogo para Configurar servidor/llave/zoom de los mapas
## esta creado desde el archvio maps.py, genereado con maps.ui
## y lo meti todo aca por que era mas facilito
## - puse el __init__ a mano y 
##  cambie algunas cosas, comparar para ver q.
class DialogoConfMapas(QtWidgets.QDialog):

    def __init__(self, ConfMapas ,parent=None):
        super(DialogoConfMapas, self).__init__(parent)
        self.ConfMapas = ConfMapas
        self.setObjectName("diagConfMapas")
        self.resize(559, 249)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbBING = QtWidgets.QRadioButton(self.groupBox)
        self.rbBING.setObjectName("rbBING")
        self.verticalLayout_2.addWidget(self.rbBING)
        self.rbGMAPS = QtWidgets.QRadioButton(self.groupBox)
        self.rbGMAPS.setObjectName("rbGMAPS")
        self.verticalLayout_2.addWidget(self.rbGMAPS)
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
        self.rbGMAPS.raise_()
        self.lnKEY.raise_()
        self.label.raise_()
        self.rbBING.raise_()
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.btnGuardar = QtWidgets.QPushButton(self)
        self.btnGuardar.setEnabled(False)
        self.btnGuardar.setCheckable(False)
        self.btnGuardar.setFlat(False)
        self.btnGuardar.setObjectName("btnGuardar")
        self.horizontalLayout_3.addWidget(self.btnGuardar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sBoxZoom = QtWidgets.QSpinBox(self.groupBox_2)
        self.sBoxZoom.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sBoxZoom.setMaximum = 20
        self.sBoxZoom.setMinimum = 1
        self.sBoxZoom.setObjectName("sBoxZoom")
        self.horizontalLayout.addWidget(self.sBoxZoom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sBoxZoom.raise_()
        self.label_2.raise_()
        self.sBoxZoom.raise_()
        self.label_2.raise_()
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi()
        
        
        #Cargo datos
        with open(JSON_MAPAS,'r') as archivo_conf_maps:
            temp = json.loads(archivo_conf_maps.read())
        if self.ConfMapas['llave'] ==  temp['llave']:
            self.lnKEY.setPlaceholderText(self.ConfMapas['llave'])
        else:
            self.lnKEY.setText(self.ConfMapas['llave'])
            self.btnGuardar.setEnabled(True)
            
        if self.ConfMapas['servicio']=='BING':
            self.rbBING.setChecked(True)
        if self.ConfMapas['servicio']=='GoogleMaps':
            self.rbGMAPS.setChecked(True)
        self.sBoxZoom.setValue(int(self.ConfMapas['zoom']))
        
        # CONNECTS
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.sBoxZoom.valueChanged.connect(self.cambio_zoom)
        self.lnKEY.textEdited.connect(self.edite_la_key)
        self.btnGuardar.clicked.connect(self.guardar_configuracion)
        self.rbBING.toggled.connect(self.cambio_server)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def cambio_server(self):
        self.btnGuardar.setEnabled(True)
        if self.rbBING.isChecked():
            self.ConfMapas['servicio'] = 'BING'
        if self.rbGMAPS.isChecked():
            self.ConfMapas['servicio'] = 'GoogleMaps'
        
    def edite_la_key(self):
        self.btnGuardar.setEnabled(True)
        self.ConfMapas['llave']=self.lnKEY.text()
    
    def guardar_configuracion(self):
        with open(JSON_MAPAS,'r') as archivo_conf_maps:
            temp = json.loads(archivo_conf_maps.read())
        if self.ConfMapas['llave'] !=  temp['llave']:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("¡Está seguro que desea sobreescribir\nlos datos del servicio?")
            msg.setInformativeText("Este cambio no se podra deshacer")
            msg.setWindowTitle("Confirmar")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            retval = msg.exec_()
            if retval == QtWidgets.QMessageBox.Ok:
                with open(JSON_MAPAS,'w') as arch:
                    arch.write(json.dumps(self.ConfMapas))
                logger.info('[CONF_MAPAS] Guardo nueva configuracion (KEY) en maps.json: {}'.format(self.ConfMapas))
        else:
            with open(JSON_MAPAS,'w') as arch:
                arch.write(json.dumps(self.ConfMapas))
            logger.info('[CONF_MAPAS] Guardo nueva configuracion (NO KEY) en maps.json: {}'.format(self.ConfMapas))
        self.btnGuardar.setEnabled(False)
    
    def cambio_zoom(self):  
        self.btnGuardar.setEnabled(True)
        self.ConfMapas['zoom'] = str(self.sBoxZoom.value())
        
    
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("diagConfMapas", "Configuracion del servidor de mapas"))
        self.groupBox.setTitle(_translate("diagConfMapas", "Proveedor"))
        self.rbBING.setText(_translate("diagConfMapas", "BING Maps"))
        self.rbGMAPS.setText(_translate("diagConfMapas", "Google Maps"))
        self.label.setText(_translate("diagConfMapas", "Llave (API KEY)"))
        self.btnGuardar.setText(_translate("diagConfMapas", "Guardar Cambios"))
        self.label_2.setText(_translate("diagConfMapas", "Zoom Predeterminado"))


class Mojon:
    """Objeto base mojon, contine la info de cada uno"""
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
        if not l[-1].mapas : l[-1].mapas = ['','']
        l[-1].archivos_img = d['archivos_img']
        l[-1].eventos = d['eventos']
    print ('cargue: ',len(l),' eventos')
    return l
    
    

class RevisadorApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    global DEBUG   
    global version
    eventos_sesion = defaultdict(list)
    indice =0
    mojones = []
    mostrar_ppal = 0
    
    def __init__(self, parent=None):
        super(RevisadorApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(QPixmap('img_default/icono.ico')))
        self.lblimg1.actualizar(IMG_DEFAULT)
        self.lblimg2.actualizar(IMG_DEFAULT)
        self.lblimg3.actualizar(IMG_DEFAULT)
        self.lblimg4.actualizar(IMG_DEFAULT)
        self.lblimg5.actualizar(IMG_DEFAULT)
        self.lblimgppal.actualizar(IMG_DEFAULT)
        self.lblimg1.mousePressEvent = self.sel_img1
        self.lblimg2.mousePressEvent = self.sel_img2
        self.lblimg3.mousePressEvent = self.sel_img3
        self.lblimg4.mousePressEvent = self.sel_img4
        self.lblimg5.mousePressEvent = self.sel_img5
        self.btnAnterior.clicked.connect(self.btn_Anterior)
        self.btnSiguiente.clicked.connect(self.btn_Siguiente)
        self.btnGetMap.clicked.connect(self.btn_GetMap)
        self.spinBoxZoom.valueChanged.connect(self.cambio_zoom)
        self.actionSalir.setStatusTip('Salir de la aplicacion')
        self.actionSalir.triggered.connect(self.salir)
        self.actionAbrir.setShortcut('Ctrl+A')
        self.actionAbrir.setStatusTip('Abrir sesion')
        self.actionAbrir.triggered.connect(self.abrir_sesion)
        self.actionExportar_Map.triggered.connect(self.exportar_map)
        self.actionExportar_Img.triggered.connect(self.exportar_img)
        self.actionExportar_CSV.triggered.connect(self.exportar_csv)
        self.actionExportar_Todo.triggered.connect(self.exportar_todo)
        self.actionConfigurarMapas.triggered.connect(self.configurar_mapa)
        self.actionAcerca_de.triggered.connect(self.mostrar_version)
        self.MODIFICADO = False
        self.setWindowTitle('VISUALIZADOR -- REFOCA')
        #cargo configuracion de descarga de mapas
        if os.path.exists(JSON_MAPAS):
            with open(JSON_MAPAS,'r') as archivo_conf_maps:
                self.conf_maps = json.loads(archivo_conf_maps.read())
            self.spinBoxZoom.setValue(int(self.conf_maps['zoom']))
            self.MAPS_JSON_NO_ENCONTRADO = False
        else:
            self.conf_maps ={"servicio": "BING", "llave": "Ingrese LLAVE", "zoom": 17} 
            with open(JSON_MAPAS,'w') as archivo_conf_maps:
                archivo_conf_maps.write(json.dumps(self.conf_maps))
            self.spinBoxZoom.setValue(int(self.conf_maps['zoom']))
            logger.warning('[ init__RevisadorAPP] No se encontro maps.json. Se crea uno con valores por defecto')
            self.MAPS_JSON_NO_ENCONTRADO = True
            
        logger.info('__init__ ok')
    
    def sel_img1(self,event):
        if os.path.isfile(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[0])):
            self.lblimgppal.actualizar(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[0]))
        else:
            self.lblimgppal.actualizar(IMG_DEFAULT)
        self.mostrar_ppal = 0
    
    def sel_img2(self,event):
        if os.path.isfile(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[1])):
            self.lblimgppal.actualizar(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[1]))
        else:
            self.lblimgppal.actualizar(IMG_DEFAULT)
        self.mostrar_ppal = 1
    
    def sel_img3(self,event):
        if os.path.isfile(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[2])):
            self.lblimgppal.actualizar(os.path.join(self.dirtemp ,  self.mojones[self.indice].archivos_img[2]))
        else:
            self.lblimgppal.actualizar(IMG_DEFAULT)
        self.mostrar_ppal = 2
    
    def sel_img4(self,event):
        if os.path.isfile(os.path.join(self.dirtemp ,  self.mojones[self.indice].mapas[0])):
            self.lblimgppal.actualizar(os.path.join(self.dirtemp ,  self.mojones[self.indice].mapas[0]))
        else:
            self.lblimgppal.actualizar(IMG_DEFAULT)
        self.mostrar_ppal = 3
    
    def sel_img5(self,event):
        if os.path.isfile(os.path.join(self.dirtemp ,  self.mojones[self.indice].mapas[1])):
            self.lblimgppal.actualizar(os.path.join(self.dirtemp ,  self.mojones[self.indice].mapas[1]))
        else:
            self.lblimgppal.actualizar(IMG_DEFAULT)
        self.mostrar_ppal = 4
    
    
    def abrir_sesion(self):
        #antes de abrir ver si hay que borrar tempdir
        archivo_anax = QtWidgets.QFileDialog.getOpenFileName(self, 'Seleccione archivo ANAX', '','*.anax')[0]
        print('anax: ',archivo_anax)
        if archivo_anax:
            logger.info('[Abrir sesion] Abro archivo {}'.format( archivo_anax ))
        else:
            return
        self.archivo_anax = archivo_anax
        self.dirtemp = tempfile.mkdtemp() + '/'
        print ('Cree el dir temporal: ',self.dirtemp)
        #abrir el anax
        if zipfile.is_zipfile(archivo_anax):
            zip = zipfile.ZipFile(archivo_anax)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            info = 'El archivo seleccionado no es un archivo de sesion .anax valido'
            msg.setText(info)
            msg.setWindowTitle('Archivo no valido')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            print( 'no es anax, mostrar popup con error')
            return
        #descomprimir el anax
        zip.extractall(self.dirtemp)
        if not self.cargar_pickle(self.dirtemp):
            print( 'fallo carga de pickle')
            self.mojones = self.crear_lista_mojones(self.dirtemp)
        #crear lista de eventos - imagenes
        self.indice = 0 
        #self.cargar_nuevo_objeto_evento(self.indice_actual)
        self.cargar_mojon_gui(self.indice)
        self.MODIFICADO = False
        logger.info('abrir_sesion ok')
    
    def cargar_pickle(self,carpeta):
        if os.path.exists(os.path.join(carpeta,'analizador.pkl')):
            logger.info( '[cargar_pickle] Existe archivo sesion.pkl en carpeta: {} tonces lo cargo'.format(carpeta))
            self.mojones = deserializo_y_cargo(os.path.join(carpeta,'analizador.pkl'))
            print( self.mojones)
            return True
        else:
            print( '[cargar_pickle] No existe archivo sesion.pickle')
            return False
        
    
    def crear_lista_mojones(self,carpeta):
        """Crea Lista de Objetos Mojon:
            lista todos los archivos (path) de 'carpeta' y remueve
            los que NO terminan en .jpg y los que NO comienzan con
            '__c1__' , '__c2__' , '__c3__' 
        """
        print( 'entre en crear lista mojones')
        archivos = os.listdir(carpeta)
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
                if len(lista) <50:
                    print( 'primer arch de este mojon',progresiva)
                lista.append(Mojon(progresiva))
                lista[lista.index(progresiva)].archivos_img[camara] = nombre
                lista[lista.index(progresiva)].latitud = latitud
                lista[lista.index(progresiva)].longitud = longitud
                print( lista[lista.index(progresiva)].archivos_img)
            #print lista
        lista.sort(key=lambda x : x.progresiva)
        
        return lista

    def validar_coordenadas(self,mojon):
        if mojon.latitud == '-' or mojon.longitud == '-':
            return False
        else:
            return True
    
    def mostrar_version(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        info = 'Version: ' + version
        info += '\nContacto: fedes82@gmail.com'
        msg.setText(info)
        msg.setWindowTitle("Acerca de Refoca - Revisador")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
     
    def cambio_zoom(self):
        self.conf_maps['zoom'] = self.spinBoxZoom.value()
        
    def btn_GetMap(self):
        """Descarga dos mapas desde GMaps o BING (diagrama y imagen satelital).
        agrega en el header del request 'req' que se identifica como 'Mozilla/5.0',
        por compatibilidad con GMaps.
        los guarda en un archivo de nombre 0010map.png y 0010maph.png , para 0010m de progresiva).
        """
        ERRORSERVER = False
        ERRORKEY = False
        
        if not self.validar_coordenadas(self.mojones[self.indice]):
                logger.info( '[GetMap] - Valor de coordenadas no valido para prog: {}'.format(self.mojones[self.indice]) )
                return
                
        if self.conf_maps['servicio'] == 'GoogleMaps':
            gmaps = 'http://maps.googleapis.com/maps/api/staticmap?center={},{}&markers={},{}&zoom=12&size=640x360&&maptype=hybrid&key={}'.format(
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['llave'])
            logging.info(' [btn_GetMap] descargo {}'.format(gmaps))
            req = urllib.request.Request(gmaps, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                url = urllib.request.urlopen(gmaps)
                nombre = os.path.join(self.dirtemp,self.mojones[self.indice].progresiva+'maph.png')
                with open(nombre,'wb') as arch:
                    arch.write(url.read())
                
                self.mojones[self.indice].mapas[1] = self.mojones[self.indice].progresiva + 'maph.png'
            except HTTPError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] The server couldn\'t fulfill the request.Error code: {}'.format(e.code))
                ERRORKEY = True
            except URLError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] We failed to reach a server.Reason: {}'.format( e.reason))
                ERRORSERVER = True
            
            gmaps = 'http://maps.googleapis.com/maps/api/staticmap?center={},{}&markers={},{}&zoom=12&size=640x360&&maptype=roadmap&key={}'.format(
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['llave'])
            req = urllib.request.Request(gmaps, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                url = urllib.request.urlopen(req)
                nombre = os.path.join(self.dirtemp,self.mojones[self.indice].progresiva+'map.png')
                with open(nombre,'wb') as arch:
                    arch.write(url.read())
                self.mojones[self.indice].mapas[0] = self.mojones[self.indice].progresiva + 'map.png'
                print( 'tengo mapa guardado en:',self.mojones[self.indice].mapas[0])
            except HTTPError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] The server couldn\'t fulfill the request.Error code: {}'.format(e.code))
                ERRORKEY = True
            except URLError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] We failed to reach a server.Reason: {}'.format( e.reason))
                ERRORSERVER = True

        
        if self.conf_maps['servicio']  == 'BING':
            gmaps = "http://dev.virtualearth.net/REST/v1/Imagery/Map/Road/{},{}/{}?ms=640,360&pp={},{};127&mapLayer=Basemap,Buildings&fmt=png&key={}".format(
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['zoom'],
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['llave'] )
            print( gmaps)
            req = urllib.request.Request(gmaps, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                url = urllib.request.urlopen(req)
                nombre = os.path.join(self.dirtemp,self.mojones[self.indice].progresiva+'map.png')
                with open(nombre,'wb') as arch:
                    arch.write(url.read())
                self.mojones[self.indice].mapas[1] = self.mojones[self.indice].progresiva + 'maph.png'
                
                
            except HTTPError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] The server couldn\'t fulfill the request.Error code: {}'.format(e.code))
                ERRORKEY = True
            except URLError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] We failed to reach a server.Reason: {}'.format( e.reason))
                ERRORSERVER = True
            
            gmaps = "http://dev.virtualearth.net/REST/v1/Imagery/Map/AerialWithLabels/{},{}/{}?ms=640,360&zoomLevel=10&pp={},{};127&mapLayer=Basemap,Buildings&fmt=png&key={}".format(
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['zoom'],
                self.mojones[self.indice].latitud,
                self.mojones[self.indice].longitud,
                self.conf_maps['llave'] )
            req = urllib.request.Request(gmaps, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                url = urllib.request.urlopen(req)
                nombre = os.path.join(self.dirtemp,self.mojones[self.indice].progresiva+'maph.png')
                with open(nombre,'wb') as arch:
                    arch.write(url.read())
                self.mojones[self.indice].mapas[0] = self.mojones[self.indice].progresiva + 'map.png'
                print( 'tengo mapa guardado en:',self.mojones[self.indice].mapas[0])
                
            except HTTPError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] The server couldn\'t fulfill the request.Error code: {}'.format(e.code))
                ERRORKEY = True
            except URLError as e:
                logger.warning('[btn_GetMap] {}'.format(gmaps))
                logger.warning('[btn_GetMap] We failed to reach a server.Reason: {}'.format( e.reason))
                ERRORSERVER = True
                
        if ERRORKEY:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No se pudo descargar mapa")
            msg.setInformativeText("El servidor no puede responder.\n Verifique la llave (API KEY).\n")
            msg.setWindowTitle("Descargar mapa")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            retval = msg.exec_()
            return
        if ERRORSERVER:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No se pudo descargar mapa")
            msg.setInformativeText("El servidor no puede ser encontrado.\nVerifique su conexion a Internet.")
            msg.setWindowTitle("Descargar mapa")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            retval = msg.exec_()
            return
        
        self.cargar_mojon_gui(self.indice)
        self.MODIFICADO = True
        
    def cargar_mojon_gui(self,indice):
        """Carga en pantalla:
            -Cada una de las imágenes a mostrar, luego de decidir su posicion.
            -La tabla con las observaciones.
            -Titulo de la ventana 
        """
        attrs = vars(self.mojones[indice])
        print( ', '.join("%s: %s" % item for item in attrs.items()))
        imagenes =[IMG_DEFAULT,IMG_DEFAULT,IMG_DEFAULT,IMG_DEFAULT,IMG_DEFAULT]
        print( 'cargoar mojon img0 ',self.mojones[indice].archivos_img[0])
        print( self.dirtemp+self.mojones[indice].archivos_img[0])
        if os.path.isfile(self.dirtemp+self.mojones[indice].archivos_img[0]):
            imagenes[0]=self.dirtemp+self.mojones[indice].archivos_img[0]
        if os.path.isfile(self.dirtemp+self.mojones[indice].archivos_img[1]):
            imagenes[1]=self.dirtemp+self.mojones[indice].archivos_img[1]
        if os.path.isfile(self.dirtemp+self.mojones[indice].archivos_img[2]):
            imagenes[2]=self.dirtemp+self.mojones[indice].archivos_img[2]
        if os.path.isfile(self.dirtemp+self.mojones[indice].mapas[0]):
            print( 'trato de cargar en gui :', self.dirtemp+self.mojones[indice].mapas[0])
            imagenes[3]=self.dirtemp+self.mojones[indice].mapas[0]
        if os.path.isfile(self.dirtemp+self.mojones[indice].mapas[1]):
            imagenes[4]=self.dirtemp+self.mojones[indice].mapas[1]
        self.lblimg1.actualizar(imagenes[0])
        self.lblimg2.actualizar(imagenes[1])
        self.lblimg3.actualizar(imagenes[2])
        self.lblimg4.actualizar(imagenes[3])
        self.lblimg5.actualizar(imagenes[4])
        
        self.lblimgppal.actualizar(imagenes[self.mostrar_ppal])
        
        #lleno tabla
        self.tablaEventos.setRowCount(len(self.mojones[indice].eventos))
        prog = self.mojones[indice].progresiva
        lat = self.mojones[indice].latitud
        long = self.mojones[indice].longitud
        for i, evento in enumerate(self.mojones[indice].eventos):
            #parsear evento
            parametro, categoria, valor = evento[0],evento[1],evento[2]
            self.tablaEventos.setItem(i, 0, QTableWidgetItem(prog)) 
            self.tablaEventos.setItem(i, 1, QTableWidgetItem(lat)) 
            self.tablaEventos.setItem(i, 2, QTableWidgetItem(long)) 
            self.tablaEventos.setItem(i, 3, QTableWidgetItem(parametro)) 
            self.tablaEventos.setItem(i, 4, QTableWidgetItem(categoria))
            self.tablaEventos.setItem(i, 5, QTableWidgetItem(valor))
        
        self.setWindowTitle('VISUALIZADOR -- REFOCA -- {}m - Lat: {} Long: {} \t\tObservacion {} de {}'.format(prog,lat,long,indice+1,len(self.mojones)))
    logger.info('cargar_mojon_gui ok')
    
    def parsear_nombre(self,nom_img):
        """toma el nombre como parametro y devuelve
        progresiva,latitud,longitud"""
        progresiva = nom_img[:6]
        #por compatibilidad hacia atras
        if nom_img.endswith('MARCA.jpg'):
            nom_img = nom_img[:-8]
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
        return progresiva,lat,long
    
    def btn_Siguiente(self):
        if self.indice >= len(self.mojones)-1:
            self.indice = 0
        else:
            self.indice +=1
        print( 'nuevo indice',self.indice)
        self.cargar_mojon_gui(self.indice)
    
    def btn_Anterior(self):
        if self.indice == 0:
            self.indice = len(self.mojones)-1
        else:
            self.indice -= 1
        print( 'nuevo indice',self.indice)
        self.cargar_mojon_gui(self.indice)
    
    def guardar_sesion(self):
        if os.path.exists(os.path.join(self.dirtemp,'analizador.pkl')):
            choice = QtWidgets.QMessageBox.question(self, 'Guardar Sesion',
                                            "¿Desea sobreescribir los daros de la sesion?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                serializo_y_guardo( self.mojones, os.path.join(self.dirtemp,'analizador.pkl') )
                self.MODIFICADO = False
            ### creo nuevo ANAX (zip) con los nuevos archivos
                with zipfile.ZipFile(self.archivo_anax,'w') as zip:
                    for file in os.listdir(self.dirtemp):
                            print( file)
                            zip.write(self.dirtemp+file,arcname=file,compress_type=compression)
                print( 'guarde ',self.archivo_anax)
            else:
                pass
        else:
            #serializo_y_guardo( self.mojones, os.path.join(self.dirtemp,'sesion.pkl') )
            #self.eventos_sesion_modificado = False
            logger.info( '[guardar_sesion] error feo, no deberia nunca llegar aca [guardar sesion no encontro analizador.pkl]')
    

    def exportar_img(self):
        dirdest_img = QtWidgets.QFileDialog.getExistingDirectory(self, 
                    caption='Seleccionar Carpeta destino',
                    options=QtWidgets.QFileDialog.ShowDirsOnly)
        if dirdest_img:
            dirdest_img = dirdest_img + '\\'
            logger.info( '[Exportar img] - Exporto imagenes a: {}'.format(dirdest_img))
        else:
            return
        for mojon in self.mojones:
                for imagen in mojon.archivos_img:
                    if imagen:  #puede haber menos de tres imagenes
                        #pop up espere
                        print( 'copio imagen: ',imagen)
                        print( 'copio desde',os.path.join(self.dirtemp,imagen),'hasta',dirdest_img)
                        copy2(os.path.join(self.dirtemp,imagen),dirdest_img)
                        #cierro popup
                    else:
                        print( 'no habia imagen en mojon: ',mojon)
            
    def exportar_map(self):
        dirdest_map = QtWidgets.QFileDialog.getExistingDirectory(self, 
                    caption='Seleccionar Carpeta destino',
                    options=QtWidgets.QFileDialog.ShowDirsOnly)
        print( 'dirdest_map vale:', dirdest_map)
        if dirdest_map:
           # dirdest_map =os.path.join(dirdest_map ,'\\')
            dirdest_map += '\\'
            logger.info( '[Exportar map] - Exporto mapas a: {}'.format(dirdest_map))
        else:
            return
        for mojon in self.mojones:
            for mapa in mojon.mapas:
                print( 'tengo accesso ', os.access(os.path.join(self.dirtemp,mapa), os.R_OK ))
                print( 'ampa: ',mapa, 'nombre largo:',len(mapa))
                if mapa:    #puede haber descargado o no los mapas
                    print( 'copio desde',os.path.join(self.dirtemp,mapa),'hasta',dirdest_map)
                    copy2(os.path.join(self.dirtemp,mapa),dirdest_map)
    
    def exportar_csv(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Ingrese nombre y destino', filter='*.csv')[0]
        if fileName:
            logger.info('[Exportar CSV] Guardo .csv en archivo {}'.format( fileName) )
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
                print( 'mojon ', mojon)
                for evento in mojon.eventos:
                    print( 'evento:',evento)
                    print( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento)
                    writer.writerow( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento)
                
    
    def exportar_todo(self):
        dirdest_todo = QtWidgets.QFileDialog.getExistingDirectory(self, 
                    caption='Seleccionar Carpeta destino',
                    options=QtWidgets.QFileDialog.ShowDirsOnly)
        if dirdest_todo:
#            dirdest_todo = os.path.join(dirdest_todo , '\\')
            #dirdest_todo += '\\'
            logger.info( '[Exportar todo] - Exporto imagenes a: {}'.format(dirdest_todo))
        else:
            return
        mojones_a_exportar = []
        for mojon in self.mojones[:]:
            if  mojon.eventos:
                mojones_a_exportar.append(mojon)
        ## Exporto CSV
        with open(os.path.join(dirdest_todo, 'informe.csv'),'w',newline='') as f:  #es necesario el modo binario por que usa \n\r para nueva linea y con 'w' solo queda un espacio de mas
            writer = csv.writer(f)
            writer.writerow( ['Dist Progresiva','Latitud','Longitud','Parametro','Categoria','Valor'])
            for mojon in mojones_a_exportar:
                print( 'mojon ', mojon)
                for evento in mojon.eventos:
                    print( 'evento:',evento)
                    print( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento)
                    writer.writerow( [mojon.progresiva]+[mojon.latitud] +[mojon.longitud] + evento)
        for mojon in mojones_a_exportar:        
            ### Exporto mapas
            for mapa in mojon.mapas:
                print( 'tengo accesso ', os.access(os.path.join(self.dirtemp,mapa), os.R_OK ))
                print( 'mapa: ',mapa, 'nombre largo:',len(mapa))
                if mapa:
                    copy2(os.path.join(self.dirtemp,mapa),dirdest_todo)
            ### Exoporto imagenes
            for imagen in mojon.archivos_img:
                #pop up espere
                if imagen:
                    copy2(os.path.join(self.dirtemp,imagen),dirdest_todo)
                #cierro popup
    
    def configurar_mapa(self):
        dialogo = DialogoConfMapas(self.conf_maps)
        dialogo.exec_()
        if dialogo.accepted:
            print('cambie config, acepte')
            self.spinBoxZoom.setValue(int(self.conf_maps['zoom']))
    
    def closeEvent(self, event):
        print( "User has clicked the red x on the main window")
        self.salir()
    
    def salir(self):
        mensaje = 'El archivo ANAX ha sido modificada\n¿Desea guardar los cambios antes de salir?'
        if self.MODIFICADO:
            choice = QtWidgets.QMessageBox.question(self, 'Guardar Sesion',
                                            mensaje,
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.guardar_sesion()
        try:
            if self.dirtemp:
                rmtree(self.dirtemp)
        except:
            print( 'no habia dirtemp o algo asi')
        QtWidgets.qApp.quit()

####-------------------------------%%%%%%%%%%%%###########-----------------------
def main():
    logger.info('---------------------------------------------------')
    logger.info('Inicio Programa Revisador')
    app = QtWidgets.QApplication(sys.argv)
    form = RevisadorApp()
    form.showMaximized()
    if form.MAPS_JSON_NO_ENCONTRADO:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("No se encontro el archivo 'maps.json'")
        msg.setInformativeText("Se crea archivo por defecto.\nIngrese los datos en el menu COnfigurar Mapa")
        msg.setWindowTitle("Configura Mapa")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
        msg.exec_()
    print( form.size())
    
    app.exec_()

if __name__ == '__main__':
    main()
    logger.info('Cierro Programa Revisador')
    logger.info('*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/***/*/')
