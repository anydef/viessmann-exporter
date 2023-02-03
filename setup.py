from setuptools import find_packages, setup

setup(name='viessmann_exporter',
      version='1.0',
      description='Python Distribution Utilities',
      author='Pavlo Fedyna',
      author_email='fed.pavlo@gmail.com',
      install_requires=['PyViCare', 'Flask', 'prometheus-client', 'APScheduler'],
      packages=find_packages(),
      )
