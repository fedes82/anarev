# -*- mode: python -*-

block_cipher = None


a = Analysis(['analizador.py'],
             pathex=['C:\\Users\\fedeprueba\\Documents\\GitHub\\anarev\\analizador'],
             binaries=[],
             datas=[('img_default','img_default'),('perfiles','perfiles')],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='analizador',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='img_default\\icono.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='analizador')
