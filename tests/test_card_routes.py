import pytest
from app.models.card import Card


def test_delete_card_not_found(client):
    response = client.delete("/cards/999")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "not found" in response_body["details"].lower()


def test_like_card(client, one_saved_card):
    
    original_likes = one_saved_card.likes_count

    response = client.patch(f"/cards/{one_saved_card.card_id}/like")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["likes_count"] == original_likes + 1


def test_like_card_not_found(client):
    response = client.patch("/cards/999/like")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "not found" in response_body["details"].lower()


def test_update_card(client, one_saved_card):
    updated_data = {
        "message": "Updated message",
        "likes_count": 5
    }

    response = client.put(f"/cards/{one_saved_card.card_id}", json=updated_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["message"] == "Updated message"
    assert response_body["likes_count"] == 5


def test_update_card_not_found(client):
    data = {"message": "New message", "likes_count": 2}
    response = client.put("/cards/999", json=data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert "not found" in response_body["details"].lower()