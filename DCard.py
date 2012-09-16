#!/usr/bin/env python

import logging
import DUtilities

class DCard:
  """
  Any card in the game. The card_type is a list of card types,
  such as Action, Treasure, Victory.
  The action parameter is a function that is called when the card
  is played as an action.

  Properties:
    name : the official Dominion name of the card, as a string
    cost : cost to buy the card in coins
    treasure : value of the card when played for money
    victory_points : worth in victory points
    action : a function taking the player as an argument, called when played
    card_types: a list of the types of the card. A card can have multiple types
      The valid card types are:
      Treasure, Action, Victory, Attack, Reaction, Duration, Curse?, etc.
  """

  def __init__(
    self,
    name,
    cost,
    treasure,
    victory_points,
    action,
    card_types,
  ):
    self.name = name
    self.cost = cost
    self.treasure = treasure
    self.victory_points = victory_points
    self.action = action
    self.card_types = card_types
  
  def printme(self):
    logging.info(
      'Card name  : %s\n' % self.name +
      '  Cost     : %s\n' % self.cost +
      '  Treasure : %s\n' % self.treasure +
      '  Victory  : %s\n' % self.victory_points +
      '  Card types : %s\n' % str(self.card_types)
    )

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

def village_action(player):
  player.draw_card()
  player.add_action()
  player.add_action()

# Dictionary of All card types.
card_dict = {
  'Copper': DCard(
    name='Copper',
    cost=0,
    treasure=1,
    victory_points=0,
    action=None,
    card_types=['Treasure']
  ),

  'Silver': DCard(
    name='Silver',
    cost=3,
    treasure=2,
    victory_points=0,
    action=None,
    card_types=['Treasure']
  ),

  'Gold': DCard(
    name='Gold',
    cost=6,
    treasure=3,
    victory_points=0,
    action=None,
    card_types=['Treasure']
  ),

  'Estate': DCard(
    name='Estate',
    cost=2,
    treasure=0,
    victory_points=1,
    action=None,
    card_types=['Victory']
  ),

  'Duchy': DCard(
    name='Duchy',
    cost=5,
    treasure=0,
    victory_points=3,
    action=None,
    card_types=['Victory']
  ),

  'Province': DCard(
    name='Province',
    cost=8,
    treasure=0,
    victory_points=6,
    action=None,
    card_types=['Victory']
  ),

  'Harem': DCard(
    name='Harem',
    cost=6,
    treasure=2,
    victory_points=2,
    action=None,
    card_types=['Victory','Treasure']
  ),

  'Village': DCard(
    name='Village',
    cost=3,
    treasure=0,
    victory_points=0,
    action=village_action,
    card_types=['Action']
  ),

}

class Copper:
    
    def __init__(self):

        self.name = 'Copper'
        self.cost = 0
        self.value = 1
        self.victory_points = 0


class Estate:
    
    def __init__(self):

        self.name = 'Estate'
        self.cost = 1
        self.value = 0
        self.victory_points = 1


if __name__ == '__main__':

  logging.basicConfig(level=logging.DEBUG, format='%(message)s')

  for card in card_dict.values():
    card.printme()

