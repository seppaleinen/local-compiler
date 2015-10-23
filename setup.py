from setuptools import setup
    
setup(
    name='local-compiler',
    version='1.0.0',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=[ 'lib' ],
    url='http://seppaleinen.github.io/local-compiler',
    zip_safe=False,
    license='GPLv3',
    description='Common library for managing version-control and compiling.',
    install_requires=[
        "gitPython==1.0.1"
    ],
    tests_require=[
        "gitPython==1.0.1"
    ],
    test_suite='tests',
)
