from setuptools import setup
from distutils.command.install import install
import os


class SkipInstall(install):
    # Skips install
    def run(self):
        skip = True

    
setup(
    name='test',
    version='0.1.0',
    cmdclass={'install': SkipInstall},
)
