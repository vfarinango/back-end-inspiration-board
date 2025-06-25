from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        response = {"details": f"{cls.__name__} id {model_id} is invalid"}
        abort(make_response(response, 400))
    pk_column = cls.__mapper__.primary_key[0]
    query = db.select(cls).where(pk_column == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"details": f"{cls.__name__} with id {model_id} not found"}
        abort(make_response(response, 404))

    return model


def create_model_instance(cls, data):
    try:
        new_instance = cls.from_dict(data)
    except KeyError:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))

    db.session.add(new_instance)
    db.session.commit()

    return new_instance


def create_model_response(cls, data):
    new_instance = create_model_instance(cls, data)
    key = cls.__name__.lower()
    return {key: new_instance.to_dict()}, 201
