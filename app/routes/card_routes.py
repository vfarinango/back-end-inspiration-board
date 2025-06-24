from flask import Blueprint, request
from ..db import db
from app.models.card import Card
from .route_helper_methods import validate_model


bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return {"details": f"Card {card_id} deleted"}, 200


@bp.patch("/<card_id>/like")
def like_card(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    db.session.commit()
    return card.to_dict(), 200


@bp.put("/<card_id>")
def update_card(card_id):
    card = validate_model(Card, card_id)
    data = request.get_json()
    card.update(data)
    db.session.commit()
    return card.to_dict(), 200