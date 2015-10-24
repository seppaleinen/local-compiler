from setuptools import setup
    
setup(
    name='local-compiler',
    version='0.1.0',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=[ 'lib' ],
    url='http://seppaleinen.github.io/local-compiler',
    zip_safe=False,
    license='GPLv3',
    description='Common library for managing version-control and compiling.',
    install_requires=[
        "gitPython==1.0.1",
        "setuptools==18.4",
        "enum34==1.0.4",
    ],
    tests_require=[
        "gitPython==1.0.1",
        "pep8==1.6.2",
        "mock==1.3.0",
    ],
    test_suite='tests',
)
