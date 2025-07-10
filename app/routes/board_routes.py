from flask import Blueprint, request
from ..models.board import Board
from ..models.card import Card
from ..db import db
from .route_helper_methods import validate_model, create_model_response 

bp = Blueprint("board_bp", __name__, url_prefix="/boards") 

@bp.get("")
def get_boards():
    query = db.select(Board)
    boards = db.session.scalars(query.order_by(Board.board_id))
    boards_response = [board.to_dict() for board in boards]
    return boards_response, 200


@bp.post("")
def create_board():
    request_body = request.get_json()
    return create_model_response(Board, request_body) 


@bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200


@bp.put("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()
    board.update(data) 
    db.session.commit()
    return board.to_dict(), 200


@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return {"details": f"Board {board_id} deleted"}, 200


@bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]
    return cards, 200


@bp.post("/<board_id>/cards")
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()
    new_card = Card(
        message=data["message"],
        likes_count=data.get("likes_count", 0),
        board_id=board.board_id
    )
    db.session.add(new_card)
    db.session.commit()
    return new_card.to_dict(), 200
