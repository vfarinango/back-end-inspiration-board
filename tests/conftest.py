import pytest
from app import create_app
from app.db import db

@pytest.fixture
def app():
    # Create a fresh app for testing
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_saved_board(app):
    from app.models.board import Board

    board = Board(title="Test Board", owner="Tester")
    db.session.add(board)
    db.session.commit()
    return board
