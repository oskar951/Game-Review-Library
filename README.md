# Game-Review-Library

The fundemental project for QA consulting.

## Index

1. [Brief](#Brief)
2. [Architecture](#Architecture)
3. [Risk Assessment](#Risk-Assessment)
5. [Testing](#Testing)
6. [Front End Design/Result](#Front-End-Design/Result)
7. [Workflow and Tools](#Workflow-and-Tools-Used)
8. [Future Improvements](#Improvements-to-Make-in-the-Future)



## Brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules
covered during training.

My decision was to create a game review library where a user may create a collection of games, add or delete games,
and also add them to reviews with a rating.

## Architecture


### Entity Relationship Diagram
My initial ERD included Users, Reviews and Games tables. A user would have an ID and this along with the Game ID would be
incorperated as foreign keys in a game review so that it would belong to a user and a certain game. Here is the inital ERD:

![Initial ERD](https://github.com/oskar951/Game-Review-Library/blob/master/Images/GameERD.jpg)

My delivered ERD has only the Games and Reviews tables, this time with more rows that have all the necessary fields. Because I am not including a users table, I have insead decided to add first and last names to the reviews. The relationship between these tables is one to one and zero to many, the Games table will share the ID as a foregin key in the reviews table. Here is my final ERD:

![Final ERD](https://github.com/oskar951/Game-Review-Library/blob/master/Images/FinalGameERD.jpg)

[Back to top](#Index)

### CI Pipeline
Here is my continuous integration and deployment pipeline showcasing the process my project takes from the testing and source code being used, then pushed to the github version control system. This is updated in my project tracking Trello board and Jenkins the CI server is looking for changes in github and pulling the code to then automatically build it and deploy to the live environment.

![CI Pipeline](https://github.com/oskar951/Game-Review-Library/blob/master/Images/CIpipeline2.jpg)

### Trello Project Tracking

Using Trello, I tracked my project along the way with a Kanban style board which allowed me to see my progress and things that need to be done. I added a colour code for MoSCoW so that the must have content is green, this way you can see all the green must have items have progressed to the 'Done' column. I also have some Bugs and one of them has a fix in the card description which helped me get over the problem. User stories and a Use case were also included here.


![Trello Board](https://github.com/oskar951/Game-Review-Library/blob/master/Images/TrelloBoard.jpg)

## Risk Assessment

In my risk assessment I have listed possible risks of the software and risks I may run into within the project itself. I added the risks cause and effect as well as the likelihood of it happening, this is then followed by a control measure which can help negate the risk and give it a lower likelihood and consequence. 

I then reviewed my risks towards the end of the project to see which control measures are implemented and whether I avoided those risks or not.

![Risk Assessment](https://github.com/oskar951/Game-Review-Library/blob/master/Images/RiskAssessment.jpg)

## Testing

In my inital testing to see the response code for my pages(home, about, addgames, games, review) to see if those pages are shown to the user. All the tests passed with a total coverage of 55%

Adding some more tests got me to 86% with more testing needed on forms and routes.
![Test coverage1](https://github.com/oskar951/Game-Review-Library/blob/master/Images/CoverageReport1.jpg)

My final test coverage is at 89% with some website routes still needing testing. Tests have been made which add data to database and return the page with that data to show integration of databases.

![Test coverage2](https://github.com/oskar951/Game-Review-Library/blob/master/Images/CoverageReport2.jpg)

## Front End Design/Result

For the front end of the website I created 2 wire frames of the expected and minimum desired outcome. The frames are simple and white, including the page links and review positions as well as the form layout.

![Home page wireframe](https://github.com/oskar951/Game-Review-Library/blob/master/Images/HomePageWireframe.jpg)
![Add review wireframe](https://github.com/oskar951/Game-Review-Library/blob/master/Images/AddReviewWireframe.jpg)

### Front End Result

The final coutcome of the front end looks much nicer and actually has more functionality than expected. The greyed out review is indicating a mouseover event to show that the review actually is a link and when hovered over can be clicked. This then goes to a new page for that specific review where you can delete or update it, the layout here is the same as the home page below but it shows the review ID at the top of the page and has update and delete buttons.

![Home page](https://github.com/oskar951/Game-Review-Library/blob/master/Images/homepage.jpg)
![Review page](https://github.com/oskar951/Game-Review-Library/blob/master/Images/reviewpage.jpg)

[Back to top](#Index)

## Workflow and Tools Used

Here is a workflow for creating the app:

![WorkFlow](https://github.com/oskar951/Game-Review-Library/blob/master/Images/WorkFlow.jpg)

* SQL - Database service
* Python - Logic
* Flask - Front End (HTML)
* Jenkins - Continues Integration and Deployment server
* PyTest - Testing
* Git - Versions Control System
* Trello - Project Tracking
* GCP - Cloud Server

## Improvements to Make in the Future

Fulle testing coverage is something I would like to improve on for next time.

To further build on the project I would like to implement validation when writing a review for a game that doesnt exist so that the user is notified to create a review with a game from the database. 

I would also like to implement users and logins so that reviews may be linked to accounts and even have a sort of social network between eachother for forums and discussions. This would also include user profiles and the reviews that they have made.

A great addition would be to have a page for upcoming game releases which could show what games people are most excited for so others can look forward to them.

Some functionality for the project I have included in my project tracking using MoSCoW showing which things I could have and things I definitely wont have by the end of the project, these are what I decided could be improvements for next time.

## Acknowledgements

Thanks to the Trainers for the knowledge used to build and document this project.

Also thanks to my cohort for all learning together and being a great group.


**Written and Produced by** - *Oskaras Ceremnovas* 

##### Copyright (c)
*2020 QA Academy Training - All rights reserved*
