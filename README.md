# Game-Review-Library

The fundemental project for QA consulting.

## Index

1. [Brief](#Brief)
2. [Architecture](#Architecture)
3. [Risk Assessment](#Risk-Assessment)
5. [Testing](#Testing)
6. [Workflow and Tools](#Workflow-and-Tools-Used)



## Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules
covered during training.

My decision was to create a game review library where a user may create a collection of games, add or delete games,
and also add them to played games with a rating.

## Architecture

### Entity Relationship Diagram
My initial ERD included Users, Reviews and Games tables. A user would have an ID and this along with the Game ID would be
incorperated as foreign keys in a game review so that it would belong to a user and a certain game. Here is the inital ERD:

![Initial ERD](https://github.com/oskar951/Game-Review-Library/blob/master/Images/GameERD.jpg)

My delivered ERD has only the Games and Reviews tables, this time with more rows that have all the necessary fields. Because I am not including a users table, I have insead decided to add first and last names to the reviews. The relationship between these tables is one to one and zero to many, the Games table will share the ID as a foregin key in the reviews table. Here is my final ERD:

![Final ERD](https://github.com/oskar951/Game-Review-Library/blob/master/Images/FinalGameERD.jpg)

## Risk Assessment


## Testing

In my inital test to see the response code for my pages(home, about, addgames, games, review) to see if those pages are shown to the user. All the tests passed with a total coverage of 55%

## Workflow and Tools Used


SQL - Database service
Python - Logic
Jenkins - Continues Integration and Deployment service
PyTest - Testing
Git - Versions Control System
Trello - Project Tracking
GCP - Virtual Environment

