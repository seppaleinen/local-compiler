from setuptools import setup
from distutils.command.install import install
import os

class PostInstallClean(install):
    # Calls the default run command, then deletes build directories
    def run(self):
        os.system('rm -rf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        install.run(self)
    
setup(
    name='local-compiler',
    version='0.1.0',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=[ 'lib' ],
    url='http://seppaleinen.github.io/local-compiler',
    zip_safe=True,
    license='GPLv3',
    description='Common library for managing version-control and compiling.',
    install_requires=[
        "gitPython==1.0.1",
        "setuptools==19.4",
        "enum34==1.1.2",
    ],
    tests_require=[
        "gitPython==1.0.1",
        "pep8==1.7.0",
        "mock==1.3.0",
    ],
    test_suite='tests',
    cmdclass={'install': PostInstallClean},
)
