from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory data so tests do not leak state into each other."""
    baseline = deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline))
