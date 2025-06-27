# Inspiration Board: Back-end Layer

This scaffold includes the following:

## `app/__init__.py`

This file configures the app. We expect developers to modify this file by:
- Importing all models
- Importing `db` and `migrate` from a separate file that manages creating the `SQLAlchemy` and `Migrate` instances
- Initializing the app with the `SQLAlchemy` and `Migrate` instances
- Importing and registering all blueprints

Prior projects like `Solar System`, `Flasky`, and [`hello-books-api`](https://github.com/AdaGold/hello-books-api) are great resources to reference for project structure and set up needs.

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `tests`

This folder only contains an empty `__init__.py` file. Developers are expected to:
- create a `conftest.py` file to set up their app and any necessary test data for testing
- create test files for any model or route tests

## `requirements.txt`

This file lists the dependencies we anticipate are needed for the project.

## `.gitignore`

This is a hidden file which lists specific files and file extension types that should be ignored by the git repo when looking for changed files to stage.

## Database name: inspiration_board

Table name: board
Columns:

board_id, int, primary key
title, string
owner, string
Table name: card
Columns:

card_id, int, primary key
message, string
likes_count, int
board_id, int, foreign key to board_id in board
This implies that there are two models:

Board
Card

API Documentation for Boards/Cards

Base URL:  https://back-end-inspiration-board-97fl.onrender.com


Boards Endpoints:

Path
Method
Body
Response(ex) 200
Status Code 400/404
/boards
get
-
[{"board_id": 1, "owner": "Bob", "title": "First"}, {...}]


/boards
post
{"owner": "Bob", "title": "First"}
{"board_id": 1, "owner": "Bob", "title": "First"}
{
  "details": "Board id abc is invalid"
}
{
  "details": "Invalid data"
}
{
  "details": "Board with id 999 not found"
}


/boards/<board_id>


get
-

{"board_id": 1, "owner": "Bob", "title": "First"}

/boards/<board_id>
put
{"owner": "Bob", "title": "Updated Title"}
{"board_id": 1, "owner": "Bob", "title": "Updated Title"}


/boards/<board_id>
delete
-
{"details": "Board 1 deleted"}


/boards/<board_id>/cards
get
-
[{"card_id": 1, "message": "Hello!", "likes_count": 0, "board_id": 1}, {...}]


/boards/<board_id>/cards
post
{"message": "New card", "likes_count": 0}
{"card_id": 2, "message": "New card", "likes_count": 0, "board_id": 1}



 Cards Endpoints:

Path
Method
Body
Response(ex) 200
400/404
/cards/<card_id>
delete
-
{"details": "Card 2 deleted"}
{
  "details": "Board id abc is invalid"
}
{
  "details": "Invalid data"
}
{
  "details": "Board with id 999 not found"
}
/cards/<card_id>/like
patch
-
{"card_id": 2, "message": "Nice!", "likes_count": 1, "board_id": 1}


/cards/<card_id>
put
{"message": "Updated!", "likes_count": 2}
{"card_id": 2, "message": "Updated!", "likes_count": 2, "board_id": 1}



