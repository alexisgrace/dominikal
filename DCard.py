#!/usr/bin/env python

import logging
import DUtilities

class DCard:
  """
  Any card in the game. The card_type is a list of card types,
  such as Action, Treasure, Victory.
  The action parameter is a function that is called when the card
  is played as an action.
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

def get_copper():
  return DCard(
    name="Copper",
    cost=0,
    treasure=1,
    victory_points=0,
    action=None,
    card_types=["Treasure"]
  )

