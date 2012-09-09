#!/usr/bin/env python

import random

hand = [];
library = [1]*7 + [0]*3;
discard = [];


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
      library.extend(discard)
      discard=[]
      shuffle(library)
      draw_card()

def draw_card():
  hand.append(library.pop(0))

def discard_hand():
  global hand
  discard.extend(hand)
  hand = []

def buy_estate():
  discard.append(0)

def buy_copper():
  discard.append(1)

def dumb_buy_CE_only():
  money = hand.count(1)
  if money>=2:
    print 'money = ' + str(money) + '. Buy Estate.'
    buy_estate()
  else:
    print 'money = ' + str(money) + '. Buy Copper.'
    buy_copper()

def init_game(): # Throwaway to make testing easier
  shuffle(library)
  draw_hand()
  print_all()

def print_all():
  print 'Library: ' + str(library)
  print 'Hand   : ' + str(hand)
  print 'Discard: ' + str(discard)
  

def main() :
  shuffle(library)
  draw_hand()
  print_all()

  n_turns = 1000;
  for i in range(n_turns):  
    print 'Turn ' + str(i)
    dumb_buy_CE_only()
    discard_hand()
    draw_hand()
    print_all()
 
if __name__ == "__main__":
  main()
