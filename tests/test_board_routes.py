import pytest
from app.models.board import Board

def test_create_one_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Foodie Board",
        "owner": "Aigerim"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Foodie Board",
            "owner": "Aigerim"
        }
    }

def test_create_one_board_missing_title(client):
    # Arrange
    data = {"owner": "Aigerim"}

    # Act
    response = client.post("/boards", json=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid data"}


def test_create_one_board_with_extra_keys(client):
    data = {
        "title": "Motivational Board",
        "owner": "Max",
        "extra": "should be ignored"
    }

    response = client.post("/boards", json=data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Motivational Board",
            "owner": "Max"
        }
    }


def test_get_all_boards_one_saved_board(client, one_saved_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["title"] == one_saved_board.title
    assert response_body[0]["owner"] == one_saved_board.owner

def test_get_all_boards_no_saved_board(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_board(client, one_saved_board):
    # Act
    response = client.get(f"/boards/{one_saved_board.board_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["board_id"] == one_saved_board.board_id
    assert response_body["title"] == one_saved_board.title
    assert response_body["owner"] == one_saved_board.owner

def test_update_board(client, one_saved_board):
    # Act
    response = client.put(f"/boards/{one_saved_board.board_id}", json={
        "title": "Updated Title",
        "owner": "New Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["title"] == "Updated Title"
    assert response_body["owner"] == "New Owner"

def test_delete_board(client, one_saved_board):
    # Act
    response = client.delete(f"/boards/{one_saved_board.board_id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "deleted" in response_body["details"]

    # Confirm it is gone
    get_response = client.get(f"/boards/{one_saved_board.board_id}")
    assert get_response.status_code == 404

def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/999")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert "not found" in response_body["details"].lower()
