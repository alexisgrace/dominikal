#!/usr/bin/env python

import logging
import DCard
import DUtilities


class Player:

    def __init__(
        self,
        name="Player One",
    ):
        self.name = name
        self.hand = []
        self.library = [DCard.card_dict['Copper']]*7 + [DCard.card_dict['Estate']]*3
        self.discard = []
        self.in_play = []
        self.actions_left = 0
        logging.info('New player: %s' % self.name)
        DUtilities.shuffle(self.library)


    def print_all(self):
        logging.info('-------------------------------------')
        logging.info('%s status:' % self.name)
        logging.info('-------------------------------------')
        logging.info('Library  : ' + str(self.library))
        logging.info('Discard  : ' + str(self.discard))
        logging.info('Hand     : ' + str(self.hand))
        logging.info('In Play  : ' + str(self.in_play))
        logging.info('Actions : ' + str(self.actions_left))
        DUtilities.print_zone_nicely(self.hand)
        logging.info('-------------------------------------')


    def discard_hand(self):
        logging.debug('%s: Discarding remaining hand.' % self.name)
        self.discard.extend(self.hand)
        self.hand = []


    def draw_card(self):
        logging.debug('%s: Drawing one card.' % self.name)
        try:
            self.hand.append(self.library.pop(0))
        except IndexError: # throws if empty
            logging.debug('%s: Library is empty. Shuffling in discard pile.' % self.name)
            self.library.extend(self.discard)
            self.discard=[]
            DUtilities.shuffle(self.library)
            try:
                self.hand.append(self.library.pop(0))
            except IndexError:
                logging.info('%s: Cannot draw card. Library is empty.' % self.name)


    def draw_hand(self):
        logging.debug('%s: Drawing hand.' % self.name)
        for i in range(5):
            self.draw_card()


    def count_money(self):
        return DUtilities.count_money(self.hand)
           
    def count_victory_points(self):
        return DUtilities.count_victory_points(
            self.hand + self.library + self.discard
        )

    def play(self, card):
        """
        Error if not enough actions.
        Put card from hand into play. Error if not found.
        Decrement actions_left
        Execute card.action()
        """
        if('Action' in card.card_types and self.actions_left<1): 
            raise Error('Not enough actions to play action card')
        try:
            self.hand.remove(card)
        except ValueError: # list.remove throws if not found
            raise Error('Card doesn\'t exist in the hand:')
        self.in_play.append(card)
        if('Action' in card.card_types): 
          self.actions_left -= 1
          card.action(self)
    
    def add_action(self): self.actions_left += 1


        
           

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format='%(message)s') 

    test_player = Player('Testy McTesterson')
    logging.warning('Adding a Village to the standard starting cards!')
    test_player.library = \
      [DCard.card_dict['Village']]*1 + \
      [DCard.card_dict['Estate']]*3 + \
      [DCard.card_dict['Copper']]*7
    DUtilities.shuffle(test_player.library)
    test_player.print_all()

    test_player.draw_hand()
    test_player.print_all()

    test_player.discard_hand()
    test_player.print_all()

    test_player.draw_hand()
    test_player.print_all()

    test_player.draw_card()
    test_player.print_all()

    test_player.add_action()
    while (
        test_player.actions_left > 0 and 
        DCard.card_dict['Village'] in test_player.hand
        ):
        test_player.play(DCard.card_dict['Village'])

    test_player.print_all()


