from setuptools import setup, find_packages

setup(
    name='lol',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='Welkom',
    description='EDSA Python hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Njabulo Mhlambi',
    author_email='mhlambinjabulo@gmail.com'
)
