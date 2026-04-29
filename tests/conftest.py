import pytest
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"

@pytest.fixture(scope = "function")
def create_order():
    payload = {
        "id": 1,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2026-04-25T01:55:07.615Z",
        "status": "approved",
        "complete": "true"
    }
    response = requests.post(url = f"{BASE_URL}/store/order", json = payload)
    assert response.status_code == 200
    return response.json()
