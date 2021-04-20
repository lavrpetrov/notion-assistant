#!/usr/bin/env python

from distutils.core import setup
from pathlib import Path

setup(name='SimpleTaskRepeater',
      version='0.1.0',
      description='Simple Task Repeater',
      author='Petr Lavrov',
      author_email='calmquant@gmail.com',
      url='https://github.com/calmquant/simple-task-repeater',
      packages=['simple_task_repeater'],
      long_description=Path('README.md').read_text(),
      install_requires=Path('requirements.txt').read_text().split()
      )
