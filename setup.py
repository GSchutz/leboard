from distutils.core import setup
from os.path import abspath, dirname, join, isfile
from setuptools import find_packages

if isfile('leboard/VERSION'):
    with open('leboard/VERSION', 'r') as f:
        VERSION = f.read()
else:
    VERSION = "0"

with open(join(abspath(dirname(__file__)), 'README.rst'), encoding='utf-8') as file:
    description = file.read()

setup(name='leboard',
      version=VERSION,
      description="Le Board, a simple leaderboard generator for ranking your algorithms experiments",
      long_description=description,
      keywords=['leaderboard', 'ranking', 'models'],
      author='GSchutz',
      author_email='guilherme@gschutz.com',
      url='https://github.com/GSchutz/leboard',
      download_url='https://github.com/GSchutz/leboard/archive/{}.tar.gz'.format(VERSION),
      packages=find_packages(),
      package_data={'leboard': ['VERSION']},
      include_package_data = True,
      install_requires=[
          'docopt>=0.6.2',
          'firebase-admin==2.10.0',
          'google-cloud-firestore>=0.29.0',
          'numpy>=0.1.14',
      ],
      entry_points={
          'console_scripts': ['leboard=leboard.cli:main']
      },
      )
