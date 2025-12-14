# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Добавляем все ресурсы
        ('assets/icons/asset-management.ico', 'assets/icons'),
        ('assets/icons/categories/*', 'assets/icons/categories'),
        ('assets/icons/sidebar/*', 'assets/icons/sidebar'),
        ('assets/icons/*.ico', 'assets/icons'),
        ('assets/icons/*.png', 'assets/icons'),
        # Добавьте другие ресурсы если нужно
        # ('assets/fonts/*', 'assets/fonts'),
    ],
    hiddenimports=[
        'customtkinter',
        'PIL',
        'PIL._imaging',
        'sqlalchemy',
        'sqlalchemy.dialects.postgresql',
        'matplotlib',
        'matplotlib.backends.backend_tkagg',
        'numpy',
        'CustomTkinterMessagebox',  # если используете
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=None,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Установлено в False для --noconsole
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icons/asset-management.ico'],  # Путь к иконке
)