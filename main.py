# page 497 section classes. 

import random 

class Coin:

 def __init__(self):
    self.sideup = 'Heads'

 def toss(self):
    if random.randint(0, 1) == 0:
      self.sideup = 'Heads'
    else:
      self.sideup = 'Tails'

 def get_sideup(self):
    return self.sideup

def main():
  my_coin = Coin()
  print('This side up: ', my_coin.get_sideup())
  print('I am going to toss the Coin!....')
  my_coin.toss()
  print('This side is up:', my_coin.get_sideup())
main()