import random

class Coin: # creates class
  def __init__(self): # function that creates coin--initializer
    # establish atributes
    self.sideup = 'Heads' # instance variable -- every instance of coin has a side up
    # __.attribute can make an atribute private - means attribute can not be changed in main

# next define menthods
  def toss(self):
    if random.randint(0,1) == 0:
      self.sideup = 'Heads'
    else:
      self.sideup = 'Tails'

  def get_sideup(self): # getter method - return current value
    return self.sideup

# create main method outside of class

def main():
  my_coin = Coin() 
  print('This side is up:', my_coin.get_sideup())
  my_coin.toss()
  print(my_coin.get_sideup())


main()

# can create the class and store it in its own py files -- module
# can import module and use class in main
