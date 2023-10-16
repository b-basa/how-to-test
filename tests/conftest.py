import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    # pytest provides a monkeypatch fixture to replace values and behaviors
    # In this example, Any test that calls requests.get() will raise a RuntimeError
    # Source: https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())