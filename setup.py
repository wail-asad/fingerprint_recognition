from distutils.core import setup
from setuptools import find_packages
import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(name="fingerprint_recognition", install_requires=install_requires,version='1.1',
      packages=find_packages(),)

# setup(name='fingerprint_recognition',
#       version='1.0',
#       packages=find_packages(),
#      )