#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from src.pyapp import Config

cfg = Config()
cryptoKey = cfg.cryptoKey    # 对Python字节码加密
name = cfg.appName    # 项目名称
version = cfg.appVersion    # 版本号


# spec配置文件 前半部分通用格式
def common():
    return f'''
# 对Python字节码加密
block_cipher = pyi_crypto.PyiBlockCipher(key='{cryptoKey}')

added_files = [
    ('./gui', 'gui'),
]

a = Analysis(['./src/index.py'],
             pathex=['./dist'],
             binaries=None,
             datas=added_files,
             hiddenimports=['clr'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
'''


def macos():
    return f'''
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='{name}',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        target_arch=None,  # x86_64, arm64, universal2
        codesign_identity=None,
        entitlements_file=None)
coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='{name}')
app = BUNDLE(coll,
            name='{name}'+'.app',
            version='{version}',
            icon='./src/assets/logo.icns',
            bundle_identifier=None)
'''


def linux():
    return f'''
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='{name}',
          debug=False,
          strip=True,
          upx=True,
          console=False ) # set this to see error output of the executable
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='{name}')
'''


def windows():
    return f'''
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='{name}',
          debug=False,
          strip=True,
          icon='.\\src\\assets\\logo.ico',
          upx=True,
          console=False ) # set this to see error output of the executable
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='{name}')
'''


# 生成 spec 配置文件
specDir = os.path.dirname(__file__)

# build-macos.spec
with open(os.path.join(specDir, 'build-macos.spec'), 'w+', encoding='utf-8') as f:
    f.write(common() + macos())

# build-linux.spec
with open(os.path.join(specDir, 'build-linux.spec'), 'w+', encoding='utf-8') as f:
    f.write(common() + linux())

# build-windows.spec
with open(os.path.join(specDir, 'build-windows.spec'), 'w+', encoding='utf-8') as f:
    f.write(common() + macos())
