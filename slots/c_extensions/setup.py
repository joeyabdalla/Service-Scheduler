from setuptools import setup, Extension
import operations


module = Extension('operations',
                  sources = ['operations_module.c', 'operations.c'])

setup(name = 'Operations',
      version = '1.0',
      description = 'Python bindings for basic operations',
      ext_modules = [module])

result = operations.multiply(5, 4)
print(result)