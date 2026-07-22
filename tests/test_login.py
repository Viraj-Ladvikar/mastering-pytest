import pytest


def test_login(browser,base_url):

    assert base_url == "http://127.0.0.1:8000"
    assert browser == "Chrome"