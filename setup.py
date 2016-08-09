from distutils.core import setup
from Cython.Build import cythonize

setup(
	name = 'CCA' ,
	ext_modules = cythonize("test1.pyx"),
)