from distutils.core import setup, Extension

module = Extension('myModule', sources = ['myModule.c'])

setup(name='packageName',
      version = '1.0',
      description = 'This is a package for my module.',
      ext_modules = [module])
