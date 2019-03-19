from setuptools import setup, find_packages

setup(
    name='lol',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='Welkom',
    description='EDSA Python hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Njabz-1/lol',
    author='Njabulo Mhlambi',
    author_email='mhlambinjabulo@gmail.com'
)
