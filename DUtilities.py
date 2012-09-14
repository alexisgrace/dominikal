
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


