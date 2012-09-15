import logging
import random

def shuffle(zone) :
  """
  Shuffles the zone as if it were a list.
  random.random() uses a Mersenne twister with a period of 2**19937-1,
  or ~1e6300. The number of permutations of lists grows combinatorically,
  but for even a 200 card deck, there are only 1e460 permutations, so 
  the random.shuffle() method should hit all of these.
  """
  random.shuffle(zone)

def count_money(zone):
    money = 0
    for card in zone:
        money += card.value
    return money


def count_victory_points(zone):
    points = 0
    for card in zone:
        points += card.victory_points
    return points


def print_zone_nicely(zone):
    logging.info('%i cards:' % len(zone))
    card_dict = {}
    for card in zone:

        try:
            n_cards = card_dict[card.name]
        except KeyError:
            n_cards = 0

        n_cards += 1
        card_dict[card.name] = n_cards
      
    names = card_dict.keys()
    names.sort()

    for name in names:
        n_cards = card_dict[name]

        logging.info('\t %i of %s' % (n_cards, name))


