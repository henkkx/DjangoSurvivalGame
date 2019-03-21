#Scribbles From Another Dimensions


Description:
The purpose of this web application is to provide an interface for a
game of search and survival. The game is as follows:

The goal of the game is to survive in a post-apocalyptic town by searching houses for food and supplies as well as fighting enemies when necessary. 

On any particular street in the town, there are a number of houses and the player can choose to enter a house. Each house has rooms. The player can enter the rooms to search them for different items. However, these rooms may also be occupied by other humans or creatures that may or may not be hostile. Depending on the case, the player may choose to 1) talk to them and recruit them to the player's party or 2) to enter combat.

When entering combat, the player may 1) attack or 2) try to run. Fleeing from combat might end succesfully, in which case the players leaves the house, or unsuccesfully, in which case the player is forced to stay in combat.

Winning a fight grants experience points and allows the player to loot whatever is left in the room.
Losing a fight might result in losing party members and/or health.

Each action in the game costs time. The day ends when
the player runs out of time. At the end of the day, the amount of food is decreased
food depending on the size of the party. If there is not enough food, then party members
might leave. Party size and food is updated after every day.

Players get exp both passively by surviving and actively by winning fights. Players get different badges based on their exp, and their exp is also shown on the leaderboards. 
 

Specifications:
Players need to be able to:
- create an account and profile
- view, edit, update and maintain their profile
- start a game and return back to a game in progress.
- Play the game according to the mechanics described above
- View the leaderboard

Visitors to the site:
- Need to be able to view the leaderboard
- Read the instructions of the game
- Be able to register

## Installing / Getting started

Python 3.5 or greater is required.

```shell
pip install -r requirements.txt
python DjangoSurvivalGame/manage.py runserver
```

These commands will install all the required python modules and begin the Django webserver.

## Developing

### Built With
Bootstrap CSS, jQuery, Javascript, AJAX, JSON, Python

### Prerequisites
https://www.python.org/downloads/

## Tests

### Running Tests
```shell
python manage.py test
```

## Database

SQLite 





