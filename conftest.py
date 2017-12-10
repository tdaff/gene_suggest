# Test configuration setup for pytest
import pytest

from gene_suggest.__main__ import create_app


# fixture required by pytest-flask that provides
# the app interface to any classes that require it
@pytest.fixture
def app():
    flask_app = create_app()
    flask_app.debug = True
    return flask_app
