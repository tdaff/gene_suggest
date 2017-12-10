"""
Install information
"""

from setuptools import setup, find_packages

setup(name='gene_suggest',
      version='1.0.0',
      description='',
      long_description=open('README.rst').read(),
      author='Tom Daff',
      author_email='tomdaff@cantab.net',
      license='BSD',
      url='https://github.com/tdaff/gene_suggest/',
      packages=find_packages(exclude=['tests']),
      entry_points={
          'console_scripts':
              ['gsd = gene_suggest.__main__:main']},
      package_data={
          'gene_suggest': ['templates/*.html']},
      install_requires=['flask', 'sqlalchemy', 'pymysql'],
      extras_require={'test': ['pytest']},
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: BSD License'])

