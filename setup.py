import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.12'
PACKAGE_NAME = 'ValidatePhysicalAddressesColombia'
AUTHOR = 'Felipe Duenas, Ivan Sierra'
AUTHOR_EMAIL = 'andres.sierra03@uptc.edu.co'
URL = 'https://github.com/ItsAiz/Analizador-Sem-ntico-Direcciones-rurales-y-urbanas-Colombia.git'
LICENSE = 'UPTC'
DESCRIPTION = 'Librería para leer direcciones fisicas Colombianas desde un txt y validar si son correctas o no'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"



INSTALL_REQUIRES = [
      'regex'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)