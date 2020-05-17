# Game-Review-Library

The fundemental project for QA consulting.

## Index

1. [Brief](#Brief)
2. [Architecture](#Architecture)



## Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules
covered during training.

My decision was to create a game review library where a user may create a collection of games, add or delete games,
and also add them to played games with a rating.

## Architecture

### Entity Relationship Diagram
My initial ERD included Users, Reviews and Games tables. A user would have an ID and this along with the Game ID would be
incorperated as foreign keys in a game review so that it would belong to a user and a certain game.
