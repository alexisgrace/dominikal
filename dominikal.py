#!/usr/bin/env python

import logging
import DPlayer


# Change to logging.DEBUG for more, logging.WARNING for less.
logging.basicConfig(level=logging.INFO, format='%(message)s') 

# for now:
# 1 = copper
# 0 = estate
stockpile = [1]*10 + [0]*10 

def buy_card(player, card):
    logging.debug('Buying a card.')
    try: 
        stockpile.remove(card)
        player.discard.append(card)
    except ValueError:
        logging.info('Card %s is not available' % card)


def buy_estate(player):
  logging.debug('Buying an estate. Placing it in the discard pile.')
  buy_card(player, 0)

def buy_copper(player):
  logging.debug('Buying a copper. Placing it in the discard pile.')
  buy_card(player, 1)

def dumb_buy_CE_only(player):
  logging.debug('My Hand is : ' + str(player.hand))
  logging.debug('Deciding what to buy...')
  money = player.count_money()
  if money>=2:
    logging.debug('money = ' + str(money) + '. Buy Estate.')
    buy_estate(player)
  else:
    logging.debug('money = ' + str(money) + '. Buy Copper.')
    buy_copper(player)

def init_game(): # Throwaway to make testing easier
  test_player.draw_hand()
  test_player.print_all()
  print_all()

def print_all():
  logging.info('Stockpile: ' + str(stockpile))

def is_game_over():
    """
    evaluate whether the game has ended
    """

    # game ends if there are no more estates in the stockpile
    if stockpile.count(0) == 0:
        logging.info('--> Zero Estates left -- GAME OVER --')
        return True

    # game continues if no end-game conditions are met
    return False
  

def main() :
  logging.info('--> Starting the game. Shuffle the library and draw 5 cards.')

  players = []

  player_one = DPlayer.Player('Player 1')
  player_one.draw_hand()
  player_one.print_all()
  players.append(player_one)

  player_two = DPlayer.Player('Player 2')
  player_two.draw_hand()
  player_two.print_all()
  players.append(player_two)

  n_players = len(players)
  n_turns = 10;
  for i in range(n_turns):  
    
    # A turn has the following actions in order:
    #  - Play action cards
    #  - Play money in any order
    #  - Buy cards, placing them in the discard pile
    #  - Discard remaining cards in hand
    #  - Draw a new hand of 5 cards
    logging.info('\n === Turn ' + str(i+1) + ' === ')

    active_player_index = i % n_players
    active_player = players[active_player_index]

    dumb_buy_CE_only(active_player)
    active_player.discard_hand()
    active_player.draw_hand()
    active_player.print_all()

    if is_game_over(): break 


if __name__ == "__main__":
  main()
