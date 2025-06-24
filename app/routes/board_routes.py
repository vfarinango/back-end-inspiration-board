from flask import Blueprint, request, jsonify
from ..models.board import Board
from ..models.card import Card
from ..db import db
from .route_helper_methods import validate_model

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

# GET /boards - list all boards
@bp.get("")
def get_boards():
    boards = Board.query.all()
    return [board.to_dict() for board in boards], 200

# POST /boards - create a new board
@bp.post("")
def create_board():
    data = request.get_json()
    new_board = Board.from_dict(data)
    db.session.add(new_board)
    db.session.commit()
    return new_board.to_dict(), 201

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
    if "title" in data:
        board.title = data["title"]
    if "owner" in data:
        board.owner = data["owner"]
    db.session.commit()
    return board.to_dict(), 200

# DELETE /boards/<board_id> - delete a board by ID
@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return {"details": f"Board {board_id} deleted"}, 200