from fastapi.testclient import TestClient
import pytest


from main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_recommend_items(client):
    k = 10
    item_id = 1
    response = client.post(
        '/recommend',
        json={
            "item_id": item_id,
            "top_k": k
        }
    )
    assert response.status_code == 200
    assert len(response.json()["recommended_items"]) == k


def test_recommend_items_item_id_not_in_data(client):
    k = 3
    item_id = int(1e4)
    response = client.post(
        '/recommend',
        json={
            "item_id": item_id,
            "top_k": k
        }
    )
    assert response.status_code == 404

