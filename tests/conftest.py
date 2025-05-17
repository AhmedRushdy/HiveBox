import pytest
import os

@pytest.fixture(autouse=True)
def clean_env():
    """Clean up environment variables before each test"""
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)
