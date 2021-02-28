
from Cython.Build import cythonize
from distutils.core import setup, Extension


sources = [
    'judge_prime_number.pyx', 'c_judge_prime_number.c'
]


ext = Extension("judge_prime_number", sources=sources)
setup(name="judge_prime_number", ext_modules=cythonize([ext]))