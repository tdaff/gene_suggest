FROM python:3.6

MAINTAINER Tom Daff "tomdaff@cantab.net"

# source tree
ADD . /opt/src/gene_suggest
WORKDIR /opt/src/gene_suggest

# Ensures that pytest is also installed
RUN pip install .[test]

# Stop images being buit if tests fail
RUN pytest -vv

# Default Flask port
EXPOSE 5000

CMD gsd
