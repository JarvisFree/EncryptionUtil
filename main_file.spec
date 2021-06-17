# -*- mode: python -*-

block_cipher = None

a = Analysis(['E:\code\my\Encryption\control\control.py'], # 入口py文件
             pathex=['E:\code\my\Encryption\control'], # 入口py文件所在路径
             binaries=[],
             datas=[
                 ('D:\jour.ico','.'), # 添加的资源文件（“.” 表示把e.db这个资源 添加到与生成的exe文件所在的路径中）
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,   # 这里是True
          name='GX数据加解密', # 生成的exe文件名称（不含后缀）
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='D:\jour.ico') # 生成的exe文件logo图（需ico格式）

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='GX数据加解密')  # 生成的exe文件 所在的文件夹名称