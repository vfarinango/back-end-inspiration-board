from flask import Blueprint, request, jsonify
from ..models.board import Board
from ..models.card import Card
from ..db import db
from .route_helper_methods import validate_model

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

# GET /boards
@bp.route("", methods=["GET"])
def get_boards():
    boards = Board.query.all()
    return jsonify([board.to_dict() for board in boards]), 200

# POST /boards
@bp.route("", methods=["POST"])
def create_board():
    data = request.get_json()
    new_board = Board.from_dict(data)
    db.session.add(new_board)
    db.session.commit()
    return jsonify(new_board.to_dict()), 201

# GET /boards/<board_id>/cards
@bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]
    return jsonify(cards), 200

# POST /boards/<board_id>/cards
@bp.route("/<board_id>/cards", methods=["POST"])
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
    return jsonify(new_card.to_dict()), 201