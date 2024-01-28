import PyInstaller.__main__

PyInstaller.__main__.run([
    'backend.py',
    '--onedir',
    '--clean',
    '--hide-console=minimize-early',
    '--name=STEP',
    '--debug=all',

])