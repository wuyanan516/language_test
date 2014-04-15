# mysetup.py
from distutils.core import setup
import py2exe

setup(service=["WindowsService"],
	options = {
                  'py2exe': {
                      'packages':['encodings'],
                  }
              },
	)