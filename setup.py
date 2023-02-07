from setuptools import setup
from torch.utils import cpp_extension

setup(name='today_is_aggregation',
      ext_modules=[cpp_extension.CppExtension('today_is_aggregation', ['main.cpp'])],
      license='Apache License v2.0',
      cmdclass={'build_ext': cpp_extension.BuildExtension})