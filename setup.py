#!/usr/bin/env python

from distutils.core import setup, Extension

pykeyfinder_module = Extension('_pykeyfinder',
                               language="c++",
                               sources=['pykeyfinder_wrap.cxx'],
                               libraries=['keyfinder'],
                               extra_compile_args=['-std=c++11']
                               )

setup(name='pykeyfinder',
      version='0.1',
      author="ains",
      description="""Simple SWIG wrapper around libKeyFinder""",
      ext_modules=[pykeyfinder_module],
      py_modules=["pykeyfinder"],
      )
