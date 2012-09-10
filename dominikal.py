#!/usr/bin/env python

import random
import logging


# Change to logging.DEBUG for more, logging.WARNING for less.
logging.basicConfig(level=logging.INFO, format='%(message)s') 

# for now:
# 1 = copper
# 0 = estate
hand = [];
library = [1]*7 + [0]*3;
discard = [];
stockpile = [1]*10 + [0]*10 


def shuffle(zone) :
  """
  Shuffles the zone as if it were a list.
  random.random() uses a Mersenne twister with a period of 2**19937-1,
  or ~1e6300. The number of permutations of lists grows combinatorically,
  but for even a 200 card deck, there are only 1e460 permutations, so 
  the random.shuffle() method should hit all of these.
  """
  random.shuffle(zone)

def draw_hand():
  global discard
  for i in range(5):
    try:
      draw_card()
    except IndexError: # throws if empty
      logging.debug('Library is empty. Shuffling in discard pile.')
      library.extend(discard)
      discard=[]
      shuffle(library)
      draw_card()

def draw_card():
  logging.debug('Drawing one card.')
  hand.append(library.pop(0))

def discard_hand():
  global hand
  logging.debug('Discarding remaining hand.')
  discard.extend(hand)
  hand = []

def buy_estate():
  logging.debug('Buying an estate. Placing it in the discard pile.')
  stockpile.remove(0)
  discard.append(0)

def buy_copper():
  logging.debug('Buying a copper. Placing it in the discard pile.')
  stockpile.remove(1)
  discard.append(1)

def dumb_buy_CE_only():
  logging.debug('My Hand is : ' + str(hand))
  logging.debug('Deciding what to buy...')
  money = hand.count(1)
  if money>=2:
    logging.debug('money = ' + str(money) + '. Buy Estate.')
    buy_estate()
  else:
    logging.debug('money = ' + str(money) + '. Buy Copper.')
    buy_copper()

def init_game(): # Throwaway to make testing easier
  shuffle(library)
  draw_hand()
  print_all()

def print_all():
  logging.info('Library  : ' + str(library))
  logging.info('Hand     : ' + str(hand))
  logging.info('Discard  : ' + str(discard))
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
  shuffle(library)
  draw_hand()
  print_all()

  n_turns = 1000;
  for i in range(n_turns):  
    # A turn has the following actions in order:
    #  - Play action cards
    #  - Play money in any order
    #  - Buy cards, placing them in the discard pile
    #  - Discard remaining cards in hand
    #  - Draw a new hand of 5 cards
    logging.info('\n === Turn ' + str(i+1) + ' === ')
    dumb_buy_CE_only()
    discard_hand()
    draw_hand()
    print_all()
    if is_game_over(): break 

if __name__ == "__main__":
  main()
