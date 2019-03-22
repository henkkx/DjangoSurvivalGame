# Scribbles From Another Dimensions


## Description:

The purpose of this web application is to provide an interface for a
game of search and survival. The game is as follows:

The goal of the game is to survive in a Mysterious town by searching houses for food and supplies as well as fighting enemies when necessary. 

On any particular street in the town, there are a number of houses and the player can choose to enter a house. Each house has rooms. The player can enter the rooms to search them for different items. However, these rooms may also be occupied by other humans or creatures that may or may not be hostile. Depending on the case, the player may choose to 1) talk to them or 2) to enter combat.

Winning a fight grants experience points and allows the player to loot whatever is left in the room.
Losing a fight might result in losing health or resulting in a GAME OVER for the player.

Each action in the game costs time. When a player leaves a building. At the end of the day, the amount of food is decreased. 
If there is not enough food, then player may die from hunger

Players get exp actively by winning fights. Players get different badges based on their exp, and their exp is also shown on the leaderboards. 
 

## Specifications:
### The Logged On Users Are Able To Access These Features :
   
   View, update and maintain their profile
   Start a game and return back to a game in progress.
   Play the game according to the mechanics described above
   View the leader board & Other Player Stats
   
### Not Logged In Users Can:
   
   Are able to view the main leader board
   Read the instructions of the game
   Register


## Installing / Getting started

Python 3.5 or greater is required.

Navigate Into The Directory That Contains manage.py

```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations Game
python manage.py migrate
python population_script.py populate
python manage.py runserver
```

These commands will install all the required python modules and begin running the Django webserver.

### Remember

If you are running this on a local server, set Debug to True in settings.py as otherwise
the Django framework won't load the static files.

This will also disable the 404 request page, However on python anywhere debug is set to False,
because python anywhere will handle the static links

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





