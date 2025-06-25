from flask import Blueprint, request
from ..models.board import Board
from ..models.card import Card
from ..db import db
from .route_helper_methods import validate_model, create_model_response 

bp = Blueprint("board_bp", __name__, url_prefix="/boards") 

# GET /boards - list all boards
@bp.get("")
def get_boards():
    query = db.select(Board)
    boards = db.session.scalars(query.order_by(Board.board_id))
    boards_response = [board.to_dict() for board in boards]
    return boards_response, 200

# POST /boards - create a new board
@bp.post("")
def create_board():
    request_body = request.get_json()
    return create_model_response(Board, request_body) 

# GET /boards/<board_id> - get one board by ID
@bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200

# PUT /boards/<board_id> - update a board by ID
@bp.put("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()
    board.update(data) 
    db.session.commit()
    return board.to_dict(), 200

# DELETE /boards/<board_id> - delete a board by ID
@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return {"details": f"Board {board_id} deleted"}, 200

# List all cards for a board
@bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]
    return cards, 200

# Create a new card for a board
@bp.post("/<board_id>/cards")
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()
    new_card = Card(
        message=data["message"],
        likes_count=data["likes_count"],
        board_id=board.board_id
    )
    db.session.add(new_card)
    db.session.commit()
    return new_card.to_dict(), 201
