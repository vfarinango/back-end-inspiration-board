from flask import abort, Blueprint, make_response, Response, request, jsonify
from ..db import db
from app.models.board import Board

bp = Blueprint("boards_bp", __name__, url_prefix="/boards")
