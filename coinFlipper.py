import random

def coinFlipper():

  HH = 0
  HT = 0
  TT = 0

  for i in range(100):
    
    coinOne = random.randint(0,1)
    coinTwo = random.randint(0,1)
    
    if coinOne == 1 and coinTwo == 1:
      HH += 1
    if (coinOne == 1 and coinTwo == 0) or (coinOne == 0 and coinTwo == 1):
      HT += 1
    if coinOne == 0 and coinTwo == 0:
      TT += 1
      
  return HH, HT, TT
      
def main():
  
  HH, HT, TT = coinFlipper()
  
  print(f"Heads-Heads: {HH}, Tails-Tails: {TT}, Heads-Tails/Tails-Heads {HT}")

main()
