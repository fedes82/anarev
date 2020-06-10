# REVISADOR REFOCA
Este programa permite revisar los informes creados con el programa ANALIZADOR REFOCA y exportar los mismos (fotos, imagenes satelitales e informes en formato cvs)

Empaquetado para correr en Windows 7 64bits.

## Para crear distribución:
----
- Ejecutar `
pyinstaller revisador.py --hidden-import PyQt5.sip
`
- Editar `revisador.spec`, agregando las carpetas con datos *('source', 'destino')* en linea datas en lista `Analisis`
`datas=[('img_default','img\_default'),],`

- agregar icono y sacar consola en linea 'console' del grupo EXE:
`console=False , icon='img_default\\icono.ico')`

- ejecutar `pyinstaller revisador.spec`
----
## CHANGELOG
### [1.2.1] - 2020-06-09
* bugs 
  * fix error con 'ingrese llave' cuando crea url para bajar mapas
* added
   * cree este README.md y el changelog aca dentro


### [1.2] -  2020-06-08

* added
  * menu 'Mapas->configurar' dialog
  * ingresar llave
  * elejir servidor BING o GMaps
  * chequear respuesta por 404 o errores de conexion
  * agregar botones zoom
  * agregar configuracion llave y servicio bing o gmaps

* bug
  * fix [SECURITY] borre la API KEY del programa, ahora se lee desde el archivo 'maps.json'

### [1.1] - 2018-10-08

* Version funcionando, sin registros anteriores