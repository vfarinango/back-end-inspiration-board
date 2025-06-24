from app.models.card import Card
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Card(
        card_id=1,
        message="Be happy!",
        likes_count=5,
        board_id=1
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["card_id"] == 1
    assert result["message"] == "Be happy!"
    assert result["likes_count"] == 5
    assert result["board_id"] == 1

def test_to_dict_missing_id():
    # Arrange
    test_data = Card(
        message="Be happy!",
        likes_count=5,
        board_id=1
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["card_id"] is None
    assert result["message"] == "Be happy!"
    assert result["likes_count"] == 5
    assert result["board_id"] == 1

def test_to_dict_missing_message():
    # Arrange
    test_data = Card(
        card_id=1,
        likes_count=5,
        board_id=1
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["card_id"] == 1
    assert result["message"] is None
    assert result["likes_count"] == 5
    assert result["board_id"] == 1

def test_to_dict_missing_likes_count():
    # Arrange
    test_data = Card(
        card_id=1,
        message="Be happy!",
        board_id=1
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["card_id"] == 1
    assert result["message"] == "Be happy!"
    assert result["likes_count"] is None
    assert result["board_id"] == 1

def test_from_dict_required_properties_only_returns_card():
    # Arrange
    card_data = {
        "message": "Be happy!",
        "likes_count": 5,
        "board_id": 1
    }

    # Act
    new_card = Card.from_dict(card_data)

    # Assert
    assert new_card.message == "Be happy!"
    assert new_card.likes_count == 5
    assert new_card.board_id == 1

def test_from_dict_with_no_message():
    # Arrange
    card_data = {
        "likes_count": 5,
        "board_id": 1
    }

    # Act & Assert
    with pytest.raises(KeyError, match='message'):
        new_card = Card.from_dict(card_data)

def test_from_dict_with_no_likes_count():
    # Arrange
    card_data = {
        "message": "Be happy!",
        "board_id": 1
    }

    # Act & Assert
    with pytest.raises(KeyError, match='likes_count'):
        new_card = Card.from_dict(card_data)

def test_from_dict_with_no_board_id():
    # Arrange
    card_data = {
        "message": "Be happy!",
        "likes_count": 5
    }

    # Act & Assert
    with pytest.raises(KeyError, match='board_id'):
        new_card = Card.from_dict(card_data)

def test_from_dict_with_extra_keys():
    # Arrange
    card_data = {
        "message": "Be happy!",
        "likes_count": 5,
        "board_id": 1,
        "extra": "some stuff",
        "another": "last value"
    }

    # Act
    new_card = Card.from_dict(card_data)

    # Assert
    assert new_card.message == "Be happy!"
    assert new_card.likes_count == 5
    assert new_card.board_id == 1
