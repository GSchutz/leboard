from distutils.core import setup
from os.path import abspath, dirname, join

from setuptools import find_packages

with open('VERSION', 'r') as f:
    VERSION = f.read()

with open(join(abspath(dirname(__file__)), 'README.md'), encoding='utf-8') as file:
    description = file.read()

setup(name='leboard',
      version=VERSION,
      description=description,
      keywords = ['leaderboard', 'ranking', 'models'],
      author='GSchutz',
      author_email='guilherme@gschutz.com',
      url = 'https://github.com/GSchutz/leboard',
      download_url = 'https://github.com/GSchutz/leboard/archive/{}.tar.gz'.format(VERSION),
      packages=find_packages(),
      entry_points={
          'console_scripts': ['leboard=leboard.cli:main']
      },
     )
