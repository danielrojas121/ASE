import app as one
import pytest

@pytest.fixture
def app():
    return one.APP

@pytest.fixture
def client(app):
	client = app.test_client()
	return client