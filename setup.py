from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1.0',
    description='A simple calculator package for Turing College.',
    long_description="Displayed on the project's GitHub page.",
    url='https://github.com/egluma/calculator',
    author='Egle Cepuliene',
    author_email='egle.martisauskaite@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests*'])
)
