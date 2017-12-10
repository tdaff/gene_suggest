gene_suggest
============

Autocompletion for gene names as an API pulling data from ENSEMBL:
https://www.ensembl.org/

This is a small flask application that provides a single endpoint
``gene_suggest`` that responds to a query with suggestions for
complete gene names. Full documentation of the interface is
provided in the ``APIDOCS.md`` file.

Installation
------------

The application is written in python and depends on:

- Python (tested with 2.7 and 3.6)
- flask
- sqlalchemy
- pymysql (for mysql, other sql drivers may work)
- pytest and pytest-flask (for testing only)

When installing with pip these will be pulled in automatically, but conda users
may wish to ``conda install`` them first.

Install from the source directory with ``pip install .`` or with
``pip install .[test]`` if you'd like to run the tests. Tests may be run
with the command ``pytest`` in the source directory.

Usage
-----

The service can be started with ``gsd`` or ``python -m gene_suggest``. By
default the service will be accessible on http://localhost:5000/gene_suggest

A demo application is included at the root URL http://localhost:5000/

To connect to a different database, set the URL in the in the ``DBURL``
environment using an address compatible with sqlalchemy.
