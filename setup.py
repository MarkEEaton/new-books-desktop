from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = ['convert.py'],
    zipfile = None,
)
