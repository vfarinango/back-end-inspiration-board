import pytest
from app import create_app
from app.db import db
from app.models.board import Board
from app.models.card import Card

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def clean_db(app):
    with app.app_context():
        db.session.remove()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

@pytest.fixture
def one_saved_board():
    board = Board(title="Test Board", owner="Tester")
    db.session.add(board)
    db.session.commit()
    return board

@pytest.fixture
def one_saved_card(one_saved_board):
    card = Card(
        message="Inspire someone today!",
        likes_count=0,
        board_id=one_saved_board.board_id
    )
    db.session.add(card)
    db.session.commit()
    return card