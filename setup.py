from setuptools import find_packages, setup

setup(
    name='mrisim',
    version='1.0',
    author='Arnaud Desvachez',
    author_email='arnaud.desvachez@gmail.com',
    license='The GNU General Public License',
    description='Simulates the MRI triggers to test protocols',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        'pynput',
    ]
)