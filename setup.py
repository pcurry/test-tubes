from setuptools import find_packages
from setuptools import setup



setup(
    name='test_tubes',
    version='0.0.1',
    author='Paul Curry',
    author_email='pcurry@gmail.com',
    description='Small Flasks for testing',
    install_requires=['Flask==1.1.1'],
    packages=find_packages(),
)
