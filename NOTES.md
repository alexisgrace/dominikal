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

Here's an API for these zone card containers
* put_card_on_bottom()
* put_card_on_top()
* shuffle()
* shuffle_top_cards(n)
* draw_card()
* find_specific_card()
* find_first_card_matching(function)
* reveal_top_n_cards()
* reveal_cards_matching(function)

In this model, the zones are dumb containers, giving and taking what you ask.

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
* draw
* play
  * copper
  * estate
  * etc.  
* buy  

METHODS
-------
* Draw()
  * remove from library
  * put in hand
* Play()
  * remove from hand -> play
* Buy()
  * remove from stockpiles -> discard
  * check $ > cost (later)
* DiscardFromPlay()
  * remove from play -> discard

STORAGE OBJECTS
---------------
* deck (list)
  * shuffle


