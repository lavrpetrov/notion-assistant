#!/usr/bin/env python

from distutils.core import setup
from pathlib import Path

setup(name='NotionAssistant',
      version='0.1.0',
      description='Notion Assistant',
      author='Lavr Petrov',
      author_email='lavrpetrovmain@gmail.com',
      url='https://github.com/lavrpetrov/notion-assistant',
      packages=['notion_assistant'],
      long_description=Path('README.md').read_text(),
      install_requires=Path('requirements.txt').read_text().split()
      )
