import os
import sys
import pytest

# Add the parent directory to Python path for importing app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import print_version

def test_print_version(capsys):
    """Test print_version when APP_VERSION is set"""
    os.environ["APP_VERSION"] = "v.1.0.0"
    print_version()
    captured = capsys.readouterr()
    assert "App Version: v.1.0.0" in captured.out

def test_print_version_not_set(capsys):
    """Test print_version when APP_VERSION is not set"""
    if "APP_VERSION" in os.environ:
        del os.environ["APP_VERSION"]
    print_version()
    captured = capsys.readouterr()
    assert "App Version: Unknown" in captured.out
