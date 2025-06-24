from app.models.board import Board
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Board(board_id=1, title="My Board", owner="Aigerim")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["board_id"] == 1
    assert result["title"] == "My Board"
    assert result["owner"] == "Aigerim"

def test_to_dict_missing_id():
    # Arrange
    test_data = Board(title="My Board", owner="Aigerim")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["board_id"] is None
    assert result["title"] == "My Board"
    assert result["owner"] == "Aigerim"

def test_to_dict_missing_title():
    # Arrange
    test_data = Board(board_id=1, owner="Aigerim")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["board_id"] == 1
    assert result["title"] is None
    assert result["owner"] == "Aigerim"

def test_to_dict_missing_owner():
    # Arrange
    test_data = Board(board_id=1, title="My Board")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["board_id"] == 1
    assert result["title"] == "My Board"
    assert result["owner"] is None

def test_from_dict_returns_board():
    # Arrange
    board_data = {"title": "My Board", "owner": "Aigerim"}

    # Act
    new_board = Board.from_dict(board_data)

    # Assert
    assert new_board.title == "My Board"
    assert new_board.owner == "Aigerim"

def test_from_dict_with_no_title():
    # Arrange
    board_data = {"owner": "Aigerim"}

    # Act & Assert
    with pytest.raises(KeyError, match='title'):
        new_board = Board.from_dict(board_data)

def test_from_dict_with_extra_keys():
    # Arrange
    board_data = {
        "extra": "not needed",
        "title": "My Board",
        "owner": "Aigerim",
        "another": "value"
    }

    # Act
    new_board = Board.from_dict(board_data)

    # Assert
    assert new_board.title == "My Board"
    assert new_board.owner == "Aigerim"
