NOTES
=====
Notes from brainstorming session 08 Sept 2012

ZONES
-----
* deck
  * hand
  * library
  * discard
  * play
* stockpiles
* trash

CARDS
-----
* money: copper, silver, gold
* victory: estate, duchy, province
* card class methods
  * money()
  * VPs()
  * cost()
  * name()
  * value()

TURN OPERATIONS
---------------
Commands menu:
1. Draw
2. Play
  * copper
  * estate
  * etc.
3. Buy

METHODS
-------
Draw()
  * remove from library
  * put in hand

Play()
  * remove from hand -> play

Buy()
  * remove from stockpiles -> discard
  * check $ > cost (later)

DiscardFromPlay()
  * remove from play -> discard

STORAGE OBJECTS
---------------
* deck (list)
  * shuffle


