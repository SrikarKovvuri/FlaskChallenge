import pytest
from app import create_app

@pytest.fixture
def srikars_fixture():
    return "Hello"

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()